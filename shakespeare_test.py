
import os
import string
import speech_recognition as sr
from cartesia import Cartesia
from jiwer import wer

# The passage I want to test


original = """
To speak or not to speak, that is the question, said Professor Eleanor Whitmore as she entered the university laboratory.

Beside her stood Doctor Ahmed Khan, who had spent many hours studying the voices of scholars and travelers.

Alas, cried the professor, can this remarkable machine understand the words of a thoughtful scholar and the whispers of a weary traveler?

The researchers listened carefully as the machine repeated each sentence. They spoke of ancient kingdoms, noble kings, distant lands, and the mysteries of human language.

When the experiment ended, the professor smiled and said, The answer, my dear friend, is not so simple. For language is a wonderful thing, and even the cleverest machine may sometimes misunderstand its meaning.
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

response.write_to_file("shakespeare.wav")
print("Audio generated successfully!")

# Recognize the generated speech
recognizer = sr.Recognizer()

with sr.AudioFile("shakespeare.wav") as source:
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
