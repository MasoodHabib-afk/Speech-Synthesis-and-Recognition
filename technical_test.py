
import os
import string
import speech_recognition as sr
from cartesia import Cartesia
from jiwer import wer

# The passage I want to test


original = """
Professor Sarah Mitchell and Doctor Ahmed Khan are developing a speech recognition system at Stanford University. Their research focuses on artificial intelligence, natural language processing, and speech synthesis.

The research team collected audio recordings from several participants. Each participant read sentences about computer science, machine learning, and modern technology.

During the experiment, the researchers tested how accurately the system converted spoken sentences into written text. They compared each original sentence with its transcription and measured the word error rate.

The results helped the researchers understand how speech recognition systems process technical vocabulary and longer sentences. Their next goal is to improve transcription accuracy across different speaking styles and recording conditions.
"""



# Generate speech using Cartesia
client = Cartesia(api_key=os.environ["CARTESIA_API_KEY"])

response = client.tts.generate(
    model_id="sonic-latest",
    transcript=original,
    voice={
        "mode": "id",
        "id": "6ccbfb76-1fc6-48f7-b71d-91ac6298247b"
    },
    language="en",
    output_format={
        "container": "wav",
        "encoding": "pcm_s16le",
        "sample_rate": 44100
    }
)

response.write_to_file("challenging.wav")
print("Audio generated successfully!")

# Recognize the generated speech
recognizer = sr.Recognizer()

with sr.AudioFile("challenging.wav") as source:
    audio = recognizer.record(source)

recognized = recognizer.recognize_google(audio)

# Clean text before calculating WER
def clean_text(sentence):
    return sentence.lower().translate(
        str.maketrans("", "", string.punctuation)
    )

error = wer(clean_text(original), clean_text(recognized))

# Display results
print("\nOriginal:", original)
print("\nRecognized:", recognized)
print(f"\nWord Error Rate: {error:.2%}")
