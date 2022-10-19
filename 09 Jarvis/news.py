import pstats
import requests
import json
import pyttsx3
import speech_recognition as sr


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
    


def todays_news():
    apidict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=e5eeda4cd17f4560823d150052daf4cb" , 
    "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=e5eeda4cd17f4560823d150052daf4cb" , 
    "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=e5eeda4cd17f4560823d150052daf4cb" ,
    "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=e5eeda4cd17f4560823d150052daf4cb" , 
    "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=e5eeda4cd17f4560823d150052daf4cb", 
    "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=e5eeda4cd17f4560823d150052daf4cb"}

    content = None
    url = None

    speak("Which field news do you want sir, [business], [entertainment], [sports], [science], [technology], [health]")
    print("Select of of the news field:-")
    print("1.Business\n2.Entertainment\n3.Sports\n4.Science\n5.Technology\n6.Health\n")

    field = input("Type field news that you want: ")
    # query = take_command().lower()

    for key , value in apidict.items():
        if key.lower() in field.lower():
            url=value
            print(url)
            print("url was found\n")
            break
        else:
            url = True
    if url is True:
        print("url not found\n")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news:\n")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"\nfor more info visit:  {news_url}\n")

        a = input("Press 1 to continue and Press 2 to stop: ")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

    speak("that's all")




















