import pyttsx3
import speech_recognition as sr
import random



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



def is_win(player, opponent):

    if (player=='rock' and opponent=='scissor') or (player=='paper' and opponent=='rock') or (player=='scissor' and player=='paper'):
        return True


def play():
    # user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors: \n")
    # computer = random.choice(['r','p','s'])

    # if user == computer:
    #     return "It's a tie!"
    
    # if is_win(user , computer):
    #     return "You won!"
    
    # return "You lost"


    # user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors: \n")
    computer = random.choice(['rock','paper','scissor'])
    
    speak("What is your choice?, rock, paper, scissor")
    query = take_command().lower()
    speak(f"I choose: {computer}")
    print(f"I choosed: {computer}")

    if query == computer:
        return "It's a tie!"
    
    if is_win(query , computer):
        print("You won!")
        return speak("You won!")
    
    return print("You lost"),speak("You lost")
    
def is_win(player, opponent):

    if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') or (player=='s' and player=='p'):
        return True


# replay
def replay():
    query = ''
    x = ''

    while query not in ['yes','no']:
        speak("Want to play again?, yes or no")
        print("Yes or No?")
        query = take_command().lower()
    
        if query =='yes':
            return x==True
        elif query == 'no':
            return x == False
    return x

# starting the game
def start_game():

    speak("Welcome to the rock,paper,scissor")
    print("\n***Welcome to the rock🗿, paper📄, scissor✂️***\n")
    print("Let's play the game")
    speak("Let's play the game")

    game_on = True

    while game_on==True:
        print(play())
        game_on = replay()

























