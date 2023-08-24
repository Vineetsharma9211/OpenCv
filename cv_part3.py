import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    rep,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    img=cv2.line(frame,(0,0),(width ,height),(255,0,0),10)
    img=cv2.line(frame,(0,height),(width ,0),(0,255,0),5)
    img=cv2.rectangle(img,(100,100),(200,200),(0,0,255),2)
    img=cv2.circle(img, (300,300),60,(125,125,125),-1)
    font=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.putText(img,"Vineet is good boy",(200,height-10),
                    font,1,(0,0,0),5,cv2.LINE_AA)
    cv2.imshow('frame',img )
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
