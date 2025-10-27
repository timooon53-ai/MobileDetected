import cv2
image = cv2.imread("images/cell-phone.jpg")

if image is not None:
    for i in range(10):
        cv2.imshow("Image", image)
        cv2.waitKey(1000)