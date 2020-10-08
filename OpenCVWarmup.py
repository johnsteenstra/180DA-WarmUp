import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load a color image in greyscale
img = cv2.imread('eagle.jpg', 1) # 1- color, 0 - greyscale, -1 - unchanged
cv2.imshow('pre_image', img)
cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('post_image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Take a picture
cap = cv2.VideoCapture(0)
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Display the resulting frame
	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture with 'q'
cap.release()
cv2.destroyAllWindows()