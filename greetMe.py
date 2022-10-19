import pyttsx3
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate' , 190)


def speak(audio):
    engine.say(audio)    # The engine will speak the audio
    engine.runAndWait()  


def greet_me():
    '''
        # The bot will greet the user with this function.
    '''
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<8:
        print("😊😊 A very good morning 😊😊!\n")
        speak("A very good morning sir")
    elif hour>=8 and hour<12:
        print("😊😊 Good Morning 😊😊!\n")
        speak("Good Morning sir")
    elif hour>=12 and hour<16:
        print("😊😊 Good Afternoon! 😊😊\n")
        speak("Good Afternoon sir!")
    else:
        print("😊😊 Good Evening 😊😊!\n")
        speak("Good Evening!")
    speak("Please tell me, how can I help you?\n")