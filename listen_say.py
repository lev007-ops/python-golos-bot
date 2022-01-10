import speech_recognition

from actions import NO_RECOGNIZE

import pyttsx3

engine = pyttsx3.init()


def listen():
    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.7
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(mic, 0.5)
            audio = sr.listen(source=mic)
            return sr.recognize_google(audio, language='ru-Ru').lower().strip()
    except speech_recognition.UnknownValueError:
        return NO_RECOGNIZE


def say(text):
    print(text)
    # engine.say(text)
    # engine.runAndWait()


if __name__ == '__main__':
    # print(listen())
    # say('мой разработчик крутой!')
    vs = engine.getProperty('voices')
    for v in vs:
        engine.setProperty('voice', v.id)
        say('привет')
        print(v.id)
        
