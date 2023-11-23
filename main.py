#PERSONAL AI PROJECT

import speech_recognition
import pyttsx3
from abilities import Abilities

engine = pyttsx3.init()
voices = engine.getProperty("voices")
recognizer = speech_recognition.Recognizer()
run = True

while run:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio).lower()
            if 'claude' in text:
                skill = Abilities(text).work()
                print(f"Recognized {text}")
                engine.setProperty('voice', voices[0].id)
                engine.say(skill)
                engine.runAndWait()
                if "sir" in skill:
                    run = False
            elif 'claudia' in text:
                skill = Abilities(text).work()
                print(f"Recognized {text}")
                engine.setProperty('voice', voices[1].id)
                engine.say(skill)
                engine.runAndWait()
                if "sir" in skill:
                    run = False

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue

