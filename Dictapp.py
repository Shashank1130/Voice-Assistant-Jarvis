from turtle import speed
import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
from time import sleep
import webbrowser
import os
import pyautogui
"""
    # Use can press any keyboard button using this module means if we want to close tabs in chrome, we can jsut use this module to let press the keys without letting us to press the keys.
"""



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate' , 190)


def speak(audio):
    engine.say(audio)    
    engine.runAndWait()  
    

dictapp= {"commandprompt":"cmd","word":"winword","excel":"excel","paint":"paint","powerpint":"powerpoint" , "vscode":"code","chrome":"chrome", "whatsapp":"whatsapp","notepad":"notepad", "clock":"clock","brave":"brave"}


def openwebapp(query):
    speak("Launching...")

    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("launch","")
        query = query.replace("jarvis","")
        query = query.replace("space","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    
    else:
        keys = list(dictapp.keys())

        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")




def closewebapp(query):
    speak("Closing..")

    try:

        if "close one tab" in query:
            pyautogui.hotkey("ctrl","w") # Hotkey will press the "ctrl" and "w" for us
            speak("1 tabs closed")

        elif "close 2 tabs" in query:
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("2 tabs are closed")

        elif "close 3 tabs" in query:
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("3 tabs are closed")

        elif "close 4 tabs" in query:
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("4 tabs are closed")

        elif "close 5 tabs" in query:
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("5 tabs are closed")
            
        elif "close all tabs" in query:
            pyautogui.hotkey("Alt","F4")
            speak("All tabs are closed.")
            
        # For applications inside the device
        else:
            keys = list(dictapp.keys())

            for app in keys:
                if app in query:
                    os.system(f"taskkill /f /im {dictapp[app]}.exe")
    except:
        speak("Sorry, can not open it right now ,  you can say again")
        
    
                

def opennewtabs(query):

    if "open a new tab" in query:
        pyautogui.hotkey("ctrl","t")
        speak("Done ,sir")
    elif "open 2 new tabs" in query:
        pyautogui.hotkey("ctrl","t")
        pyautogui.hotkey("ctrl","t")
        speak("Done ,sir")
















