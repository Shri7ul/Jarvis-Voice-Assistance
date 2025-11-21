import speech_recognition as sr
import pyttsx3
import datetime
import logging
import os
import webbrowser
import wikipedia
import random
import subprocess

# Configure logging
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


#Activate the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Select the first voice

# Function to make the assistant speak
def speak(text):
    """This function makes the assistant speak the given text.
    
    Args:
         text
    returns:
         voice
    """
    engine.say(text)
    engine.runAndWait()


# speak("Hello, I am your assistant. How can I help you today?")

def takeCommand():
    """This function listens for user input and converts it to text.
    
    Args:
         None
    returns:
         str: The recognized text from the user's speech.
         """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        logging.info(e)
        print("Say that again please...")
        return "None"   
    
    return query

def greeting():
    """This function greets the user based on the time of day.
    
    Args:
         None
    returns:
         None
    """
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am your assistant. Please tell me how may I help you")

greeting()

while True:
    query = takeCommand().lower()
    print(query)
    if "your name" in query:
        speak("I am your assistant.")
        logging.info("User asked for assistant's name.")

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"The time is {strTime}")
        logging.info("User asked for current time.")

    elif "exit" in query or "quit" in query:
        speak("Goodbye!")
        break
    elif "how are you" in query:
        speak("I am fine, thank you. How can I assist you today?")
        logging.info("User asked how the assistant is doing.")

    elif "whom created you" in query or "who made you" in query:
        speak("I was created by InHuman.")
        logging.info("User asked about the assistant's creator.")

    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
        logging.info("User requested to open Google.")


speak("Hello, I am your assistant. How can I help you today?")

