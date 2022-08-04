import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')  #get all the voices 
# print(voices[1].id)
engine.setProperty('voice', voices[0].id) #setting voice Id (men/women)


def speak(audio):
    engine.say(audio)   
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Im Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com', 'Shadow7925')
    server.sendmail('yourmail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        
        elif 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")
        
        elif 'instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")

        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")
            
        elif 'facebook' in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
            
        elif 'open geeks' in query:
            speak("opening geeks")
            webbrowser.open("https://www.geeksforgeeks.org/")
              
        elif 'github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")
            
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")
            
        elif 'open google' in query:
            speak('Okay!')
            speak("opening google")
            webbrowser.open("google.com")
             
        elif 'google' in query:
            speak('Okay!')
            speak("opening google")
            webbrowser.open("google.com") 


        elif 'play music' in query:
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'music' in query:
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'romantic music' in query:
            music_dir = 'F:\\Music1'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'jarvis time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\xyz\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to sk' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry . I am not able to send this email")    
