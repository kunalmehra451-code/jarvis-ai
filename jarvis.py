import cv2
from deepface import DeepFace
from elevenlabs import generate, play, set_api_key
import time

# 🔴 PASTE YOUR ELEVENLABS API KEY BELOW
set_api_key("PASTE_YOUR_API_KEY_HERE")

def speak_sweet_voice(text):
    """Generate a natural human-like voice"""
    audio = generate(
        text=text,
        voice="Bella",
        model="eleven_multilingual_v2"
    )
    play(audio)

def start_jarvis_companion():
    cap = cv2.VideoCapture(0)
    print("Jarvis is active. Looking for you...")

    last_interaction_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            if int(time.time()) % 2 == 0:
                result = DeepFace.analyze(
                    frame,
                    actions=["emotion"],
                    enforce_detection=False
                )

                emotion = result[0]["dominant_emotion"]
                current_time = time.time()

                if emotion == "sad" and (current_time - last_interaction_time > 15):
                    response = "Kya hua mere babu ko? Itne upset kyun ho? Please smile karo na."
                    print("Jarvis:", response)
                    speak_sweet_voice(response)
                    last_interaction_time = current_time

        except Exception:
            pass

        cv2.imshow("Jarvis AI", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_jarvis_companion()
