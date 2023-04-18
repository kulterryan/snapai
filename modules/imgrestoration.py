import os
from dotenv import load_dotenv

import replicate
import requests

load_dotenv()
REPLICATE_API_TOKEN=os.getenv("REPLICATE_API_TOKEN")

def imgrestoration(path_img):
  print("STARTED: Image Restoration Module")
  print("Input Image: ", path_img)
  print("Please wait while the image is being restored...")

  # API Call
  output = replicate.run(    
    "jingyunliang/swinir:660d922d33153019e8c263a3bba265de882e7f4f70396546b6c9c8f9d47a021a",
    input={
      "image": open(r'{}'.format(path_img),
      "rb"
    )}
  )  

  # Download Image
  response = requests.get(output)
  with open("images/output.png", "wb") as file:
    file.write(response.content)  
    print("Image Restoration Complete")
    print("Output Image: images/output.png")
    os.system(r"images\output.png")

  return 0