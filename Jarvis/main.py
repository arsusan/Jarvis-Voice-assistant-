# starting of progarm
# Importing packages
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
# changing voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#

# output the audio


def talk(text):

    engine.say(text)
    engine.runAndWait()


#

# introduction of jarvis
def intro():
    introduction = "Hello, I am Jarvis. What can i do for you? "
    talk(introduction)


intro()

# taking command from user


def take_command():

    try:
        with sr.Microphone() as source:

            print("listening..............")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


# Processing the command (main program)

def run_alexa():

    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I did not exit.')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi, haha')
    elif 'joke' in command:
        jokes = pyjokes.get_joke()
        print(jokes)
        talk(jokes)
    elif 'who create you' in command:
        talk('Mr Susan Aryal, create me using Python ')
    elif 'fuck' in command:
        talk('Think again, You cant do that, haha')
    else:
        talk('Please say the command again.')


run_alexa()  # calling run function

# end of the program
