# from textblob import TextBlob


# def detect_emotion_from_text(user_text):
#     text = user_text.lower().strip()

#     # Rule-based keywords first (better for your project demo)
#     if any(word in text for word in ["sad", "depressed", "unhappy", "cry", "lonely", "hurt", "tired"]):
#         return "sad"

#     elif any(word in text for word in ["angry", "mad", "furious", "annoyed", "irritated", "hate"]):
#         return "angry"

#     elif any(word in text for word in ["happy", "joy", "excited", "great", "awesome", "good", "wonderful"]):
#         return "happy"

#     elif any(word in text for word in ["fear", "afraid", "scared", "nervous", "anxious", "worried"]):
#         return "fear"

#     elif any(word in text for word in ["surprised", "shocked", "unexpected", "wow", "amazing"]):
#         return "surprise"

#     elif any(word in text for word in ["disgust", "gross", "disappointed", "bad", "awful"]):
#         return "disgust"

#     # Fallback using TextBlob sentiment polarity
#     polarity = TextBlob(text).sentiment.polarity

#     if polarity > 0.3:
#         return "happy"
#     elif polarity < -0.3:
#         return "sad"
#     else:
#         return "neutral"

import os
import re
import requests

KEYWORD_EMOTIONS = {
    "sad": ["sad", "depressed", "unhappy", "cry", "lonely", "hurt", "tired"],
    "angry": ["angry", "mad", "furious", "annoyed", "irritated", "hate"],
    "happy": ["happy", "joy", "excited", "great", "awesome", "good", "wonderful"],
    "fear": ["fear", "afraid", "scared", "nervous", "anxious", "worried"],
    "surprise": ["surprised", "shocked", "unexpected", "wow", "amazing"],
    "disgust": ["disgust", "gross", "disappointed", "bad", "awful"]
}


def rule_based_emotion(user_text):
    text = user_text.lower()
    for emotion, terms in KEYWORD_EMOTIONS.items():
        if any(term in text for term in terms):
            return emotion
    return "neutral"


def parse_groq_response(response):
    try:
        data = response.json()
    except ValueError:
        return None

    if not isinstance(data, dict):
        return None

    if "choices" in data and isinstance(data["choices"], list) and data["choices"]:
        message = data["choices"][0].get("message")
        if isinstance(message, dict) and "content" in message:
            return message["content"].strip()

    # fallback for nonstandard Groq output
    text = data.get("content") if isinstance(data.get("content"), str) else None
    return text


def normalize_emotion_label(raw_emotion):
    if not isinstance(raw_emotion, str):
        return "neutral"

    text = raw_emotion.lower()
    for emotion, terms in KEYWORD_EMOTIONS.items():
        if any(term in text for term in terms):
            return emotion

    if "happy" in text or "joy" in text:
        return "happy"
    if "sad" in text or "depress" in text:
        return "sad"
    if "angry" in text or "furious" in text:
        return "angry"
    if "fear" in text or "scared" in text or "anxious" in text:
        return "fear"
    if "surprise" in text or "shocked" in text:
        return "surprise"
    if "disgust" in text or "gross" in text:
        return "disgust"

    return "neutral"


def detect_emotion_from_text(user_text):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return rule_based_emotion(user_text)

    url = "https://api.groq.com/openai/v1/chat/completions"
    model_name = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
    print(f"[Groq API] using model: {model_name}")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "You are an emotion detection assistant."},
            {"role": "user", "content": f"Classify the emotion in this text: {user_text}"}
        ],
        "temperature": 0.0
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
    except requests.RequestException as exc:
        print(f"[Groq API] request failed: {exc}")
        return rule_based_emotion(user_text)

    if response.status_code != 200:
        try:
            error_data = response.json()
            if isinstance(error_data, dict) and error_data.get("error"):
                err = error_data["error"]
                if err.get("code") == "model_not_found":
                    print(f"[Groq API] model not found: {model_name}. Set GROQ_MODEL to a valid accessible model.")
                print(f"[Groq API] non-200 status: {response.status_code} - {err.get('message')}")
        except ValueError:
            print(f"[Groq API] non-200 status: {response.status_code} - {response.text}")
        return rule_based_emotion(user_text)

    raw_emotion = parse_groq_response(response)
    emotion = normalize_emotion_label(raw_emotion)
    if emotion == "neutral" and raw_emotion:
        emotion = rule_based_emotion(user_text)

    return emotion
