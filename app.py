# Starting of program
# Importing packages
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Change voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to output audio
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Introduction of Jarvis
def intro():
    introduction = "Hello, I am Jarvis. What can I do for you?"
    talk(introduction)

intro()

# Function to take command from user
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
            return command
    except Exception as e:
        print("Error: " + str(e))
        return ""

# Processing the command (main program)
def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I did not get that.')
    elif 'are you single' in command:
        talk('I am in a relationship with WiFi, haha')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'who created you' in command:
        talk('Mr. Susan Aryal created me using Python.')
    elif 'eat' in command:
        talk('Think again, you can’t do that, haha')
    else:
        talk('Please say the command again. may be')

# Run Jarvis
run_jarvis()

# End of the program
