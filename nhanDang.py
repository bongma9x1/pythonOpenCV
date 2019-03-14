import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('digits.png',0)
#cat 1 anh thanh nhieu mang nho
cells = [np.hsplit(row,100) for row in np.vsplit(img,50)]

cv2.imwrite('anhso.jpg',cells[0][0])
#chuyen mang sang numpy
x = np.array(cells)
#chia thanh mang 1 chieu moi chieu 20 pixel
xx = x[0,0].reshape(-1,20)
print(xx)

cv2.waitKey(0)
cv2.destroyAllWindows()