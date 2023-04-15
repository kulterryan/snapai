import os
from dotenv import load_dotenv

load_dotenv()
REPLICATE_API_TOKEN=os.getenv("REPLICATE_API_TOKEN")

import replicate
output = replicate.run(
    "jingyunliang/swinir:660d922d33153019e8c263a3bba265de882e7f4f70396546b6c9c8f9d47a021a",
    input={"image": open(r'C:\Users\Asus\Downloads\main-qimg-1f718d061c7444511cd1bcd80b6b53c4-lq.jpeg', "rb")}
)
print(output)