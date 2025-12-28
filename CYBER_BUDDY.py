import os
import time
import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv

# ================= ENV SETUP =================
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# ================= MAC NATIVE TTS =================
def speak(text: str):
    """Native Mac TTS - Fast and Clean"""
    clean_text = text.replace('"', '').replace("'", "")
    print(f"🤖 CyberBuddy: {text}")
    # Using 'say' directly ensures no library conflicts on Mac
    os.system(f'say -v Rishi -r 185 "{clean_text}"')

# ================= GEMINI SETUP =================
SYSTEM_PROMPT = "You are CyberBuddy. Very concise. Address user as SIR."
model = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=SYSTEM_PROMPT)

def get_gemini_response(user_text: str):
    try:
        # Added a safety timeout for the API call
        response = model.generate_content(user_text)
        return response.text.strip()
    except Exception as e:
        return f"API Error: {str(e)}"

# ================= MAIN LOOP =================
def main():
    r = sr.Recognizer()
    
    # ADJUSTING THESE FOR SPEED
    r.energy_threshold = 400 
    r.dynamic_energy_threshold = False # Fixed threshold is often more stable on Mac
    r.pause_threshold = 0.6            # Faster detection of end-of-speech

    print("⚡ CyberBuddy Initializing...")
    
    with sr.Microphone() as source:
        print("🔧 One-time calibration...")
        r.adjust_for_ambient_noise(source, duration=1)
    
    speak("I am online, SIR. Ask me anything.")

    while True:
        try:
            with sr.Microphone() as source:
                print("\n🎤 Listening...")
                # phrase_time_limit keeps the audio chunks small and fast
                audio = r.listen(source, phrase_time_limit=5, timeout=None)

            print("⌛ Recognizing...")
            # Use 'show_all=False' to get the quickest string return
            user_text = r.recognize_google(audio, language="en-IN")
            
            if not user_text:
                continue

            print(f"🗣 You: {user_text}")

            if any(word in user_text.lower() for word in ["exit", "stop", "quit"]):
                speak("Shutting down. Goodbye SIR.")
                break
            
            # 1. Get Response
            reply = get_gemini_response(user_text)
            
            # 2. Speak Response
            speak(reply)

        except sr.UnknownValueError:
            # This happens if you didn't say anything clearly
            print("❓ Silence detected...")
            continue
        except sr.RequestError as e:
            print(f"❌ Google Speech API is down: {e}")
            continue
        except Exception as e:
            print(f"⚠️ Unexpected Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()
