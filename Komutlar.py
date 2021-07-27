import time
import pywhatkit  # send messages and etc.
from gtts import gTTS    #(googleTextToSpeech - text->sound and save with .mp3 doc )
from playsound import playsound
import bs4
import os
import sys
import vlc   #muzik
from random import choice
import requests
import smtplib
from datetime import datetime
import pyttsx3    #Speak
from lxml import html
import webbrowser
from selenium import webdriver  #Web surfing(limited)
from pytube import YouTube  # download video
import subprocess
import psutil  # system monitoring, profiling, limiting process resources and the management of running processes
from plyer import notification
from notifypy import Notify
from flask import Flask, jsonify, request, render_template # develop web applications, like url...
import speech_recognition as sr2 #Sound->text
r2 = sr2.Recognizer()  #Try to understand sound
# create object
engine = pyttsx3.init()
# assign voice
voices = engine.getProperty('voices')
# changing index changes voices but only 0 and 1 are working here
engine.setProperty('voice', voices[1].id)
# run tool
engine.runAndWait()
print("")

class Komut():
    def __init__(self, gelenSes):
        self.ses = gelenSes.upper()
        self.sesBloklari = self.ses.split()
        self.komutlar = ["AÇ","YENIDEN","TAMAM", "ZAMAN","BATARYA","PIL", "MÜZIK", "MERHABA", "NASILSIN", "KAPAT",
                         "HAVA", "SAAT", "OYNAT", "ARA","NASIL GİDİYOR","NE HABER","SELAM"
                         "SEN","POWERPOINT","POINT","EXCEL","GOOGLE CHROME","INTERNET","GOOGLE","CHROME",
                         "MICROSOFT EDGE","NOTEPAD","NOT DEFTERİ","NOT","YAZI", "MESAJ",
                         "GÜNLERDEN","TARIH","SPAS","EYVALLAH","TESEKKÜRLER", "MAIL"
                         "YAPILDIN","YAŞ","YARATILDIN","KODLADI", "ADIN", "AD","ÇAL"]

    #KOMUT VE İSLEMLERİ

    def seslendirme(self, yazi):
        self.yazi=yazi
        tts = gTTS(text=yazi, lang='tr')
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")
    def aramayap(self):
        with sr2.Microphone() as src:
          self.seslendirme("Ne aratayım")
          audio = r2.listen(src)
          data = r2.recognize_google(audio, language='tr-tr')
          print(data)
          self.seslendirme(data+" arıyorum")
          webbrowser.open("https://www.google.com/search?q=" +"".join(data))
    def muzikac(self):
        with sr2.Microphone() as src:
            self.seslendirme("Ne dinlersin?")
            audio = r2.listen(src)
            data = r2.recognize_google(audio, language='tr-tr')
            print(data)
            self.seslendirme(data + " açıyorum")
            webbrowser.open('https://www.youtube.com/results?search_query=' + data)
    def mediaPlayer(self):
        listem = ["C:\\Users\\yarim\\Music\\passenger_let_her_go_official_video_mp3_37807.mp3","C:\\Users\\yarim\\Music\\ed_sheeran_give_me_love_lyrics_mp3_33039.mp3"]
        for sarki in listem:
            player = vlc.MediaPlayer(sarki)
            player.play()
            time.sleep(10)
            player.stop()
    def saat(self):
        self.saatim = datetime.now().strftime("%H:%M:%S")
        self.seslendirme("saat"+self.saatim)
    def internet(self):
        self.seslendirme("Açılıyor")
        webbrowser.open("https://www.google.com")
        exit()
    def kapatApp(self):
        self.seslendirme("Kapatıyorum")
        sys.exit()
    def uygulamaac(self):
        while True:
           with sr2.Microphone() as src:
                self.seslendirme("Ne açayım?")
                audio = r2.listen(src)
                data = r2.recognize_google(audio, language='tr-tr')
                if data == "NOTEPAD" or "NOT DEFTERI" or "NOT" or "YAZI":
                        self.seslendirme(data + " açılıyor...")
                        os.system("Notepad")
                        exit()
                elif data == "SEN" or "MICROSOFT WORD":
                        os.system("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk")
                        exit()
                elif data == "POWER POİNT" or "POİNT" or "MİCROSOFT POWER POİNT":
                        subprocess.Popen(["C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"])
                        exit()
                elif data == "EXCEL" or "MİCROSOFT EXCEL":
                        subprocess.Popen(["C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"])
                        exit()
                elif data == "TAMAM":
                    exit()
    def tarih(self):
        tarih=datetime.now()
        yil=str(tarih.year)
        ay=str(tarih.month)
        gun=str(tarih.day)
        self.seslendirme(gun+"-"+ay+"-"+yil)
    def mesajGonder(self):
        with sr2.Microphone() as src:
            self.seslendirme("Numara nedir?")
            audio1 = r2.listen(src)
            numara = r2.recognize_google(audio1, language='tr-tr')

            self.seslendirme("Ne yazayım?")
            audio2 = r2.listen(src)
            mesaj = r2.recognize_google(audio2, language='tr-tr')
            print(mesaj)

            # self.seslendirme("Mesajın ne zaman gönderilsin? Saati söyler misin?")
            # audio3 = r2.listen(src)
            # saat = r2.recognize_google(audio3, language='tr-tr')
            # print(tarih)
            #
            # self.seslendirme("Dakika?")
            # audio3 = r2.listen(src)
            # dk = r2.recognize_google(audio3, language='tr-tr')
            # print(tarih)
            self.seslendirme("Bekleyin")
            pywhatkit.sendwhatmsg(numara,mesaj,15,35)
            #pywhatkit.send_mail("yarimdunyahazal.31@gmail.com","hazalyarimdunya.49@gmail.com",content)

    def mailGonder(self):
        with sr2.Microphone() as src:
            self.seslendirme("Ne yazayım?")
            audio1 = r2.listen(src)
            icerik = r2.recognize_google(audio1, language='tr-tr')
            print(icerik)
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("deneme@gmail.com", "şifre")
            self.seslendirme("Bekleyin")
            pywhatkit.sen("deneme@gmail.com","deneme@gmail.com",icerik)
    def havadurumu(self):
        with sr2.Microphone() as src:
            self.seslendirme("Hangi şehir?")
            audio1 = r2.listen(src)
            sehir = r2.recognize_google(audio1, language='tr-tr')
            print(sehir)
        webbrowser.open("https://www.google.com/search?q={}+hava+durumu&source=hp&ei=lhW9YLyMLsv7kwWqzLKYCg&iflsig=AINFCbYAAAAAYL0jpkGcu6jkMtx2vqfEGNMgd2QX8mAs&oq=bulan%C4%B1k+hava&gs_lcp=Cgdnd3Mtd2l6EAMYADIICAAQsQMQgwEyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6CAguELEDEJMCOgsIABCxAxDHARCjAjoFCAAQsQM6AgguOgsILhCxAxCDARCTAjoFCC4QsQM6CAguELEDEIMBOggIABDHARCvAVDpAljEE2CEImgAcAB4AIABpQOIAdwYkgEJMC4yLjQuNC4xmAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz".format(sehir))
    def sohbet(self):
        sozler = ["İyiyim", "İyiyim sen?","İyi gidiyor sen?","teşekkür ederim iyiyim"]
        secim = choice(sozler)
        self.seslendirme(secim)
    def yas(self):
        tarih=datetime.now()
        yil=tarih.year
        age=yil-2021
        self.seslendirme(str(age)+"yaşındayım")
    def selamlama(self):
        selam=["Merhaba", "Selam"]
        secim=choice(selam)
        self.seslendirme(secim)
    def tanısma(self):
        ad="Hazistan"
        self.seslendirme("Benim adım "+ad)
        print(ad)
        self.seslendirme("Senin adın ne?")

        with sr2.Microphone() as src:
            audio = r2.listen(src)
            data = r2.recognize_google(audio, language='tr-tr')
            print(data)
            self.seslendirme("Memnun oldum "+data)
    def uretim(self):
        self.seslendirme("Hazal Yarımdünya")
    def baskaIstek(self):
        with sr2.Microphone() as src:
            self.seslendirme("Başka birşey istiyor musunuz?")
            audio1 = r2.listen(src)
            data1 = r2.recognize_google(audio1, language='tr-tr')
            if data1=="Evet":
               self.seslendirme("Dinliyorum...")
               audio2 = r2.listen(src)
               data2 = r2.recognize_google(audio2, language='tr-tr')
               print(data2)
               Komut(data2)
            elif data1=="Hayır":
                self.seslendirme("Peki, görüşürüz...")
                exit()
    def pilSeviyesi(self):
        pil = psutil.sensors_battery()
        yuzde = pil.percent
        notification.notify(title="Pil yüzdesi", message=str(yuzde) + "% Kalan pil", timeout=10)
    def bilgKapat(self):
        with sr2.Microphone() as src:
            self.seslendirme("Emin misiniz?")
            audio = r2.listen(src)
            data = r2.recognize_google(audio, language='tr-tr')
            if data=="Evet" or data=="Eminim":
               self.seslendirme("yeniden başlatılıyor...")
               os.system("shutdown /r /t 2")
            else:
                self.seslendirme("Peki o zaman")
                exit()

    def komutBul(self):
        for komut in self.komutlar:
            if komut in self.sesBloklari:
                self.komutCalistir(komut)

    def komutCalistir(self, komut):
        if komut == "MERHABA" or komut == "SELAM":
            self.selamlama()
        if komut == "NASILSIN":
            self.sohbet()
        if komut == "SPAS" or komut == "EYVALLAH" or komut == "TESEKKÜRLER":
            self.baskaIstek()
        if komut == "KAPAT" or komut == "TAMAM":
            self.kapatApp()
        if komut == "HAVA":
            self.havadurumu()
        if komut == "SAAT":
            self.saat()
        if komut == "OYNAT":
            self.playyoutube()
        if komut == "ARA":
            self.aramayap()
        if komut == "URETILDIN" or komut=="YAPILDIN" or komut=="YARATILDIN" or komut=="KODLADI":
            self.uretim()
        if komut == "AÇ":
            self.uygulamaac()
        if komut == "INTERNET" or komut=="GOOGLE CHROME" or komut=="GOOGLE" or komut=="CHROME":
            self.internet()
        if komut == "ADIN" or komut=="AD":
            self.tanısma()
        if komut == "MÜZIK":
            self.muzikac()
        if komut == "BATARYA" or komut=="PIL":
            self.pilSeviyesi()
        if komut == "MESAJ":
            self.mesajGonder()
        if komut == "MAIL":
            self.mailGonder()
        if komut == "YENIDEN":
            self.bilgKapat()
        if komut == "YAŞ":
            self.yas()
        if komut == "ÇAL":
            self.mediaPlayer()
        if komut == "TARIH" or komut=="GÜNLERDEN":
            self.tarih()
