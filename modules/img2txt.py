"""
Image to Text Generator Module
"""

# # Importing required libraries
# import io
# import os

# # Imports the Google Cloud client library
# from google.cloud import vision

# def imagex():
#   # Instantiates a client
#   client = vision.ImageAnnotatorClient()

#   # The name of the image file to annotate
#   file_name = os.path.abspath('resources/wakeupcat.jpg')

#   # Loads the image into memory
#   with io.open(file_name, 'rb') as image_file:
#       content = image_file.read()

#   image = vision.Image(content=content)

#   # Performs label detection on the image file
#   response = client.label_detection(image=image)
#   labels = response.label_annotations

#   print('Labels:')
#   for label in labels:
#       print(label.description)

def img2txt():
  print("Image to Text Converter")

# def detect_labels_uri(uri):
#   client = vision.ImageAnnotatorClient()
#   image = vision.Image()
#   image.source.image_uri = uri

#   response = client.label_detection(image=image)
#   labels = response.label_annotations
#   print('Labels:')

#   for label in labels:
#       print(label.description)

#   if response.error.message:
#       raise Exception(
#           '{}\nFor more info on error messages, check: '
#           'https://cloud.google.com/apis/design/errors'.format(
#               response.error.message))
  
# detect_labels_uri(uri="https://cdn.arstechnica.net/wp-content/uploads/2023/01/catplay.jpg")