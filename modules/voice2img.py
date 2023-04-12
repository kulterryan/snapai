"""
Voice 2 Image Generator Module
"""

# Importing Libraries
from modules import voice2text

def voice2img(inp_voice):
  print("HIT: Voice to Image Generator")
  print("Input Voice: ", inp_voice)
  
def main():
  inp_voice = voice2text.voice2text()
  voice2img(inp_voice)

if __name__ == "__main__":
  main()