import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('eagle.jpg', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
edge = cv2.Canny(frame, 100, 200)
	
plt.subplot(121), plt.imshow(frame, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edge, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()

