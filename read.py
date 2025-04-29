import cv2 as cv
import numpy as np
import os


img = cv.imread("photos/cat.jpeg") # Read the image
re_img = cv.resize(img, (300, 300))

# joining multiple images horizontally
h = np.hstack((re_img, re_img))
# joining multiple images vertically
v = np.vstack((h, h))
# print(img) # Print the image matrix
cv.imshow("Cat", v) # Display the image
cv.waitKey(0)
# cv.destroyAllWindows()
cv.destroyWindow("Cat") # Destroy the window

#getting all file names from the folder
list_name = os.listdir(f"F:\OpenCV_Tutorial\photos")
print(list_name)
for name in list_name:
     path = "F:\OpenCV_Tutorial\photos"
     img_name = path + "\\" + name 
     img = cv.imread(img_name)
     img = cv.resize(img, (300, 300))
     cv.imshow(name, img)
     cv.waitKey(1000)
     cv.destroyAllWindows()