# import random

# def get_adaptive_content(emotion):
#     emotion = emotion.lower()

#     content_map = {
#         "happy": {
#             "quotes": [
#                 "Happiness is contagious. Keep spreading your smile! 😊",
#                 "Smile, it confuses people and brightens the room.",
#                 "Joy shared is joy doubled.",
#                 "A happy mind creates a happy life.",
#                 "Let your happiness inspire others."
#             ],
#             "suggestions": [
#                 "Celebrate your mood and share positivity with someone.",
#                 "Use this good energy to complete something meaningful.",
#                 "Take a happy selfie and save the moment.",
#                 "Spread your positive mood by helping someone.",
#                 "Listen to your favorite upbeat song."
#             ],
#             "videos": [
#                 "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
#                 "https://www.youtube.com/watch?v=OPf0YbXqDm0",
#                 "https://www.youtube.com/watch?v=JGwWNGJdvx8",
#                 "https://www.youtube.com/watch?v=fRh_vgS2dFE",
#                 "https://www.youtube.com/watch?v=60ItHLz5WEA"
#             ],
#             "music": [
#                 "https://www.youtube.com/watch?v=y6Sxv-sUYtM",
#                 "https://www.youtube.com/watch?v=3JZ4pnNtyxQ",
#                 "https://www.youtube.com/watch?v=09R8_2nJtjg",
#                 "https://www.youtube.com/watch?v=KQetemT1sWc",
#                 "https://www.youtube.com/watch?v=RgKAFK5djSk"
#             ],
#             "exercises": [
#                 "Write down 3 things that made you happy today.",
#                 "Dance for 2 minutes to your favorite song.",
#                 "Share one positive message with a friend.",
#                 "Take a short gratitude break and smile intentionally.",
#                 "Stand up and stretch while thinking of one good memory."
#             ],
#             "extras": [
#                 "Positive Challenge: Compliment one person today 🌟",
#                 "Happiness Tip: Capture this mood in a journal.",
#                 "Energy Boost: Use your mood to start a pending task.",
#                 "Joy Tip: Spread your smile to someone nearby.",
#                 "Wellbeing Tip: Celebrate small wins today."
#             ]
#         },

#         "sad": {
#             "quotes": [
#                 "Tough times never last, but tough people do. 💙",
#                 "It’s okay to feel sad. Healing takes time.",
#                 "Even the darkest night will end and the sun will rise.",
#                 "You are allowed to pause, breathe, and begin again.",
#                 "Your feelings are valid, but they are not permanent."
#             ],
#             "suggestions": [
#                 "Take a small break and do something comforting.",
#                 "Drink water and sit somewhere peaceful for a few minutes.",
#                 "Talk to someone you trust if you feel like it.",
#                 "Step outside and get a little fresh air.",
#                 "Watch something gentle or uplifting."
#             ],
#             "videos": [
#                 "https://www.youtube.com/watch?v=mgmVOuLgFB0",
#                 "https://www.youtube.com/watch?v=ZXsQAXx_ao0",
#                 "https://www.youtube.com/watch?v=26U_seo0a1g",
#                 "https://www.youtube.com/watch?v=2Lz0VOltZKA",
#                 "https://www.youtube.com/watch?v=wnHW6o8WMas"
#             ],
#             "music": [
#                 "https://www.youtube.com/watch?v=2OEL4P1Rz04",
#                 "https://www.youtube.com/watch?v=DWcJFNfaw9c",
#                 "https://www.youtube.com/watch?v=5qap5aO4i9A",
#                 "https://www.youtube.com/watch?v=lFcSrYw-ARY",
#                 "https://www.youtube.com/watch?v=UfcAVejslrU"
#             ],
#             "exercises": [
#                 "Try a 2-minute deep breathing exercise: inhale for 4, hold for 4, exhale for 6.",
#                 "Place one hand on your chest and take 5 slow breaths.",
#                 "Write one thing you want to let go of today.",
#                 "Sit quietly and listen to calm music for 2 minutes.",
#                 "Close your eyes and relax your shoulders slowly."
#             ],
#             "extras": [
#                 "Uplifting Tip: Talk to a close friend or listen to calming music.",
#                 "Gentle Reminder: You do not need to fix everything today.",
#                 "Comfort Tip: Rest is also productive sometimes.",
#                 "Healing Tip: Be kind to yourself today.",
#                 "Support Tip: Reach out instead of carrying it alone."
#             ]
#         },

#         "angry": {
#             "quotes": [
#                 "For every minute you are angry, you lose sixty seconds of peace. ❤️",
#                 "Calmness is power.",
#                 "A moment of patience can save hours of regret.",
#                 "Breathe first, react later.",
#                 "Peace begins when anger pauses."
#             ],
#             "suggestions": [
#                 "Pause before reacting. Take a few deep breaths.",
#                 "Step away from the situation for a minute.",
#                 "Drink some water and reset your thoughts.",
#                 "Avoid replying immediately if you're upset.",
#                 "Channel your energy into movement or a short walk."
#             ],
#             "videos": [
#                 "https://www.youtube.com/watch?v=9WgP4u5mY7s",
#                 "https://www.youtube.com/watch?v=inpok4MKVLM",
#                 "https://www.youtube.com/watch?v=O-6f5wQXSu8",
#                 "https://www.youtube.com/watch?v=1ZYbU82GVz4",
#                 "https://www.youtube.com/watch?v=tybOi4hjZFQ"
#             ],
#             "music": [
#                 "https://www.youtube.com/watch?v=lFcSrYw-ARY",
#                 "https://www.youtube.com/watch?v=UfcAVejslrU",
#                 "https://www.youtube.com/watch?v=5qap5aO4i9A",
#                 "https://www.youtube.com/watch?v=DWcJFNfaw9c",
#                 "https://www.youtube.com/watch?v=2OEL4P1Rz04"
#             ],
#             "exercises": [
#                 "Anger Control Exercise: Count backwards from 20 slowly while breathing deeply.",
#                 "Unclench your fists and relax your jaw slowly.",
#                 "Take 10 slow breaths without looking at your phone.",
#                 "Walk around the room for one minute before responding.",
#                 "Write what made you angry, then tear the paper."
#             ],
#             "extras": [
#                 "Meditation Tip: Relax your shoulders and unclench your jaw.",
#                 "Control Tip: Delay your reaction by 60 seconds.",
#                 "Calm Tip: Silence can be stronger than anger.",
#                 "Mind Reset: Your next action matters more than your first feeling.",
#                 "Peace Tip: Step away before you say something you regret."
#             ]
#         },

#         "neutral": {
#             "quotes": [
#                 "All is well. Stay balanced. ⚖️",
#                 "Calm is a quiet kind of strength.",
#                 "A balanced mind makes better decisions.",
#                 "Stillness also has value.",
#                 "Peaceful moments deserve attention too."
#             ],
#             "suggestions": [
#                 "Take a moment for mindfulness or light stretching.",
#                 "Use this stable mood to focus on something important.",
#                 "Do a small productive task right now.",
#                 "Organize one small part of your day.",
#                 "Take a short break and reset your attention."
#             ],
#             "videos": [
#                 "https://www.youtube.com/watch?v=inpok4MKVLM",
#                 "https://www.youtube.com/watch?v=ZToicYcHIOU",
#                 "https://www.youtube.com/watch?v=86m4RC_ADEY",
#                 "https://www.youtube.com/watch?v=tybOi4hjZFQ",
#                 "https://www.youtube.com/watch?v=O-6f5wQXSu8"
#             ],
#             "music": [
#                 "https://www.youtube.com/watch?v=5qap5aO4i9A",
#                 "https://www.youtube.com/watch?v=DWcJFNfaw9c",
#                 "https://www.youtube.com/watch?v=UfcAVejslrU",
#                 "https://www.youtube.com/watch?v=lFcSrYw-ARY",
#                 "https://www.youtube.com/watch?v=2OEL4P1Rz04"
#             ],
#             "exercises": [
#                 "Focus Exercise: Sit quietly for 1 minute and observe your breathing.",
#                 "Stretch your neck and shoulders for 30 seconds.",
#                 "Close your eyes and count 10 slow breaths.",
#                 "Write one priority for the next hour.",
#                 "Stand up and take a mindful pause."
#             ],
#             "extras": [
#                 "Productivity Tip: Plan one useful thing for the next hour.",
#                 "Balance Tip: Keep your energy steady and focused.",
#                 "Clarity Tip: Use calm moments to think clearly.",
#                 "Wellness Tip: Stability is also a healthy state.",
#                 "Mind Tip: A neutral mood is a good time to reset."
#             ]
#         },

#         "surprise": {
#             "quotes": [
#                 "Life is full of unexpected moments — embrace them! 😲",
#                 "Surprises can become beautiful memories.",
#                 "Not every unexpected moment is a bad one.",
#                 "Stay open to what life brings.",
#                 "Wonder begins where certainty ends."
#             ],
#             "suggestions": [
#                 "Take a moment to settle and process what you’re feeling.",
#                 "Pause and understand why you feel surprised.",
#                 "Breathe slowly and let the moment settle.",
#                 "Observe your thoughts before reacting quickly.",
#                 "Use this moment to reflect before acting."
#             ],
#             "videos": [
#                 "https://www.youtube.com/watch?v=1ZYbU82GVz4",
#                 "https://www.youtube.com/watch?v=inpok4MKVLM",
#                 "https://www.youtube.com/watch?v=86m4RC_ADEY",
#                 "https://www.youtube.com/watch?v=tybOi4hjZFQ",
#                 "https://www.youtube.com/watch?v=O-6f5wQXSu8"
#             ],
#             "music": [
#                 "https://www.youtube.com/watch?v=DWcJFNfaw9c",
#                 "https://www.youtube.com/watch?v=5qap5aO4i9A",
#                 "https://www.youtube.com/watch?v=UfcAVejslrU",
#                 "https://www.youtube.com/watch?v=lFcSrYw-ARY",
#                 "https://www.youtube.com/watch?v=2OEL4P1Rz04"
#             ],
#             "exercises": [
#                 "Grounding Exercise: Name 5 things you can see around you.",
#                 "Take 3 slow breaths and observe your surroundings.",
#                 "Sit still for 30 seconds before reacting.",
#                 "Write one word that describes your current feeling.",
#                 "Touch a nearby object and focus on its texture."
#             ],
#             "extras": [
#                 "Calm Tip: Unexpected moments are easier to handle when you pause first.",
#                 "Awareness Tip: Not every surprise needs instant action.",
#                 "Focus Tip: Slow down your response to stay clear.",
#                 "Mindfulness Tip: Observe before reacting.",
#                 "Reset Tip: Let the emotion settle before deciding anything."
#             ]
#         },

#         "fear": {
#             "quotes": [
#                 "You are stronger than your fears. 🌱",
#                 "Courage is not the absence of fear, but moving through it.",
#                 "Fear becomes smaller when faced gently.",
#                 "Take one step at a time — that is enough.",
#                 "You have handled difficult moments before."
#             ],
#             "suggestions": [
#                 "Take slow breaths and remind yourself you are safe.",
#                 "Focus only on what is in front of you right now.",
#                 "Avoid overthinking the worst-case scenario.",
#                 "Sit down and ground yourself for a minute.",
#                 "Repeat one calming sentence to yourself."
#             ],
#             "videos": [
#                 "https://www.youtube.com/watch?v=O-6f5wQXSu8",
#                 "https://www.youtube.com/watch?v=inpok4MKVLM",
#                 "https://www.youtube.com/watch?v=1ZYbU82GVz4",
#                 "https://www.youtube.com/watch?v=86m4RC_ADEY",
#                 "https://www.youtube.com/watch?v=tybOi4hjZFQ"
#             ],
#             "music": [
#                 "https://www.youtube.com/watch?v=UfcAVejslrU",
#                 "https://www.youtube.com/watch?v=DWcJFNfaw9c",
#                 "https://www.youtube.com/watch?v=5qap5aO4i9A",
#                 "https://www.youtube.com/watch?v=lFcSrYw-ARY",
#                 "https://www.youtube.com/watch?v=2OEL4P1Rz04"
#             ],
#             "exercises": [
#                 "Breathing Exercise: Inhale for 4 seconds, exhale for 6 seconds, repeat 5 times.",
#                 "Place both feet firmly on the ground and breathe slowly.",
#                 "Name 3 things you can hear around you.",
#                 "Count 10 breaths without rushing.",
#                 "Hold something nearby and focus on staying present."
#             ],
#             "extras": [
#                 "Reassurance Tip: Focus only on what you can control right now.",
#                 "Calm Tip: Fear often feels bigger than it is.",
#                 "Grounding Tip: Stay with the present moment.",
#                 "Courage Tip: Small calm actions matter.",
#                 "Support Tip: You do not have to face everything alone."
#             ]
#         },

#         "disgust": {
#             "quotes": [
#                 "Sometimes discomfort is a signal to reset and refresh. 🌿",
#                 "Not every unpleasant feeling needs to stay with you.",
#                 "A reset can begin with one deep breath.",
#                 "Release what disturbs your peace.",
#                 "Step back, clear your mind, and begin again."
#             ],
#             "suggestions": [
#                 "Step away for a moment and clear your mind.",
#                 "Wash your face and take a fresh pause.",
#                 "Shift your attention to something lighter.",
#                 "Take a small reset break away from the trigger.",
#                 "Breathe deeply and refocus your thoughts."
#             ],
#             "videos": [
#                 "https://www.youtube.com/watch?v=inpok4MKVLM",
#                 "https://www.youtube.com/watch?v=86m4RC_ADEY",
#                 "https://www.youtube.com/watch?v=tybOi4hjZFQ",
#                 "https://www.youtube.com/watch?v=O-6f5wQXSu8",
#                 "https://www.youtube.com/watch?v=1ZYbU82GVz4"
#             ],
#             "music": [
#                 "https://www.youtube.com/watch?v=5qap5aO4i9A",
#                 "https://www.youtube.com/watch?v=DWcJFNfaw9c",
#                 "https://www.youtube.com/watch?v=UfcAVejslrU",
#                 "https://www.youtube.com/watch?v=lFcSrYw-ARY",
#                 "https://www.youtube.com/watch?v=2OEL4P1Rz04"
#             ],
#             "exercises": [
#                 "Reset Exercise: Wash your face, take a breath, and refocus.",
#                 "Open a window or move to a fresher space.",
#                 "Take 5 slow breaths while relaxing your face.",
#                 "Stretch your arms and release body tension.",
#                 "Look away from the trigger and ground yourself."
#             ],
#             "extras": [
#                 "Mind Reset Tip: Shift attention to something peaceful.",
#                 "Clarity Tip: Step away and let your mind cool down.",
#                 "Fresh Start Tip: A short reset can change your mood.",
#                 "Wellness Tip: Clear discomfort before continuing.",
#                 "Pause Tip: Give yourself space to mentally reset."
#             ]
#         }
#     }

#     selected = content_map.get(emotion, content_map["neutral"])

#     return {
#         "quote": random.choice(selected["quotes"]),
#         "suggestion": random.choice(selected["suggestions"]),
#         "videos": selected["videos"],
#         "music": selected["music"],
#         "exercise": random.choice(selected["exercises"]),
#         "extra": random.choice(selected["extras"])
#     }

import ast
import json
import os
import re
import requests

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


def get_youtube_videos(query, max_results=3):
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        return []

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
        return urls
    except requests.RequestException as exc:
        print(f"[YouTube API] search failed: {exc}")
    except ValueError as exc:
        print(f"[YouTube API] invalid JSON: {exc}")
    return []


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


def get_default_adaptive_content():
    return DEFAULT_CONTENT.copy()


def get_adaptive_content(emotion):
    url = "https://api.groq.com/openai/v1/chat/completions"
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("[Groq API] GROQ_API_KEY is not set. Using default adaptive content.")
        return get_default_adaptive_content()

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
        return get_default_adaptive_content()

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
        return get_default_adaptive_content()

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

    return get_default_adaptive_content()
