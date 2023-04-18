"""
# Minor Project

# College: Oriental Institute of Science and Technology, Bhopal
# Project Name: SnapAI

# Branch: CSE-AIML
# Semester: 6th
# Team Members:
    1. Anushka Prajapati
    2. Aryan Chaurasia
    3. Pratyush Dixit

# Project Description:

# Project Features:

# Project Dependencies:

# Project Files:

"""

# Importing the required libraries
from switch import switch

# Importing the required libraries
from modules.txt2img import txt2img
from modules.voice2img import voice2img
from modules.img2txt import img2txt
from modules.imgrestoration import imgrestoration

# Main
def main():
  print("# Minor Project")
  print("Choose one of the following options:")
  print("1. Voice to Image")
  print("2. Text to Image")
  print("3. Image to Text")
  print("4. Image Restoration")
  opt_input = int(input("Enter your choice: "))
  print("You have chosen option: ", opt_input)
  
  # switch(opt_input)

  # Switch Case
  if opt_input == 1:
    voice2img()
  elif opt_input == 2:
    user_prompt = input("Enter your prompt: ")
    txt2img(user_prompt)
  elif opt_input == 3:
    img_url = input("Enter Image URL: ")
    img2txt(img_url)
  elif opt_input == 4:
    imgrestoration("images/input.jpg")
  else:
    print("Invalid Option")


if __name__ == "__main__":
  while True:
    main()