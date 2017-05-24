import sys
import os

path=sys.argv[1]
images=[f for f in os.listdir(path) if f.endswith('.jpg')];
pathtojson='/Users/talha/Coding/ClionProjects/CameraOCR/build/CameraOCR '
pathtoeval='/Users/talha/Coding/ClionProjects/CameraOCR/build/CameraOCREvaluation '

for image in images:
	print image
	filename=image.strip('.jpg');
	gt=filename+'.csv'
	omniout=image+'.txt'
	omnijson=filename+'-table.json'
	command1=pathtojson+path+image+' 1 z '+path+omniout
	command2=pathtoeval+path+omnijson+' '+path+gt

	os.system(command1)
	os.system(command2)