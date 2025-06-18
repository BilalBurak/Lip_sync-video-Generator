from TTS.api import TTS

# Load a free TTS model (offline)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

text = "Welcome to the future of generative AI. Today, you will see how machines can talk, learn, and think creatively."

# Generate and save audio
tts.tts_to_file(text=text, file_path="speech.wav")

print("✅ Audio saved as 'speech.wav'")
