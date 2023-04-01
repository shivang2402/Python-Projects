import pyttsx3

# Initializing the engine
engine = pyttsx3.init()

# Set properties for the voice
voices = engine.getProperty('voices')
# Print all available voices
for voice in voices:
    print(voice.id)
# Change the voice to another language, e.g., French
engine.setProperty('voice', 'fr-FR')

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            break
        lang = input("Enter language code (e.g. en-US, fr-FR, de-DE): ")
        engine.setProperty('voice', lang)
        speak(x)
