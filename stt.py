
import speech_recognition as sr

# Create a speech recognizer
recognizer = sr.Recognizer()

# Go through all five recordings
for i in range(1, 6):
    filename = f"sample_{i}.wav"

    # Read the audio file
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)

    # Convert audio into text
    text = recognizer.recognize_google(audio)

    print(f"Sample {i}: {text}")
