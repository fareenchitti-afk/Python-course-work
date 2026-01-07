import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {command}\n")
            return command.lower()
        
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return ""
        
        except sr.RequestError:
            print("Speech service is down.")
            speak("Speech service is down.")
            return ""
        
def run_assistant():
    speak("Hello! I'm your virtual assistant. How can I help you?")
    while True:
        command = listen()

        if 'time' in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

        elif 'date' in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'your name' in command:
            speak("I am your Python assistant!")

        elif 'stop' in command or 'exit' in command or 'bye' in command:
            speak("Okay bye bye! Have a good day")
            break

        else:
            speak("Sorry, I can't do that yet.")

# Run the assistant
run_assistant()