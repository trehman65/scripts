import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np
import os
##HYPERPARAMETERS :P 
INPUT_DIR = "/Users/talha/Desktop/tobe/"
OUTPUT_DIR="/Users/talha/Desktop/croped2/"
current_file = None
gt_list=[]
image_data = None 
path=None 
image_path=None
outputDir=OUTPUT_DIR
dir = INPUT_DIR
def onclick(event):
    global path, gt_list, image_path, image_data, outputDir
    if event.dblclick:
        print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              (event.button, event.x, event.y, event.xdata, event.ydata))
        # print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f'(event.button, event.x, event.y, event.xdata, event.ydata)
        gt_list.append((event.xdata,event.ydata))
        if(len(gt_list)==2):
            image_data = image_data[int(gt_list[0][1]):int(gt_list[1][1]), int(gt_list[0][0]):int(gt_list[1][0])]
            temp_no=0
            while(os.path.isfile(outputDir+str(temp_no)+image)):
                temp_no+=1 
            cv2.imwrite(outputDir+str(temp_no) + image, image_data)
            image_data =None 
            gt_list=[]
            plt.close()
        import csv
        with open(current_file+".csv", 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([str(event.xdata), str(event.ydata)])
for image in os.listdir(dir):
    if image.endswith("jpg") or image.endswith("JPG"):
        if os.path.isfile(dir+image+".csv"):
            pass
        else:
            image_path = image
            fig = plt.figure()
            cid = fig.canvas.mpl_connect('button_press_event', onclick)
            print dir+image
            current_file = dir+image
            path=dir+image
            image_data=cv2.imread(dir+image)
            img=mpimg.imread(dir+image)
            plt.imshow(img)
            plt.show()