import cv2

# img1 = cv2.imread('images/cell-phone.jpg')
# img2 = cv2.imread('images/phone-gray.png')
img1 = cv2.imread('images/phone-gray.png')
img2 = cv2.imread('images/cell-phone.jpg')


#add = img1 + img2
#add = cv2.add(img1,img2)



# weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)
#
# img2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#
# cv2.imshow('weighted',weighted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('mask',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()