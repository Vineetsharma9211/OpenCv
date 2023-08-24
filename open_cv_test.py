import cv2

img=cv2.imread('Photo.jpg',-1)
img=cv2.resize(img,(1000,1000))
#cv2.imshow('Image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
tag=img[500:700,300:500]
img[100:300,700:900]=tag
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
