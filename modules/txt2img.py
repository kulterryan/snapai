"""
Text 2 Image Generator Module
"""

import os
from dotenv import load_dotenv

import replicate
import requests

load_dotenv()

REPLICATE_API_TOKEN=os.getenv("REPLICATE_API_TOKEN")

def txt2img(inp_txt):
  print("STARTED: Text to Image Generator")
  print("Input Text: ", inp_txt)
  print("Please wait while the image is being generated...")

  # API Call
  output = replicate.run(
    "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
    input={
      "prompt": inp_txt
    }
  )
  
  # Download Image
  response = requests.get(output[0])
  with open("images/output.png", "wb") as file:
    file.write(response.content)
    print("Image Generation Complete")
    print("Output Image: images/output.png")
  
  os.system(r"images\output.png")