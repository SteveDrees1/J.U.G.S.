import speech_recognition as sr
import sys  # Import sys for program exit
import modules.tts as tts  # Assuming tts is your text-to-speech module

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


# Function to get audio input from the microphone
def get_audio_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # You can add a timeout or phrase_time_limit to control how long it listens
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    return audio


# Recognize speech using Google Cloud Speech API (Requires API credentials)
def recognize_google_cloud(audio, credentials_json):
    recognizer = sr.Recognizer()
    try:
        print("Recognizing using Google Cloud Speech API...")
        text = recognizer.recognize_google_cloud(audio, credentials_json="/Users/bigdaddy/credentials/jugs-google"
                                                                         "-cloud-credentials.json")
        print(f"Google Cloud recognized: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Cloud Speech API; {e}")
    return None


# Recognize speech using CMU Sphinx (Offline, but less accurate)
def recognize_sphinx(audio):
    recognizer = sr.Recognizer()
    try:
        print("Recognizing using Sphinx (offline)...")
        text = recognizer.recognize_sphinx(audio)
        print(f"Sphinx recognized: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sphinx could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Sphinx; {e}")
    return None

# Main function to handle speech recognition by trying Google Cloud first, then Sphinx (offline)
def handle_recognition():
    while True:
        # Get the audio input from the microphone
        audio = get_audio_input()

        # First try Google Cloud Speech API
        result = recognize_google_cloud(audio, "/Users/bigdaddy/credentials/jugs-google-cloud-credentials.json")

        if not result:
            # If Google Cloud fails, try Sphinx for offline recognition
            result = recognize_sphinx(audio)

        if result:
            print(f"Final recognized text: {result}")
            # If the user says 'exit', stop the loop and exit the program
            if 'exit' in result:
                print("Exit command recognized. Stopping...")
                # Use TTS to say goodbye
                tts.speak("Thanks Big Daddy, goodbye!")

                sys.exit(0)  # Exit the entire program
        else:
            print("Could not recognize speech.")
