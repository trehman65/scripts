import sys
import os

path=sys.argv[1]
images=[f for f in os.listdir(path) if f.endswith('.jpg')];
pathtocamera='/Users/talha/Coding/ClionProjects/CameraOCR/build/CameraOCR '
pathtoeval='/Users/talha/Coding/ClionProjects/CameraOCR/build/CameraOCREvaluation '


for image in images:
	print image
	filename=image.strip('.jpg');
	gtpath='/Users/talha/Desktop/groundtruth/'+filename+'.csv'
	googleoutpath='/Users/talha/Desktop/googleoutput/'+filename+'.csv'
	googlejsonpath=path+filename+'-table.json'
	command1=pathtocamera+path+image+' 1 z '+googleoutpath
	command2=pathtoeval+googlejsonpath+' '+gtpath

	os.system(command1)
	os.system(command2)