"""
Voice 2 Image Generator Module
"""

# Importing Libraries
from modules.voice2txt import voice2txt
from modules.txt2img import txt2img
from modules.voicerecorder import record_voice

def voice2img():
  # Recorder
  record_voice()

  # Voice to Text
  inp_voice = voice2txt("audio/recording.wav")

  # Text to Image
  print("STARTED: Voice to Image Generator")
  print("Input Voice: ", inp_voice)
  txt2img(inp_voice)