import ast
import json
import os
import re
import requests
from urllib.parse import quote_plus

YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

DEFAULT_CONTENT = {
    "quote": "Stay present and keep moving forward.",
    "suggestion": "Take a slow breath and respond with kindness to yourself.",
    "videos": ["https://www.youtube.com/watch?v=inpok4MKVLM"],
    "music": ["https://www.youtube.com/watch?v=5qap5aO4i9A"],
    "exercise": "Try 5 slow breaths while focusing on your body.",
    "extra": "Remember that emotions are temporary and it's okay to ask for help."
}


def extract_urls_from_string(text):
    if not isinstance(text, str):
        return []
    return re.findall(r"https?://[^\s,;]+", text)


def normalize_media_list(value):
    if isinstance(value, list):
        urls = []
        for item in value:
            if isinstance(item, str):
                item_urls = extract_urls_from_string(item)
                if item_urls:
                    urls.extend(item_urls)
                else:
                    item = item.strip()
                    if item:
                        urls.append(item)
        return [u for u in urls if u]

    if isinstance(value, str):
        urls = extract_urls_from_string(value)
        if urls:
            return urls
        items = [x.strip() for x in re.split(r"[\n,;]+", value) if x.strip()]
        return items

    return []


def build_youtube_search_urls(query, max_results=3):
    if not query:
        return []
    variation_prompts = [
        query,
        f"{query} playlist",
        f"{query} calming",
        f"{query} guided"
    ]
    return [f"https://www.youtube.com/results?search_query={quote_plus(term)}" for term in variation_prompts[:max_results]]


def get_youtube_videos(query, max_results=3):
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        print("[YouTube API] YOUTUBE_API_KEY is not set. Using search page fallback for dynamic media.")
        return build_youtube_search_urls(query, max_results)

    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": api_key
    }

    try:
        response = requests.get(YOUTUBE_SEARCH_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        items = data.get("items", [])
        urls = []
        for item in items:
            video_id = item.get("id", {}).get("videoId")
            if video_id:
                urls.append(f"https://www.youtube.com/watch?v={video_id}")
        return urls if urls else build_youtube_search_urls(query, max_results)
    except requests.RequestException as exc:
        print(f"[YouTube API] search failed: {exc}")
    except ValueError as exc:
        print(f"[YouTube API] invalid JSON: {exc}")
    return build_youtube_search_urls(query, max_results)


def get_emotion_search_query(emotion, category):
    base = emotion.replace("_", " ")
    if category == "video":
        return f"{base} wellbeing videos"
    if category == "music":
        return f"{base} mood music playlist"
    return base


def clean_json_like_text(raw_text):
    if not isinstance(raw_text, str):
        return raw_text

    text = raw_text
    # Remove JavaScript-style comments, but keep URL schemes like http:// and https://
    text = re.sub(r"(?<!:)//.*?$", "", text, flags=re.MULTILINE)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    # Remove trailing commas before object/array close
    text = re.sub(r",\s*(?=[}\]])", "", text)
    return text


def parse_response_content(raw_text):
    if isinstance(raw_text, dict):
        return raw_text

    if not isinstance(raw_text, str):
        return None

    raw_text = raw_text.strip()
    cleaned = clean_json_like_text(raw_text)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    try:
        return ast.literal_eval(cleaned)
    except (ValueError, SyntaxError):
        pass

    match = re.search(r"\{.*\}", cleaned, re.S)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass

    return None


def get_default_adaptive_content(emotion=None):
    result = DEFAULT_CONTENT.copy()
    if emotion:
        result["videos"] = build_youtube_search_urls(get_emotion_search_query(emotion, "video"), max_results=3)
        result["music"] = build_youtube_search_urls(get_emotion_search_query(emotion, "music"), max_results=3)
    return result


def get_adaptive_content(emotion):
    url = "https://api.groq.com/openai/v1/chat/completions"
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("[Groq API] GROQ_API_KEY is not set. Using default adaptive content with emotion-specific media links.")
        return get_default_adaptive_content(emotion)

    model_name = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
    print(f"[Groq API] using model: {model_name}")
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    prompt = f"""
    You are an assistant that provides adaptive wellbeing content.
    Based on the emotion '{emotion}', generate:
    - One motivational quote
    - One practical suggestion
    - One short exercise
    - One extra tip
    Return the result in strict JSON format with keys: quote, suggestion, exercise, extra.
    Use a JSON object only, without explanatory text.
    """

    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "You are a wellbeing content assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
    except requests.RequestException as exc:
        print(f"[Groq API] request failed: {exc}")
        return get_default_adaptive_content(emotion)

    if response.status_code != 200:
        error_message = response.text
        try:
            error_data = response.json()
            if isinstance(error_data, dict) and error_data.get("error"):
                err = error_data["error"]
                error_message = err.get("message", error_message)
                if err.get("code") == "model_not_found":
                    print(f"[Groq API] model not found: {model_name}. Set GROQ_MODEL to a valid accessible model.")
        except ValueError:
            pass
        print(f"[Groq API] non-200 status: {response.status_code} - {error_message}")
        return get_default_adaptive_content(emotion)

    try:
        data = response.json()
        raw_content = None
        if isinstance(data, dict):
            choices = data.get("choices")
            if isinstance(choices, list) and choices:
                message = choices[0].get("message")
                if isinstance(message, dict):
                    raw_content = message.get("content")
            if raw_content is None:
                raw_content = data.get("content")

        parsed = parse_response_content(raw_content)
        if isinstance(parsed, dict):
            videos = get_youtube_videos(get_emotion_search_query(emotion, "video"), max_results=3) or DEFAULT_CONTENT["videos"]
            music = get_youtube_videos(get_emotion_search_query(emotion, "music"), max_results=3) or DEFAULT_CONTENT["music"]

            result = {
                "quote": str(parsed.get("quote", DEFAULT_CONTENT["quote"])),
                "suggestion": str(parsed.get("suggestion", DEFAULT_CONTENT["suggestion"])),
                "exercise": str(parsed.get("exercise", DEFAULT_CONTENT["exercise"])),
                "extra": str(parsed.get("extra", DEFAULT_CONTENT["extra"])),
                "videos": videos,
                "music": music
            }
            if any(result[key] != DEFAULT_CONTENT[key] for key in ["quote", "suggestion", "exercise", "extra"]) or videos != DEFAULT_CONTENT["videos"] or music != DEFAULT_CONTENT["music"]:
                return result
            print(f"[Groq API] parsed response but missing custom data, using defaults: {parsed}")
        else:
            print(f"[Groq API] could not parse content: {raw_content}")
    except (ValueError, KeyError, IndexError) as exc:
        print(f"[Groq API] response parse error: {exc}")

    return get_default_adaptive_content(emotion)
