import cv2
img = cv2.imread('1.jpg',1)
cv2.imshow('image',img)
cv2.line(img,(0,0),(400,300),(255,0,0),5)
cv2.imwrite('draw.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()