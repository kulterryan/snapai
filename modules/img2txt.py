"""
Image to Text Generator Module
"""

import os
from dotenv import load_dotenv
import azure.ai.vision as vision

load_dotenv()

vsep = os.environ["VISION_ENDPOINT"]
vskey = os.environ["VISION_KEY"]

if (vsep):
  print("Vision Endpoint: " + vsep)
else:
  print("Vision Endpoint not found")

def img2txt(img_url):
  print("STARTED: Image to Text Converter\n--")

  # Service Options
  service_options = vision.VisionServiceOptions(vsep, vskey)

  # Image Source
  vision_source = vision.VisionSource(url=img_url)

  # Image Analysis Options
  analysis_options = vision.ImageAnalysisOptions()
  analysis_options.features = (vision.ImageAnalysisFeature.CAPTION | vision.ImageAnalysisFeature.TEXT )
  analysis_options.language = "en"
  analysis_options.gender_neutral_caption = True

  # Init Image Analyzer
  image_analyzer = vision.ImageAnalyzer(service_options, vision_source, analysis_options)

  # Analyze Image
  result = image_analyzer.analyze()

  if result.reason == vision.ImageAnalysisResultReason.ANALYZED:
      if result.caption is not None:
          print("Caption:")
          print("   '{}'".format(result.caption.content))
          print("Confidence Score:")
          print("   '{:.4f}'".format(result.caption.confidence))

      # if result.text is not None:
      #     print(" Text:")
      #     for line in result.text.lines:
      #         points_string = "{" + ", ".join([str(int(point)) for point in line.bounding_polygon]) + "}"
      #         print("   Line: '{}', Bounding polygon {}".format(line.content, points_string))
      #         for word in line.words:
      #             points_string = "{" + ", ".join([str(int(point)) for point in word.bounding_polygon]) + "}"
      #             print("     Word: '{}', Bounding polygon {}, Confidence {:.4f}"
      #                   .format(word.content, points_string, word.confidence))

  elif result.reason == vision.ImageAnalysisResultReason.ERROR:

      error_details = vision.ImageAnalysisErrorDetails.from_result(result)
      print("Analysis failed.")
      print("   Error reason: {}".format(error_details.reason))
      print("   Error code: {}".format(error_details.error_code))
      print("   Error message: {}".format(error_details.message))

if __name__ == "__main__":
  img_url = input("Enter Image URL: ")
  img2txt(img_url)