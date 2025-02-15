import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

# Define the music library
music = {
    "let her go": "https://youtu.be/HTcL9WkB_wg?si=SIIiCbdh_FkMisOs"
}

def speak(text):
    """Convert text to speech."""
    ttsx.say(text)
    ttsx.runAndWait()

def process_command(command):
    """Process voice commands."""
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "play" in command:
        song = command.replace("play", "").strip()  # Extract song name after "play"
        if song in music:
            webbrowser.open(music[song])
            speak(f"Playing {song}")
        else:
            speak(f"Sorry, I don't have {song} in my library.")

    elif "what is the time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif "exit" in command:
        speak("Exiting Jarvis")
        return True  # Exit the loop

    else:
        speak(f"You said: {command}")

    return False  # Continue listening

def listen_for_command():
    """Listen for voice commands and return recognized text."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for command...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Google thinks you said: {command}")
            return command
        except sr.UnknownValueError:
            print("Google could not understand the audio")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        print("Say 'Jarvis' to activate...")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=5)  # Listen with timeout
                wake_word = recognizer.recognize_google(audio).lower()
                print(f"Google thinks you said: {wake_word}")

                if "jarvis" in wake_word:  # Check if "jarvis" is present
                    speak("Yes, how can I assist you?")
                    command = listen_for_command()

                    if command:
                        exit_flag = process_command(command)
                        if exit_flag:
                            break
            except sr.UnknownValueError:
                print("Google could not understand the audio")
            except Exception as e:
                print(f"Error: {e}")
