import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to capture audio from the microphone
def record_audio():
    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return audio

# Function to convert speech to text
def speech_to_text(audio):
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f'Speech recognized: "{text}"')
        return text
    except:
        return "Speech Recognition could not understand audio, Please try speaking more clearly."
    

# Main Function
def main():
    audio = record_audio()
    speech_to_text(audio)
if __name__ == "__main__":
    main()
