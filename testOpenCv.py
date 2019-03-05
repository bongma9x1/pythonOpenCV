import cv2
import numpy as np
img = cv2.imread('1.jpg',1)
cv2.imshow('image',img)
#cv2.line(img,(0,0),(400,300),(255,0,0),5)
#cv2.imwrite('draw.jpg',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

px = img[0][0]
#print(px)
#for i in range(100):
#	img[i][i] = [1,1,1]
#	img[i+2][i+2] = [1,1,1]
#cv2.imwrite('anh2.jpg',img)
#img1 =cv2.imread('anh2.jpg',1)
#cv2.imshow('img1',img)

#for i in range(100):
#	for j in range(200):
#		if img[i,j,0] > 30:
#			img[i,j] = [255,0,0]
#cv2.imwrite('anh2.jpg',img)
#img1 =cv2.imread('anh2.jpg',1)
#cv2.imshow('img1',img)

print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()