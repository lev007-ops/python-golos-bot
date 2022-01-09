import speech_recognition


def listen():
    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 1
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(mic, 0.5)
            audio = sr.listen(source=mic)
            return sr.recognize_google(audio, language='ru-Ru').lower().strip()
    except speech_recognition.UnknownValueError:
        return 'Не понял что вы сказали'


if __name__ == '__main__':
    print(listen())
