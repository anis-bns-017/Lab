import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/dog2.jpg", cv2.IMREAD_GRAYSCALE)
histr = cv2.calcHist([img], [0], None, [256], [0, 256])
print(histr[1])
print(histr[0])
print(histr)

plt.plot(histr)
plt.show()