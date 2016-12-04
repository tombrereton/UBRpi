# import the necessary packages
import picamera
import picamera.array
import time
import cv2
from hampy import detect_markers

# initialize the camera and grab a reference to the raw camera capture
camera = picamera.PiCamera()
rawCapture = picamera.array.PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

# display the image on screen and wait for a keypress
#cv2.imshow("Image", image)
cv2.imwrite("output.jpg", image)
cv2.waitKey(0)

# detect markers
markers = detect_markers(image)

print("Trying to detect markers...")

for m in markers:
   print 'Found marker {} at {}'.format(m.id, m.center)
   m.draw_contour(image)


cv2.imshow("Image_markers", image)
cv2.waitKey(0)
