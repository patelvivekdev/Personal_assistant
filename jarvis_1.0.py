# Import Tools
import pyttsx3
import datetime
import psutil
import pyaudio
import speech_recognition as sr
import wikipedia
import pyautogui
from face_recognition import create_model
from face_recognition import predict_persion

# Init
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# define assistant name
assistance_name = "Jarvis 1 point o"

# define username
username = ""

# Speak fun
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Time
def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("sir! the current time is:")
    print("sir! the current time is", Time)
    speak(Time)

# Date
def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    print("sir! the current date is:", day, month, year)
    speak("sir! the current date is ")
    speak(day)
    speak(month)
    speak(year)

# CPU & BATTERY
def cpu_():
    usage = str(psutil.cpu_percent())
    print("CPU is at " + usage)
    speak("CPU is at " + usage)

    battery = psutil.sensors_battery()
    print("Battery is at", battery.percent)
    speak("Battery is at")
    speak(battery.percent)

# Greeting
def greeting_():
    speak("Jarvis 1 point o in your service Mister")
    print("Jarvis 1 point o in your service Mister")
    user_()
    flag = False
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")
        flag = True
    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
        flag = True
    elif hour >= 18 and hour < 24:
        print("Good Evening!")
        speak("Good Evening!")
        flag = True
    else:
        print("it's time to bad sir ! Good night")
        speak("it's time to bad sir ! Good night")
        flag = False
    if flag:
        print("checking functionality")
        speak("checking functionality")
        cpu_()

# TO Take voice command
def takecommand_():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-US")
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"

    return query

def startcommand_():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-US")
    
    except Exception as e:
        print(e)
        return "None"
    
    return query


# username
def user_():
    speak("Face recognition starting in a moment")
    print("Face recognition starting in a moment")
    model = create_model()
    speak("Face recognition start, Please look at camera")
    print("Face recognition start, Please look at camera")
    username = predict_persion(model=model)
    speak("Welcome mister")
    speak(username)
    print(f"Welcome mister {username}")

# Screenshot
def screenshot_():
    image = pyautogui.screenshot()
    image.save(
        'C:/VIVEK/1.PYTHON_DEV/project/1.CLG_PROJECT/Personal_assistant/img.png')

# To stop
def stop():
    print("Thanks for giving me your time")
    speak("Thanks for giving me your time")
    print("See you soon,sir!")
    speak("See you soon,sir!")


if __name__ == "__main__":

    greeting_()
    print("Started.....")
    while True:
        start = startcommand_().lower()
        WAKE = "jarvis"

        if start.count(WAKE) > 0:
            print("How may i help you?")
            speak("How may i help you?")

            while True:
                query = takecommand_().lower()
                        
                if 'time' in query:
                    time_()
                if 'date' in query:
                    date_()
                if 'wikipedia' in query:
                    speak("Searching.....")
                    query = query.replace('wikipedia', '')
                    result = wikipedia.summary(query, sentences=3)
                    speak("Acording to wikipedia")
                    print(result)
                    speak(result)
                if 'battery' in query:
                    cpu_()
                if 'cpu' in query:
                    cpu_()
                if 'how are you' in query:
                    print("I am fine, Thank you")
                    speak("I am fine, Thank you")
                    print("How are you, Sir?")
                    speak("How are you, Sir?")
                    how_r_u = takecommand_()
                    if 'fine' in how_r_u or "good" in how_r_u:
                        print("It's good to know that your fine")
                        speak("It's good to know that your fine")
                if "change name" in query:
                    print("What would you like to call me, Sir ?")
                    speak("What would you like to call me, Sir ?")
                    assistance_name = takecommand_()
                    speak("Thanks for naming me")
                if "what's your name" in query or "What is your name" in query:
                    speak("My friends call me")
                    speak(assistance_name)
                    print("My friends call me", assistance_name)
                if "who made you" in query or "who created you" in query:
                    print("I have been created by JVS group.")
                    speak("I have been created by JVS group.")
                if "who i am" in query:
                    print("If you talk then definately your human.")
                    speak("If you talk then definately your human.")
                if 'reason for you' in query:
                    print("I was created as a Minor project by JVS group")
                    speak("I was created as a Minor project by JVS group")
                if 'screenshot' in query:
                    screenshot_()
                if 'stop' in query:
                    stop()
                    break