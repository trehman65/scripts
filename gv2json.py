import io
import os
import glob
import csv
import cv2
import sys
import re
import natsort
import time
import sys
import json
import os.path

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud import credentials

finalOutputJson=""

#credentials = credentials.get_credentials()
vision_client = vision.Client()

def detect_documentT(path):
    listDetections = []

    data=[]


    """Detects document features in an image."""
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    imageOpenCV = cv2.imread(path)

    cv2.imwrite(finalOutputImage,imageOpenCV)

    image = vision_client.image(content=content)

    document = image.detect_full_text()
    print document.pages[0].blocks

    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    wordString = ''
                    for symbol in list(word.symbols):
                        wordString = wordString + symbol.text
                   # print wordString
                    tl = list(word.bounding_box.vertices)[0]
                    br = list(word.bounding_box.vertices)[2]
                    listDetections.append((tl,br,wordString))
                    wordString = wordString.replace("\"", "")
                    
                    temp={}
                    temp['word']=wordString.encode("utf-8");
                    temp['boundingbox']={}
                    temp['boundingbox']['l']=tl.x;
                    temp['boundingbox']['t']=tl.y;
                    temp['boundingbox']['r']=br.x;
                    temp['boundingbox']['b']=br.y;
                    data.append(temp);


                    cv2.rectangle(imageOpenCV,(tl.x, tl.y), (br.x, br.y), (0, 0, 255), 4)
   
    cv2.imwrite(finalOutputImage,imageOpenCV)

    with open(finalOutputJson, 'w') as outfile:  
        json.dump(data, outfile)
    print "Done with " + str(path)


finalInput=sys.argv[1]
words=finalInput.split('/')
filename = words[len(words)-1]

folderpath=finalInput.replace(filename,"")
filename = filename.replace(".jpeg", "")
filename = filename.replace(".JPG", "")
filename = filename.replace(".png", "")

finalOutputJson=folderpath + filename + ".json"
finalOutputImage = folderpath + filename +"-seg"+ ".png"
detect_documentT(finalInput)
