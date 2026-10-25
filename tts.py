
from cartesia import Cartesia
import os

# Connect to Cartesia
client = Cartesia(api_key=os.environ["CARTESIA_API_KEY"])

# sentences to test
sentences = [
    "Hello, my name is Masood. I study at Stanford University.",
    "The quick brown fox jumps over the lazy dog.",
    "My favorite programming language is Python!",
    "Dr. Smith works at NASA in California.",
    "Can artificial intelligence recognize speech correctly?"
]


# Generate audio for each sentence
for i, sentence in enumerate(sentences, start=1):
    response = client.tts.generate(
        model_id="sonic-latest",
        transcript=sentence,
        voice="6ccbfb76-1fc6-48f7-b71d-91ac6298247b",
        language="en",
        output_format={
            "container": "wav",
            "encoding": "pcm_s16le",
            "sample_rate": 44100,
        },
    )

    filename = f"sample_{i}.wav"
    response.write_to_file(filename)

    print("Created:", filename)

print("All five recordings generated!")
