from xml.dom import minidom
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

outputLines=[]
finalOutputJson="/Users/talha/Desktop/xmlomni/5.json"
xmldoc = minidom.parse('/Users/talha/Desktop/5.xml')

lines = xmldoc.getElementsByTagName('ln')
lenLines = len(lines)

count=1;

for s in lines:

	if count > lenLines:
		break

	words = s.getElementsByTagName('wd')
	thisLine=""

	for t in words:
		thisWord=t.childNodes[0].nodeValue
		if(thisWord!=None):
			thisLine = thisLine + thisWord + " "
	
	l=s.attributes['l'].value
	r=s.attributes['r'].value
	t=s.attributes['t'].value
	b=s.attributes['b'].value
	
	temp={}
	temp["id"]=count
	temp["l"]=l
	temp["r"]=r
	temp["t"]=t
	temp["b"]=b
	temp["text"]=thisLine

	outputLines.append(temp)
	print thisLine
	count=count+1

with open(finalOutputJson, 'w') as outfile:  
        json.dump(outputLines, outfile)