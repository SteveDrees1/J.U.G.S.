import modules.voice_recognition as vr
import modules.nlp as nlp
import modules.smart_home as smart_home
import modules.tts as tts


def main():
    tts.speak("Hello Big Daddy! How can I assist you today?")

    while True:
        # Get voice command
        command = vr.handle_recognition()
        if command:
            print(f"You said: {command}")  # Debugging

            # Process the command using NLP
            action = nlp.process_command(command)
            print(f"Action: {action}")  # Debugging

            # Execute corresponding action
            if action == "turn_on_lights":
                smart_home.turn_on_lights()
                tts.speak("Turning on the lights.")
            elif action == "turn_off_lights":
                smart_home.turn_off_lights()
                tts.speak("Turning off the lights.")
            elif action.strip().lower() == "exit":  # Case-insensitive and whitespace trimming
                tts.speak("Goodbye!")
                break
            else:
                tts.speak(f"Sorry, I didn't understand the command: {command}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Handle the KeyboardInterrupt gracefully
        print("\nProgram interrupted by the user. Exiting gracefully...")
        try:
            tts.speak("Goodbye Big Daddy!!")  # Say goodbye before exiting
        except KeyboardInterrupt:
            # If the user interrupts again, exit without further delay
            print("\nForced exit. Goodbye!")
        exit(0)

