import cv2
import numpy as np
import matplotlib.pyplot as plt
#img = cv2.imread('5.jpg',1)
#cv2.imshow('image',img)
#cv2.line(img,(0,0),(400,300),(255,0,0),5)
#cv2.imwrite('draw.jpg',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#px = img[0][0]
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

#doc thuoc tinh cua anh cat ghep va doi kenh mau
#print(img.shape)
#print(img.size)
#print(img.dtype)
#subimg = img[0:300,0:300]
#subimg = subimg[:,:,1]
#cv2.imshow('image',subimg)

#tach doi tuong theo mau quy dinh
	#chuyen BGR to HSV
#img1 = np.uint8([[[2,40,245]]])
#img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
#print(img1)
#hsb_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#cv2.imshow('buc anh cover',hsb_img)
#min_mau = np.array([151,236,116])
#max_mau = np.array([160,236,116])
#mask = cv2.inRange(hsb_img,min_mau,max_mau)
#cv2.imshow('buc anh cover',mask)

#cong 2 anh long ghe 2 anh
#img1 = cv2.imread('1.png',1)
#img2 = cv2.imread('5.png',1)
#img1 = img1[10:300,10:300]
#img2 = img2[10:300,10:300]
#print(img1.shape)
#print(img2.shape)
#img3 = cv2.addWeighted(img1,0.7,img2,0.3,0)
#cv2.imshow('image',img3)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

####################################lam viec voi matplotlib
#plt.scatter(4,5,500,'b','<') #ve 1 diem tren toa do
#plt.scatter(10,5,500,'r','<')
####################################learning cơ bản sử dụng KNearest_create
#newMember = np.random.randint(0,100,(1,2)).astype(np.float32)
#trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
#ketqua = np.random.randint(0,2,(25,1)).astype(np.float32)
#red = trainData[ketqua.ravel()==1]
#blu = trainData[ketqua.ravel()==0]
#plt.scatter(red[:,0],red[:,1],100,'r','<')
#plt.scatter(blu[:,0],blu[:,1],100,'b','s')
#plt.scatter(newMember[:,0],newMember[:,1],100,'g','o')

#knn = cv2.ml.KNearest_create()
#knn.train(trainData,0,ketqua)
#results = knn.findNearest(newMember,3)
print (results)
plt.show()