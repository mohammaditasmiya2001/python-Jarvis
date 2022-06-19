

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import wolframalpha
import requests
from  requests import get
from bs4 import BeautifulSoup
from twilio.rest import Client
import pywhatkit as kit
import smtplib
import getpass

import json
import requests
import subprocess
from sys import platform
import random
import pyjokes



appid="2GVJK5-X9GEAPP933"
client=wolframalpha.Client(appid)




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('vvoice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
        print("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
        print("good afternoon")
    else:
        speak("goood evening")
        print("good evening")


    speak("iam jarvis maam please tell me how may i help u")            
    print("iam jarvis maam please tell me how may i help u")            



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language='en-in') 
        print(f"user said:{query}\n")  

    except Exception as e:
        print(e)
        print("say that again please")
        return "None" 
    return query




def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])
        speak(pyjokes.get_jokes()[i])




if __name__=="__main__":
    wishMe()
    while True:

        query=takeCommand().lower()
        if "wikipedia" in query:
            print("what should i want to search maam")
            speak("what should i want to search maam")
            ans=takeCommand()
            #speak("searching wikipedia")
            #query=query.replace("wikipedia","")
            try:          
                results=wikipedia.summary(ans,sentences=1)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                try:
                    res=Client.query(ans)
                    speak("according to wolframalpha,")
                    print(next(res.result).text)
                except Exception as e:
                    speak("sorry maam there are no results found")
                    speak(ans)  
        
        elif "write a note" in query:
            speak("What should i write, maam")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("maam, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:% M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
 

                        

        elif "open youtube"  in query:
        
            webbrowser.open("youtube.com")

        elif "open google"  in query:
            speak("what would you like to search")
            webbrowser.open("google.com")

       
        
        elif "open stackoverflow"  in query:
            webbrowser.open("stackoverflow.com") 

        elif "play music" in query:
            music_dir="F:\\music"  
            songs=os.listdir(music_dir) 
            print(songs)   
            os.startfile(os.path.join(music_dir,songs[0]))

        
        elif "the time" in query:
            
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"maam ,the time is {strTime}")        

        elif "open code"  in query:
            codePath="C:\\Users\\win10\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open sublime3"  in query:
            codePath="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)


       

        elif "github" in query:
            webbrowser.open_new_tab(
               "https://github.com/mohammaditasmiya2001")  
           
        
               
        elif "temperature" in query:
            speak("which place temperature maam")
            ans=takeCommand()
            search="temperature in state"  
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            print(f"current{search} is {temp}")
            speak(f"current{search} is {temp}")
    

        elif "send message" in query:   
            kit.sendwhatmsg("+918747058025","hllo samra",22,25) 
            print("Successfull message diliverd")

        elif "play song on youtube" in query:
            speak("which song you want to play maam")
            ans=takeCommand()
            kit.playonyt(ans)

        elif "stands for" in query:
            speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')    

        elif "jarvis are you there" in query:
            speak("yes,maam at your servis")

        elif "voice" in query:
            if "female" in query:
                engine.setProperty("voice",voices[0].id)
            else:
                engine.setProperty("voice",voices[1].id)   
            speak("hello maam,I have switches my voice how is it?")     

        elif "jarvis who made you" in query:
            speak("yes maam, my master buld in Ai")


        elif "your name" in query:
            speak("my name is jarvis maam")

        elif "how are you" in query:
            speak("I am fine,thank you")
            speak("how are you , maaam")


        #elif  "fine" in query or "good" in query:
            #speak("Is's good to know that your fine")

        elif "not fine" in query:
            speak("what happen maam")
            ans=takeCommand()
            speak("take care maam, god bless u")



        elif "change my name" in query:
            query=query.replace("change my name to","")
            assname=query
            
        elif "change name" in query:
            speak("what would you like to call me ,maam")
            assname=takeCommand()
            speak("Thanks for naming me") 

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.open_new_tab(
                url)
            speak('Here is What I found for' + search)      


        elif "joke" in query:
            joke()

        elif "what's your name" in query or "what is your name" in query:
            speak("my friend call me")
            speak(assname)
            speak("my friend call me",assname)

        elif "who are you" in query:
            speak("I am your assistant maam")     

        elif "location" in query:
            speak("what is the location maam")
            location=takeCommand()
            url="https://google.nl/maps/place/" + location + "/&amp;"
            webbrowser.open_new_tab(url)
            speak("here is location" +location)

        elif "your master" in query:
            if platform=="win32" or "darwin":
                speak("tasmiya is my master ,he created me couple of days ago")
                print("tasmiya is my master ,he created me couple of days ago")

            elif platform =="linux" or platform =="linux":
                name=getpass.getuser()
                speak(name,"is my master , he is running me right now") 
                print(name,"is my master , he is running me right now")       
        

        elif "quit" in query:
            speak("maam you really want to quit")
            exit()
        
        elif "shutdown" in query:
            speak("you really want to shutdown maam")
            if "yes" in ans:
                speak("ok,maam thank you for your giving  time")
                subprocess.call('shutdown / p /f')
                exit()

