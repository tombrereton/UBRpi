import sys
import cv2
from hampy import detect_markers

img = cv2.imread('output.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('image_orginal', img)

markers = detect_markers(img)

for m in markers:
    print 'Found marker {} at {}'.format(m.id, m.center)
    m.draw_contour(img)

cv2.imshow('image', img)

