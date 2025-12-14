from piper import PiperVoice
from pydub import AudioSegment
from urllib.request import urlopen
import json
import wave


voice_model = PiperVoice.load("en_US-lessac-medium.onnx", config_path="en_US-lessac-medium.onnx.json", use_cuda=True)

with wave.open("output.wav", "wb") as wav_file:
  with open("story.txt", "r", encoding="utf-8") as story_file:
    story_text = story_file.read()
    voice_model.synthesize_wav(
      text=story_text,
      wav_file=wav_file
    )
sound = AudioSegment.from_wav("output.wav")
sound.export("output.mp3", format="mp3", bitrate="192k")