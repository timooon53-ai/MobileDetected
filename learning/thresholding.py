import cv2

img = cv2.imread('images/bookpage.jpg')
# first_img = cv2.cvtColor(first_img, cv2.COLOR_BGR2GRAY)
"""вызывать, если изображение в формате RGB, если в формате BGR, то остается комментированным. Также необходимо в
    передаче first_img заменить на img"""

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
# 12 - пороговое значение, 255 - максимальное значение, передача аргумента first_img/img зависит от канальности изображения

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                             115, 1)
retval2, otsu = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)


cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
