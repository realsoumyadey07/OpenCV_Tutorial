import cv2 as cv
import numpy as np

org_img = cv.imread("photos/cat.jpeg")
re_img = cv.resize(org_img, (400, 500))
#Gaussian blur
g = cv.GaussianBlur(re_img, (7, 7), 0)
#Median blur
m = cv.medianBlur(re_img, 5)
#Bilateral filter
b = cv.bilateralFilter(re_img, 10, 100, 100)
#box filter
blurred_image = cv.boxFilter(re_img, ddepth=-1, ksize=(5, 5), normalize=True)

h = np.hstack((re_img, g, m, b, blurred_image))
cv.imshow("Cat", h)
cv.waitKey(0)
cv.destroyAllWindows()