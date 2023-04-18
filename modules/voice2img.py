"""
Voice 2 Image Generator Module
"""

# Importing Libraries
from modules.voice2txt import voice2txt
from modules.txt2img import txt2img
from modules.voicerecorder import record_voice

def voice2img():
  record_voice()
  inp_voice = voice2txt("audio/recording.wav")
  print("STARTED: Voice to Image Generator")
  print("Input Voice: ", inp_voice)
  txt2img(inp_voice)