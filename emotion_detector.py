import base64
import cv2
import numpy as np
from deepface import DeepFace


def detect_emotion_from_base64(base64_image):
    try:
        # Remove header like "data:image/png;base64,..."
        if "," in base64_image:
            base64_image = base64_image.split(",")[1]

        image_data = base64.b64decode(base64_image)
        np_arr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        result = DeepFace.analyze(
            img_path=img,
            actions=['emotion'],
            enforce_detection=False
        )

        if isinstance(result, list):
            result = result[0]

        dominant_emotion = result["dominant_emotion"]
        emotion_scores = {
            k: float(v) for k, v in result["emotion"].items()
        }

        return {
            "dominant_emotion": dominant_emotion,
            "emotion_scores": emotion_scores
        }

    except Exception as e:
        print("Emotion Detection Error:", e)
        return {
            "dominant_emotion": "neutral",
            "emotion_scores": {
                "angry": 0.0,
                "disgust": 0.0,
                "fear": 0.0,
                "happy": 0.0,
                "sad": 0.0,
                "surprise": 0.0,
                "neutral": 100.0
            }
        }