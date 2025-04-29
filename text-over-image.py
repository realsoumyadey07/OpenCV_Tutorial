import cv2 as cv

img_get = cv.imread("photos/cat.jpeg") 
img_get = cv.resize(img_get, (400, 500))
text = "Hello World"
org = (100, 100)
fontFace = cv.FONT_HERSHEY_DUPLEX
fontScale = 1
fontColor = (255, 0, 0)
thickness = 2

txt = cv.putText(img_get, "Cat", org, fontFace, fontScale, fontColor, thickness)
cv.imshow("Cat", img_get)
cv.waitKey(0)
cv.destroyWindow() 