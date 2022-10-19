from email.mime import audio
import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import webbrowser



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate' , 190)


def speak(audio):
    engine.say(audio)    
    engine.runAndWait()  
    

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source , 0 , 5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, lanaguage='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again...")
        return "None"
    return query


query = take_command().lower()


# Search google
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query= query.replace("jarvis","")
        query= query.replace("google","")      
        query= query.replace("google search","")
        speak("This is what i found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query , 1)
            print(result)
            speak(result)
        except:
            speak("I didn't found any relatable information, you can seach again")


# Wikipedia search
def searchWikipedia(query):
    if "wikipedia" in query:
        print("Searching...")
        speak("Searching")
        query= query.replace("jarvis","")
        query= query.replace("wikipedia","")
        query= query.replace("wikipedia search","")
        query= query.replace("search wikipedia","")
        query= query.replace("search","")

        try:
            result = wikipedia.summary(query ,sentences=1 )
            speak("According to wikipedia..")
            print(result)
            speak(result)
        except:
            speak("No relatable results found")

# Youtube search
def searchYoutube(query):
    if "youtube" in query:
        query= query.replace("jarvis","")
        query= query.replace("youtube","")
        query= query.replace("search","")
        query= query.replace("youtube search","")

        try:
            web = "https://www.youtube.com/"+query
            webbrowser.open(web)
            # pywhatkit.playonyt(query)
            speak("Done,  sir")
        except:
            speak("Sorry, not able to open youtube at this moment")



















