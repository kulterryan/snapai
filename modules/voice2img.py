"""
Voice 2 Image Generator Module
"""

# Importing Libraries
from voice2txt import voice2txt
from txt2img import txt2img
from voicerecorder import record_voice

def voice2img(inp_voice):
  print("HIT: Voice to Image Generator")
  print("Input Voice: ", inp_voice)
  txt2img(inp_voice)
  
if __name__ == "__main__":
  record_voice()
  inp_voice = voice2txt("audio/recording.wav")
  inp_voice
  voice2img(inp_voice)