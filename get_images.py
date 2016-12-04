import cv2 as cv
import time

capture = cv.CaptureFromCAM(0)

while True:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)
    cv.SaveImage('pic.jpg', img)
    if cv.WaitKey(10)==27:
        break
