import webbrowser
import random
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate' , 190)


def speak(audio):
    engine.say(audio)    
    engine.runAndWait()  
    

def playlist():
    speak("Playing a song from your favourite playlist")
    a = (1,2,3,4,5)
    b = random.choice(a)

    if b==1:
        webbrowser.open("https://www.youtube.com/watch?v=AETFvQonfV8")
    elif b==2:
        webbrowser.open("https://www.youtube.com/watch?v=DGBNAkqGx3w&list=PL-RhuCMcZpudFSK2gPnIDsf5WYgzGY4rT&index=37")
    elif b==3:
        webbrowser.open("https://www.youtube.com/watch?v=Az-mGR-CehY")
    elif b==4:
        webbrowser.open("https://www.youtube.com/watch?v=x-B_f2Swlyk&list=PL-RhuCMcZpudFSK2gPnIDsf5WYgzGY4rT&index=6")
    elif b==5:
        webbrowser.open("https://www.youtube.com/watch?v=MxGItnRhsBI&list=PL-RhuCMcZpudFSK2gPnIDsf5WYgzGY4rT&index=36")