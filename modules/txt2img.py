"""
Text 2 Image Generator Module
"""

#def txt2img():
  #print("Text to Image Converter")

import os
from dotenv import load_dotenv

load_dotenv()
REPLICATE_API_TOKEN=os.getenv("REPLICATE_API_TOKEN")

import replicate
output = replicate.run(
    "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
    input={"prompt": "a forest with animals in it."}
)
print(output)
