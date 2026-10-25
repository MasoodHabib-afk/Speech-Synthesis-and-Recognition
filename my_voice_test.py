
import speech_recognition as sr
from jiwer import wer
import string

original = "Hello, my name is Masood. I study at Stanford University."

recognizer = sr.Recognizer()

# Load my personal recording
with sr.AudioFile("my_voice_compatible.wav") as source:
    audio = recognizer.record(source)

# Convert my voice into text
recognized = recognizer.recognize_google(audio)

# Clean text for word comparison
def clean_text(sentence):
    return sentence.lower().translate(
        str.maketrans("", "", string.punctuation)
    )

error = wer(clean_text(original), clean_text(recognized))

print("Original:", original)
print("Recognized:", recognized)
print(f"Word Error Rate: {error:.2%}")
