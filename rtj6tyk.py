import cv2

img1 = cv2.imread('3D-Matplotlib.jpg')
img2 = cv2.imread('mainsvmimage.png')



#add = img1 + img2
add = cv2.add(img1,img2)

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()