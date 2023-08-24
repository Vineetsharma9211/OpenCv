import cv2
import numpy as np
img=cv2.imread('soccer_practice.jpg',0)
img=cv2.resize(img,(0,0),fx=0.8,fy=0.7)
template=cv2.imread('ball.png',0)
template2=cv2.imread('shoe.png',0)
template2=cv2.resize(template2,(0,0),fx=0.5,fy=0.5)

h,w=template.shape
h2,w2=template2.shape
methods=[cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
for method in methods:
    img2=img.copy()
    
    result=cv2.matchTemplate(img2,template,method)
    result2=cv2.matchTemplate(img2,template2,method)
    
    min_value_1,max_value_1,min_loc_1,max_loc_1=cv2.minMaxLoc(result)
    min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(result2)
    location1=min_loc_1
    location2=min_loc
        
    bottom_right=(location1[0]+w,location1[1]+h)
    bottom_right_2=(location2[0]+w2,location2[1]+h2)
    cv2.rectangle(img2,location1,bottom_right,255,5)
    cv2.rectangle(img2,location2,bottom_right_2,255,5)
    cv2.imshow('match',img2)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
