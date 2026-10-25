import soundfile as sf

# Read the existing WAV recording
audio, sample_rate = sf.read("my_voice.wav")

# Save it in a standard PCM format
sf.write(
    "my_voice_compatible.wav",
    audio,
    sample_rate,
    subtype="PCM_16"
)

print("Audio converted successfully!")
