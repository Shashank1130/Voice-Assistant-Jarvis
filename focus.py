import time
import datetime
import ctypes
import pyttsx3
import sys
import speech_recognition as sr
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate' , 190)


def speak(audio):
    engine.say(audio)    
    engine.runAndWait()

# We will block the websites here

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if is_admin:
    current_time = datetime.datetime.now().strftime("%H:%M")
    stop_time = input("Enter time, ef-[10:10]: ")
    a = current_time.replace(":",".")
    a = float(a)
    b = stop_time.replace(":",".")
    b = float(b)
    Focus_Time = b-a
    Focus_Time = round(Focus_Time,3)
    host_path = "C:\Windows\System32\drivers\etc\hosts"
    redirect = '127.0.0.1'

    print(f"Current time: {current_time}")
    time.sleep(2)
    website_list = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]

    if(current_time<stop_time):
        with open(host_path ,"r+") as file:
            content = file.read()
            time.sleep(2)
            for web in website_list:
                if web in content:
                    pass
                else:
                    file.write(f"{redirect} {web}")
                    print("Done")
            print("Websites are blocked , you can focus on your work now!")
            speak("Websites are blocked , you can focus on your work now!")
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        website_list = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]

        if (current_time >= stop_time):
            with open(host_path,"r+") as file:
                content = file.readlines()
                file.seek(0)

                for line in content:
                    if not any(web in line for web in website_list):
                        file.write(line)
                
                file.truncate()
                print("🎊 🎊 Congrats for the completion of the task 🎊 🎊 ")
                print("Websites are unblocked")
                speak("Congrats for the completion of the task,Websites are unblocked")
                file = open("focus.txt","a")
                file.write(f",{Focus_Time}")  
                #Write a 0 in focus.txt before starting
                file.close()
                break


else:
    ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable," ".join(sys.argv), None, 1)
































