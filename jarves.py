from math import e
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

from wikipedia import exceptions

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("good morning")
        elif hour>=12 and hour<18:
                speak("good afternoon")
        else:
            speak("good evening")

        speak("Hello. please tell me how can i help you")    
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognize")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
      #  print(e)

        print("say this again please")
        return "None" 
    return query    
def sendEmail(to ,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('alishaswain647@gmail.com', 'Abhi@123')
    server.sendmail('alishaswain647@gmail.com', to ,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
     query = takeCommand().lower()
    # logic for executing task based on query
     if 'wikipedia' in query:
         speak('searching wikipedia......')
         query = query.replace("wikipedia", "")
         result = wikipedia.summary(query, sentences=2)
         speak("according to wikipedia")
         print(result)
         speak(result)
     elif 'open youtube' in query:
        webbrowser.open("youtube.com")
     elif 'open google' in query:
         webbrowser.open("google.com")
     elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")
     elif 'play music' in query:
         msic_dir = 'D:\\song'
         songs = os.listdir(msic_dir)
         print(songs)
         os.startfile(os.path.join(msic_dir ,songs[0]))
     elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir, The time is {strTime}")
     elif 'open vs code' in query:
          codePath = "C:\\Users\\91859\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codePath)
     elif 'email to ashutosh' in query:
           try:
               speak("what should say?")
               conent = takeCommand()
               to = "malla2ashutosh@gmail.com"
               sendEmail(to, conent)
               speak("Email has been sent!")
           except Exception as e:
                print(e)
                speak("sorry, i am not able to send my email")
                    
