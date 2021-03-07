import sys

import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import playsound


WAKE = "écoute"
QUIT = "stop"

def init_voice():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)


def speak(text):
    # tts = gTTS(text=text, lang="fr")
    # filename = "voice.mp3"
    # tts.save(filename)
    # playsound.playsound(filename)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="fr-FR")
            print(said)
        except Exception as e:
            speak("Je n'ai pas compris.")
            print(r)
    return said.lower()

def quit():
    speak("Je m'éteins")

if __name__ == '__main__':
    print("start")
    init_voice()
    while True:
        text = get_audio()
        if text.count(WAKE) > 0:
            speak("Je t'écoute")
            text = get_audio()
            if text.count(QUIT) > 0:
                quit()
                break
            else:
                speak(f"tu as dit {text}")
        if text.count(QUIT) > 0:
            quit()
            break
    sys.exit(0)

