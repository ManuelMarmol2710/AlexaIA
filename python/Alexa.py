#Manuel Alejandro Marmol Barrios 29579399 

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
    
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
    
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', 'music1')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'quien es' in command:
        person = command.replace('quien es', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        elif 'tiempo' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('EL tiempo es ' + time)
        print(time)
    elif 'Chiste' in command:
        talk(pyjokes.get_joke())
    elif 'Hola' in command:
        talk('Hi!')
    elif 'como estas?' in command:
        talk('Bien super bien')
            elif 'Cual es tu color favorito?' in command:
        talk('Todos los colores!')
    elif 'Cuantos años tienes?' in command:
        talk('Poneme tu la edad xd')
    
    elif 'bye' in command:
        quit
    else:
        talk('Repetir comando.')
        

while True:
    run_alexa()

 