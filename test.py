import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="fr")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("start listening...")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="fr-FR")
            print(said)
        except Exception as e:
            print(r)
    return said.lower()

text = get_audio()

speak(f"tu as dit {text}")