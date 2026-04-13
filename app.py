from flask import Flask, render_template, request, jsonify
from emotion_detector import detect_emotion_from_base64
from content_logic import get_adaptive_content
from text_sentiment import detect_emotion_from_text
from audio_sentiment import detect_emotion_from_audio
from datetime import datetime
import json
import os

app = Flask(__name__)


def safe_content_fields(content):
    defaults = {
        "quote": "Stay centered and take a deep breath.",
        "suggestion": "Notice your current feeling and choose one calm action.",
        "videos": [],
        "music": [],
        "exercise": "Try a short breathing exercise.",
        "extra": "Remember your emotions are valid and temporary."
    }
    if not isinstance(content, dict):
        return defaults
    return {key: content.get(key, defaults[key]) for key in defaults}


@app.route('/')
def home():
    return render_template('index.html')


# ---------------- FACE EMOTION ----------------
@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    image_data = data['image']

    emotion_result = detect_emotion_from_base64(image_data)

    # Support both old and new detector outputs safely
    if isinstance(emotion_result, dict):
        emotion = emotion_result.get("dominant_emotion", "neutral")
        emotion_scores = emotion_result.get("emotion_scores", {})
    else:
        emotion = emotion_result
        emotion_scores = {}

    content = safe_content_fields(get_adaptive_content(emotion))

    log_entry = {
        "input_type": "face",
        "emotion": emotion,
        "scores": emotion_scores,
        "quote": content["quote"],
        "suggestion": content["suggestion"],
        "videos": content["videos"],
        "music": content["music"],
        "exercise": content["exercise"],
        "extra": content["extra"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    log_file = "emotion_log.json"

    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    else:
        logs = []

    logs.append(log_entry)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)

    return jsonify({
        "emotion": emotion,
        "scores": emotion_scores,
        "quote": content["quote"],
        "suggestion": content["suggestion"],
        "videos": content["videos"],
        "music": content["music"],
        "exercise": content["exercise"],
        "extra": content["extra"]
    })


# ---------------- TEXT SENTIMENT ----------------
@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    data = request.get_json()
    user_text = data['text']

    emotion = detect_emotion_from_text(user_text)
    content = safe_content_fields(get_adaptive_content(emotion))

    log_entry = {
        "input_type": "text",
        "user_text": user_text,
        "emotion": emotion,
        "quote": content["quote"],
        "suggestion": content["suggestion"],
        "videos": content["videos"],
        "music": content["music"],
        "exercise": content["exercise"],
        "extra": content["extra"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    log_file = "emotion_log.json"

    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    else:
        logs = []

    logs.append(log_entry)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)

    return jsonify({
        "emotion": emotion,
        "quote": content["quote"],
        "suggestion": content["suggestion"],
        "videos": content["videos"],
        "music": content["music"],
        "exercise": content["exercise"],
        "extra": content["extra"]
    })


# ---------------- AUDIO SENTIMENT ----------------
@app.route('/analyze_audio', methods=['POST'])
def analyze_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files['audio']
    audio_path = "temp_audio.webm"
    audio_file.save(audio_path)

    result = detect_emotion_from_audio(audio_path)
    emotion = result["emotion"]
    transcribed_text = result["transcribed_text"]

    content = safe_content_fields(get_adaptive_content(emotion))

    log_entry = {
        "input_type": "audio",
        "transcribed_text": transcribed_text,
        "emotion": emotion,
        "quote": content["quote"],
        "suggestion": content["suggestion"],
        "videos": content["videos"],
        "music": content["music"],
        "exercise": content["exercise"],
        "extra": content["extra"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    log_file = "emotion_log.json"

    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    else:
        logs = []

    logs.append(log_entry)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)

    if os.path.exists(audio_path):
        os.remove(audio_path)

    return jsonify({
        "emotion": emotion,
        "transcribed_text": transcribed_text,
        "quote": content["quote"],
        "suggestion": content["suggestion"],
        "videos": content["videos"],
        "music": content["music"],
        "exercise": content["exercise"],
        "extra": content["extra"]
    })

@app.route('/get_history', methods=['GET'])
def get_history():
    log_file = "emotion_log.json"

    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    else:
        logs = []

    emotion_counts = {
        "happy": 0,
        "sad": 0,
        "angry": 0,
        "fear": 0,
        "surprise": 0,
        "neutral": 0,
        "disgust": 0
    }

    for entry in logs:
        emotion = entry.get("emotion", "neutral").lower()
        if emotion in emotion_counts:
            emotion_counts[emotion] += 1

    return jsonify({
        "history": logs[::-1],
        "analytics": emotion_counts
    })


@app.route('/clear_history', methods=['POST'])
def clear_history():
    log_file = "emotion_log.json"

    with open(log_file, "w") as f:
        json.dump([], f, indent=4)

    return jsonify({"message": "History cleared successfully"})

if __name__ == '__main__':
    app.run(debug=True)