import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('digits.png',0)
#cat 1 anh thanh nhieu mang nho
cells = [np.hsplit(row,100) for row in np.vsplit(img,50)]

x = np.array(cells)
#tao du lieu traning va du lieu test
train = x[:,:50].reshape(-1,400).astype(np.float32)
test = x[:,50:100].reshape(-1,400).astype(np.float32)


#gan nhan cho du lieu train
k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]

#nhan dang
knn = cv2.ml.KNearest_create()
knn.train(train,0,train_labels)
kq1,kq2,kq3,kq4 = knn.findNearest(test,5)
print(kq2)

#cv2.waitKey(0)
#cv2.destroyAllWindows()