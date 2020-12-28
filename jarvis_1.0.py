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
voices = engine.getProperty('voices')
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
    user_()
    flag = False
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        print("Good Morning sir !")
        speak("Good Morning sir !")
        flag = True
    elif hour >= 12 and hour < 18:
        print("Good Afternoon sir !")
        speak("Good Afternoon sir !")
        flag = True
    elif hour >= 18 and hour < 24:
        print("Good Evening sir !")
        speak("Good Evening sir !")
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

# username
def user_():
    speak("Face recognition start, Please look at camera")
    print("Face recognition start, Please look at camera")
    model = create_model()
    username = predict_persion(model=model)
    print(f"Welcome Mister {username}")
    speak("Welcome Mister")
    speak(username)

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

    while True:
        query = takecommand_().lower()

        if 'time' in query:
            time_()

        elif 'date' in query:
            date_()

        elif 'wikipedia' in query:
            speak("Searching.....")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=3)
            speak("Acording to wikipedia")
            print(result)
            speak(result)

        elif 'battery' in query:
            cpu_()

        elif 'cpu' in query:
            cpu_()

        elif 'how are you' in query:
            print("I am fine, Thank you")
            speak("I am fine, Thank you")
            print("How are you, Sir?")
            speak("How are you, Sir?")
            how_r_u = takecommand_()
            if 'fine' in how_r_u or "good" in how_r_u:
                print("It's good to know that your fine")
                speak("It's good to know that your fine")

        elif "change name" in query:
            print("What would you like to call me, Sir ?")
            speak("What would you like to call me, Sir ?")
            assistance_name = takecommand_()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assistance_name)
            print("My friends call me", assistance_name)

        elif "who made you" in query or "who created you" in query:
            print("I have been created by JVS group.")
            speak("I have been created by JVS group.")

        elif "who i am" in query:
            print("If you talk then definately your human.")
            speak("If you talk then definately your human.")

        elif 'reason for you' in query:
            print("I was created as a Minor project by JVS group")
            speak("I was created as a Minor project by JVS group")

        elif "jarvis" in query:
            print("Jarvis 1 point o in your service Mister")
            speak("Jarvis 1 point o in your service Mister")
            speak(username)

        elif 'screenshot' in query:
            screenshot_()

        elif 'bye' or 'exit' or 'stop' in query:
            stop()
            quit()
