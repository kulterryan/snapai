# Description: Switch Case for the main.py

# Importing the required libraries
from modules.txt2img import txt2img
from modules.voice2img import voice2img
from modules.img2txt import img2txt
from modules.imgrestoration import imgrestoration

# Switch Case
def switch(opt_input):
  match opt_input:
    case 1:
      voice2img()
    case 2:
      txt2img()
    case 3:
      img2txt()
    case 4:
      imgrestoration("images/input.jpg")
    case _:
      print("Invalid Option")