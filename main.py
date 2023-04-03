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
  switch(opt_input)
  print("Hello World!")

if __name__ == "__main__":
  main()