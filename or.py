import cv2
import numpy as np
checks = cv2.imread('example_04.png',0)
ret, thresh2 = cv2.threshold(checks, 127, 255,0)
_,contours,hierarchy= cv2.findContours(thresh2,2,1)
cnt1 = contours[0]
(x,y),(MA,ma),angle = cv2.fitEllipse(cnt1)
print(x,y,MA,ma,angle)
cv2.imshow('tresh',thresh2)
cv2.waitKey()
cv2.destroyAllWindows()