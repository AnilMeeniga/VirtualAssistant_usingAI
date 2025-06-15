import pyttsx3 as p
import speech_recognition as sr
from seleniumweb import inflow
from youtube import music
import threading
from Newsapi import *
#import pyaudio as audio
engine=p.init()
rate=engine.getProperty('rate')
rate=engine.setProperty('rate',170)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text):
   engine.say(text)
   engine.runAndWait()  

r=sr.Recognizer()
speak("hello sir ,i am your voice assistant,how are you ")

with sr.Microphone() as source:
    r.energy_threshold=100000
    r.adjust_for_ambient_noise(source,1.2)
    print("listenining....")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what"and "about"and "you" in text:
    speak("Thank you for asking me sir,i am fine how can i help you sir ")
with sr.Microphone() as source:
    r.energy_threshold=100000
    r.adjust_for_ambient_noise(source,1.2)
    print("listenining....")
    audio=r.listen(source)
    text2=r.recognize_google(audio)
if "information" in text2:
    speak("you need information about which topic")
    with sr.Microphone() as source:
      r.energy_threshold=100000
      r.adjust_for_ambient_noise(source,1.2)
      print("listenining....")
      audio=r.listen(source)
      infor=r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))

    assist=inflow()
    summa=assist.get_info(infor)
    if summa:
        speak("Here is a summary of {}:".format(infor))
        print_thread=threading.Thread(target=print,args=(summa,))
        speak_thread=threading.Thread(target=speak,args=(summa,))
        print_thread.start()
        speak_thread.start()
        print_thread.join()
        speak_thread.join()
        #speak(summa)
    else:
        speak("i could not find information on that topic.")   
if"paly" in text2 or "video" in text2 or "song" in text2:
        speak("searching for in youtube"+text2)
        assist=music()
        assist.play(text2)
elif "news" or "article" or "articles" in text2:
    arr=news()
    for item in arr:
        speak("Here is the latest news {}:".format(item))
        print(item)