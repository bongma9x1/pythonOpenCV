import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('digits.png',0)
#cv2.imshow('tes',img)

cells = [np.hsplit(row,100) for row in np.vsplit(img,50)]
print(cells[0][0])
cv2.waitKey(0)
cv2.destroyAllWindows()