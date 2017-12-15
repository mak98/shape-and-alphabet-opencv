import numpy as np
import argparse
import imutils
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image file")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
j='0'
i=0
for angle in np.arange(0, 360, 45):
    rotated = imutils.rotate_bound(image, angle)
    cv2.imshow("Rotated (Correct)", rotated)
    if i==0:
        cv2.imwrite(j+'N.png',rotated)
    elif i==1:
        cv2.imwrite(j+'NE.png',rotated)
    elif i==2:
        cv2.imwrite(j+'E.png',rotated)
    elif i==3:
        cv2.imwrite(j+'SE.png',rotated)
    elif i==4:    
        cv2.imwrite(j+'S.png',rotated)
    elif i==5:
        cv2.imwrite(j+'SW.png',rotated)
    elif i==6:
        cv2.imwrite(j+'W.png',rotated)
    elif i==7:
        cv2.imwrite(j+'NW.png',rotated)
    i+=1
    cv2.waitKey(0)