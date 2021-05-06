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
            return command

    except:
        pass


def run_alexa():
    command = take_command()
    command = command.lower()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M &p')
        talk('Current time is '+time)

    elif 'who is' in command:
        person = command.replace('Who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)

    elif 'what is' in command:
        thing = command.replace('What is', '')
        info = wikipedia.summary(thing, 1)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'goodbye' in command:
        talk('Goodbye')
        return 1
    else:
        talk("Please say the command again")


while True:
    x = run_alexa()
    if x == 1:
        break
