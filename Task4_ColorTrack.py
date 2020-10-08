import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#This video loop is a slightly modified version of the code found in the 
# 'Changing Colorspaces' tutorial found on the OpenCV website
while(1):

	#Take each frame
	_, frame = cap.read()

	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# define range of yellow color in HSV
	lower_yellow = np.array([20, 100, 100])
	upper_yellow = np.array([40, 255, 255])

	#Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
	
	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame, frame, mask = mask)

	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#ret, thresh = cv2.threshold(gray, 127, 255, 0)
	#contours, hierarchy = cv2.findContours(thresh, 1, 2)
	#cnt = contours[0]
	#M = cv2.moments(cnt)
	#rect = cv2.minAreaRect(cnt)
	#box = cv2.boxPoints(rect)
	#box = np.int0(box)
	#gray = cv2.drawContours(gray, [box], 0, (0, 0, 255), 2)

	#cv2.imshow('contour', gray)
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()