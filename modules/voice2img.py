"""
Voice 2 Image Generator Module
"""

# Importing Libraries
from voice2txt import voice2txt
import txt2img

def voice2img(inp_voice):
  print("HIT: Voice to Image Generator")
  print("Input Voice: ", inp_voice)
  txt2img.txt2img(inp_voice)
  
if __name__ == "__main__":
  inp_voice = voice2txt.voice2txt()
  voice2img(inp_voice)