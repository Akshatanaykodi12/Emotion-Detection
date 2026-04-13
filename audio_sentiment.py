import speech_recognition as sr
from text_sentiment import detect_emotion_from_text
from pydub import AudioSegment
import os

# IMPORTANT: change this only if your ffmpeg is in another folder
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"


def detect_emotion_from_audio(audio_file_path):
    recognizer = sr.Recognizer()
    wav_path = "converted_audio.wav"

    try:
        # Convert browser audio (webm) to wav
        audio = AudioSegment.from_file(audio_file_path)
        audio.export(wav_path, format="wav")

        # Read converted wav
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)

        # Convert speech to text
        text = recognizer.recognize_google(audio_data)

        # Detect emotion from text
        emotion = detect_emotion_from_text(text)

        return {
            "transcribed_text": text,
            "emotion": emotion
        }

    except sr.UnknownValueError:
        return {
            "transcribed_text": "Could not understand audio clearly",
            "emotion": "neutral"
        }

    except sr.RequestError:
        return {
            "transcribed_text": "Speech recognition service error",
            "emotion": "neutral"
        }

    except Exception as e:
        return {
            "transcribed_text": f"Audio conversion/processing failed: {str(e)}",
            "emotion": "neutral"
        }

    finally:
        if os.path.exists(wav_path):
            os.remove(wav_path)