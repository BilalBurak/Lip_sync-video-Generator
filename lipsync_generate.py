import os
print("📂 Current working directory:", os.getcwd())
print("📁 Files in current directory:", os.listdir())
# Define paths
face_image = "input_video3.mp4"
audio_file = "speech.wav"
output_video = "output_video.mp4"
checkpoint_path = "Wav2ip/checkpoints/wav2lip.pth"

# Check all files exist
assert os.path.exists(face_image), f"❌ {face_image} not found!"
assert os.path.exists(audio_file), f"❌ {audio_file} not found!"
assert os.path.exists(checkpoint_path), f"❌ {checkpoint_path} not found!"

# Build Wav2Lip command
cmd = f"python Wav2ip/inference.py --checkpoint_path {checkpoint_path} --face {face_image} --audio {audio_file} --outfile {output_video}"

# Run command
print("▶️ Running Wav2Lip...")
os.system(cmd)
print(f"✅ Video saved as '{output_video}'")
