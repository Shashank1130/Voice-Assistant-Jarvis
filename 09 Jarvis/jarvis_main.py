import cmd
import queue
import os
import random
from socket import timeout
from turtle import back
# from signal import alarm
import requests
import pyautogui
'''
    # PyAutoGUI is a Python module which can automate your GUI and programmatically control your keyboard and mouse.
'''
import random
from bs4 import BeautifulSoup
from urllib.parse import SplitResult
import pyttsx3
'''
    # "pyttsx3" is a txt-to-speech conversion library in Python, and it works offline
'''
import speech_recognition as sr
import wikipedia
'''
    # This module is used to recognize the audio of the user.
'''
import datetime
import webbrowser
'''
    # We can open browsers with this module
'''
import smtplib
import lxml
from plyer import notification
'''
    # This module will be used to give notification on the desktop screen
'''
from pygame import mixer
'''
    # Mixer is used to play song , like a dj
'''
import speedtest



engine = pyttsx3.init('sapi5')
'''  
    # sapi5:- 
        # This is a windows API , which we will use to take or select the voice of the bot.

    # Engine instance:- It is s very easy to use tool whcih "converts the entered text into speech".
'''
voices = engine.getProperty('voices')
'''
    # in voices variable, we are taking all the voices present in the windows machine
'''
engine.setProperty('voice', voices[0].id)
'''

    # Here we are choosing a voice out of all voices present in the machine.
'''
engine.setProperty('rate' , 190)
'''
    # This will decide the speed of the pronouncing of jarvis
'''


# Creating Fucntions

# 1. Speak Function
def speak(audio):
    '''
        We will use this function for speaking and for waiting after speaking
    '''
    engine.say(audio)    # The engine will speak the audio
    engine.runAndWait()  
    '''
        # This means that, after speaking of the audio, it will wait for some time
    '''


# 3. Take Command
def take_command():
    '''
        # It takes microphone input from the user and returns string output.
    '''
    # Initialize the recognizer
    # This will help us to recognize the audio
    r = sr.Recognizer()

    # Use the microphone as source for input
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        '''
            # Seconds of non-speaking audio before a phrase is considered complete 

            # or

            # sun ne ke liye kitna wait karega 
        '''
        r.energy_threshold = 300

        # Listens for the user's input
        audio = r.listen(source, 0 ,5)
        '''
            # Here jarvis will wait for 4 seconds, and if the user will not say anything , it will move forward.
        '''

    try:
        print("Recognizing....")
        # Google will recognize the "audio" now
        query = r.recognize_google(audio , language = 'en-in')
        print(f"User said: {query}\n")
    
    except Exception as ex:        
        print("Say that again please...")
        return "None"
    return query

def alarm(query):
    timehere = open("alarm.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":


    while True:
        query = take_command().lower()
        
        # if "hey jarvis" in query:
        #     from greetMe import greet_me
        #     greet_me()
        if "hi jarvis" in query:
            from greetMe import greet_me
            greet_me()
        # elif "wake up jarvis" in query:
        #     from greetMe import greet_me
        #     greet_me()

            while True:
                query = take_command().lower()
                if "go to sleep" in query:
                    speak("Ok sir, you can call me anytime")
                    break
                
                #--------- conversations ---------
                elif "who are you" in query:
                    speak("i am jarvis sir")
                elif 'hello' in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query:
                    speak("That's awsome sir")
                elif 'how are you' in query:
                    speak("i am fine and healthy sir")
                elif "i am not fine" in query:
                    speak("Don't worry sir, i am her with you , you can tell me anything")
                elif "thank you" in query:
                    speak("you're welcome,sir")
                elif "where do you live" in query:
                    speak("My address is in cloud, but currently i am in Realme book laptop")



                
                #------- open and close apps and webapps -------
                elif "open a new tab" in query:
                    from Dictapp import opennewtabs
                    opennewtabs(query)
                elif "open 2 new tabs" in query:
                    from Dictapp import opennewtabs
                    opennewtabs(query)

                elif "open" in query:
                    from Dictapp import openwebapp
                    openwebapp(query)
                
                elif "close" in query:
                    from Dictapp import closewebapp
                    closewebapp(query)
                    
                
                
                

                

                #------ open any installed app  ------
                elif "launch" in query:
                    try:
                        query = query.replace('open' , '')
                        query = query.replace('jarvis' , '')
                        query = query.replace('launch' , '')
                        pyautogui.press('super')
                        pyautogui.typewrite(query)
                        pyautogui.sleep(1)
                        pyautogui.press("enter")
                    except:
                        speak("Sorry, can't open the application right now.")
                

                


                # -------- browsing --------
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
 
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                




                #------- automating the youtube controls ------
                elif "pause video" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play video" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute video" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    volumeup()
                elif "full volume" in query:
                    from keyboard import fullvolume
                    fullvolume()
                elif "volume down" in query:
                    from keyboard import volumedown
                    volumedown()
                
                elif "forward video" in query:
                    from keyboard import forward
                    forward()
                elif "backward video" in query:
                    from keyboard import backward
                    backward()



                #------- playing song from playlist -------
                elif "play a song from my favourite playlist" in query:
                    from playlist import playlist
                    playlist()
                elif "play song from my favourite playlist" in query:
                    from playlist import playlist
                    playlist()
                elif "play songs from my favourite playlist" in query:
                    from playlist import playlist
                    playlist()


                # ------- temperature & weather -------
                elif "temperature" in query:
                    search = "temperature in rewa"
                    url = f"https://www.google.com/search?q={search}"
                    req = requests.get(url)
                    data = BeautifulSoup(req.text , "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    print(f"Current {search} is {temp}")
                    speak(f"Current {search} is {temp}")
                
                elif "weather" in query:
                    search = "weather in rewa"
                    url = f"https://www.google.com/search?q={search}"
                    req = requests.get(url)
                    data = BeautifulSoup(req.text , "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"Current {search} is {temp}")


                #------- time and date ------
                elif "the time" in query:
                    time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Current time is: {time}")
                    speak(f"Current time is {time}")


                #------- NEWS -------
                elif "today's news" in query:
                    from news import todays_news
                    todays_news()
                elif "today's latest news" in query:
                    from news import todays_news
                    todays_news()
                elif "latest news" in query:
                    from news import todays_news
                    todays_news()


                #------- remember -------
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to"+rememberMessage)
                    remember = open("remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt")
                    speak("You told me to"+remember.read())
                    remember.close()
                    


                #------- shutdown -------
                elif "shutdown the system" in query:
                    speak("Are you sure tou want to shotdown your system")

                    shutdown = input("Press 'Y' for Yes, and 'N' for No: ").lower()

                    if shutdown == "y":
                        speak("shutting down the system , have a nice day sir")
                        os.system("shutdown /s /t 1")
                    elif shutdown == "n":
                        break

                elif "shutdown my system" in query:
                    speak("Are you sure tou want to shotdown your system")

                    shutdown = input("Press 'Y' for Yes, and 'N' for No: ").lower()
                    if shutdown == "y":
                        speak("shutting down the system , have a nice day sir")
                        os.system("shutdown /s /t 1")
                    elif shutdown == "n":
                        break


                    

                #------ scheduling the day -------
                elif "schedule my day" in query:
                    tasks = []
                    speak("Do you want to clear old texts (Please speak yes or no)")
                    query = take_command().lower()

                    if 'yes' in query:
                        file = open('tasks.txt','w')
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the number of tasks: "))

                        for i in range(no_tasks):
                            tasks.append(input(f"Enter the task : "))
                            file = open("tasks.txt",'a')
                            file.write(f"{i}.  {tasks[i]}\n")
                            file.close()
                        
                    elif 'no' in query:
                        i=0
                        no_tasks = (input("Enter the number of tasks: "))

                        for i in range(no_tasks):
                            tasks.append(input(f"Enter the task {i}: "))
                            file = open("tasks.txt",'a')
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    
                elif "show my schedule" in query:
                    speak("here is your schedule for the day sir")
                    file = open('tasks.txt')
                    content = file.read()
                    file.close()
                    mixer.init() # This will initialize the 'mixer' function
                    mixer.music.load("Notification.mp3") # This will load the notification sound
                    mixer.music.play() # This will play the notification sound


                    notification.notify(
                    title = 'My schedule:',
                    message = content,
                    timeout = 20)



                #------ internet speed -------
                elif "internet speed" in query:
                    check = speedtest.Speedtest()
                    upload_speed= check.upload()/1048576   # We had divide the upload speed by 1048576 number , becoz by default it will tell the speed in bytes but after dividing that number it will show the speed in mb
                    # 1mb = 1024*1024 bytes
                    down_speed = check.download()/1048576
                    print(f"Upload speed is: {round(upload_speed , 4)}mb/sec")
                    print(f"Download speed is: {round(down_speed , 4)}mb/sec")
                    speak(f"current upload speed is: {round(upload_speed , 4)} megabytes per second")
                    speak(f"Current download speed is: {round(down_speed , 4)} megabytes per second")



                #------- game play ------
                elif "play rock paper scissor" in query:
                    from game import start_game
                    start_game()
                elif "play a game" in query:
                    from game import start_game
                    start_game()
                elif "play game" in query:
                    from game import start_game
                    start_game()


                #----- ss and  photo ------
                elif "take screenshot" in query:
                    image = pyautogui.screenshot()
                    image.save("ss.png")
                    speak("Screenshot captured and save, sir")
                elif "take ss" in query:
                    image = pyautogui.screenshot()
                    image.save("ss.png")
                    speak("Screenshot captured and save, sir")
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(3)
                    speak("smile")
                    pyautogui.press("enter")
                    speak("photo captured")



                #------- focus mode -------

                elif "turn on the focus mode" in query:
                    # speak("Are you sure you want to turn on the focus mode? (yes or no)")
                    # print("Please speak: 'Yes' or 'No'\n")

                    # query = take_command().lower()

                    # if query=='yes':
                    #     speak("Entering on the focus mode")
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\shash\\OneDrive\\Desktop\\Python Projects\\09 Jarvis\\focus.py")
                    elif query=='no':
                        speak("ok sir")


                #------- for exiting -------
                elif "finally sleep" in query:
                    speak("Bye bye , have a nice day, sir")
                    exit()
                

       








































