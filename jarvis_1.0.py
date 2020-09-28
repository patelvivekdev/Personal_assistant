# Import Tools
import pyttsx3
import datetime
import psutil
import pyaudio
import speech_recognition as sr
import wikipedia

# Init
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)


# Speak fun
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("sir! the current time is:")
    print("sir! the current time is",Time)
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    print("sir! the current date is:" ,day,month,year)
    speak("sir! the current date is ")
    speak(day)
    speak(month)
    speak(year)

def cpu():
    usage = str(psutil.cpu_percent())
    print("CPU is at "+ usage)
    speak("CPU is at "+ usage)

    battery = psutil.sensors_battery()
    print("Battery is at" , battery.percent)
    speak("Battery is at")
    speak(battery.percent)

def greeting_():
    def time_():
        Time = datetime.datetime.now().strftime("%I:%M:%S")
        return Time
    Time = time_()    
    print("welcome back sir!")
    speak("welcome back sir!")
    flag = False
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        print("Good Morning")
        speak("Good Morning")
        print("Time is ",Time)
        speak("Time is " +Time)
        flag = True
    elif hour>=12 and hour < 18:
        print("Good Afternoon")
        speak("Good Afternoon")
        print("Time is ",Time)
        speak("Time is " +Time)
        flag = True
    elif hour >= 18 and hour < 24:
        print("Good Evening")
        speak("Good Evening")
        print("Time is ",Time)
        speak("Time is " +Time)
        flag = True
    else:
        print("it's time to bad sir! Good night")
        speak("it's time to bad sir! Good night")
        flag = False
    if flag:
        print("checking functionality")
        speak("checking functionality")
        cpu()
        print("Jarvis at your service. How can i help you today?")
        speak("Jarvis at your service. How can i help you today?")

def takecommnd_():
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

def stop():
    speak("See you soon,sir!")
    print("See you soon,sir!")

if __name__ == "__main__":

    greeting_()
    while True:
        query = takecommnd_().lower()
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak("Searching.....")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=3)
            speak("Acording to wikipedia")
            print(result)
            speak(result)
        elif 'battery' in query:
            cpu()
        elif 'bye' in query:
            stop()
            break