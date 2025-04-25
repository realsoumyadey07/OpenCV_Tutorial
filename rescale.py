import cv2 as cv

# img = cv.imread("photos/cat.jpeg")
# cv.imshow("Cat", img)

#change the size of the image
def rescaleFrame(frame, scale=0.2):
     width = int(frame.shape[1] * scale)
     height = int(frame.shape[0] * scale)
     dimensions = (width, height)

     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#change the resolution of the video
def changeResolution(width, height):
     capture.set(3, width)
     capture.set(4, height)
     

#reading videos
capture = cv.VideoCapture("videos/sea_coast.mp4")

while True:
     isTrue, frame = capture.read()
     frame_resize = rescaleFrame(frame)
     cv.imshow("Video", frame)
     cv.imshow("Video resized", frame_resize)
     if cv.waitKey(20) & 0xFF == ord('d'):
         break

capture.release()
cv.destroyAllWindows()
