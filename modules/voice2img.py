"""
Voice 2 Image Generator Module
"""

# Importing Libraries
from modules import voice2text, txt2img

def voice2img(inp_voice):
  print("HIT: Voice to Image Generator")
  print("Input Voice: ", inp_voice)
  txt2img.txt2img(inp_voice)

  
def main():
  inp_voice = voice2text.voice2text()
  voice2img(inp_voice)