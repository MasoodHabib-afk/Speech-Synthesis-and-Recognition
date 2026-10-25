
import speech_recognition as sr
from jiwer import wer
import string

# Original sentences
sentences = [
    "Hello, my name is Masood. I study at Stanford University.",
    "The quick brown fox jumps over the lazy dog.",
    "My favorite programming language is Python!",
    "Dr. Smith works at NASA in California.",
    "Can artificial intelligence recognize speech correctly?"
]


recognizer = sr.Recognizer()

# Remove capitalization and punctuation
def clean_text(sentence):
    return sentence.lower().translate(
        str.maketrans("", "", string.punctuation)
    )

# Evaluate all five recordings
for i, original in enumerate(sentences, start=1):
    filename = f"sample_{i}.wav"

    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)

    recognized = recognizer.recognize_google(audio)

    error = wer(clean_text(original), clean_text(recognized))

    print(f"\nSample {i}")
    print("Original:", original)
    print("Recognized:", recognized)
    print(f"Word Error Rate: {error:.2%}")
