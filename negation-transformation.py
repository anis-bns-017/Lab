import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/elephant.png", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

for i in range(rows): 
    for j in range(cols):
        img[i][j] = 255 - img[i][j]


image = cv2.resize(img, (700, 500))
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
