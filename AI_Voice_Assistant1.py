import speech_recognition as sr
import pyttsx3
import datetime

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return "none"

# Start assistant
speak("Hello, I am your AI assistant. How can I help you?")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello! Nice to meet you")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("Current time is " + time)

    elif "your name" in command:
        speak("My name is Mini AI Assistant")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        break

    else:
        speak("Sorry, I did not understand")