import pyttsx3
import speech_recognition as sr
from sound import play_sound

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak_text(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Listen for a voice command and return the text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        play_sound()
        #speak_text("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        speak_text("Sorry, I did not understand that.")
    except sr.RequestError:
        speak_text("Sorry, I am having trouble with the service.")
    return ""
