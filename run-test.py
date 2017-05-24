import sys
import os

path=sys.argv[1]
images=[f for f in os.listdir(path) if f.endswith('.jpg')];
pathtocameraocr='/Users/talha/Coding/ClionProjects/CameraOCR/build/CameraOCR '
pathtoeval='/Users/talha/Coding/ClionProjects/CameraOCR/build/CameraOCREvaluation '
gtpath='/Users/talha/Desktop/gt/'
pathgoogleoutput='/Users/talha/Desktop/googleoutput/'



for image in images:
	print image
	filename=image.strip('.jpg');
	gt=filename+'.csv'
	googleoutfile= filename +’.csv’
	command1= pathtocameraocr+path+image+' 1 z '+ pathgoogleoutput + googleoutfile
	googlejson=filename+'-table.json'
	command2=pathtoeval+path+ googlejson +' '+ gtpath+gt

	print command1

	#os.system(command1)
	#os.system(command2)