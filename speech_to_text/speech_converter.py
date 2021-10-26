import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
harvard = sr.AudioFile('audio_files/audio_files_harvard.wav')

while True:
    try:
        with harvard as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Speech: {text}")

        # with sr.Microphone() as mic:
        #     recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        #     audio = recognizer.listen(mic)

        #     text = recognizer.recognize_google(audio)
        #     text = text.lower()

        #     print(f"Speech: {text}")

    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
