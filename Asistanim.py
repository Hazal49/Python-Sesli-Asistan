import speech_recognition as sr
import time
from Komutlar import Komut
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Nasıl yardımcı olabilirim?")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio, language='tr-tr')
        print(data)
        komut = Komut(data)
        komut.komutBul()
        time.sleep(1)
    except sr.UnknownValueError:
        print("Anlamadım.Tekrar eder misin")
