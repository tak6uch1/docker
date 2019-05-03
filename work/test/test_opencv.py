import numpy as np
import cv2
import matplotlib.pyplot as plt

#%matplotlib inline
RESIZEX = 300
RESIZEY = 400

img = cv2.imread('../img/sample/dedenne.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (RESIZEX, RESIZEY))
blr = cv2.blur(img, (5, 5))
edg = cv2.Canny(blr, 50, 80)

plt.subplot(1, 3, 1), plt.imshow(img)
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(blr)
plt.title('Blur'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(edg, cmap = 'gray')
plt.title('Edge'), plt.xticks([]), plt.yticks([])
plt.show()
