import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('images/elephant.png', cv2.IMREAD_GRAYSCALE)

half = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(img, (7000, 7000))

streach_near = cv2.resize(img, (700, 540), interpolation=cv2.INTER_LINEAR)

Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [img, half, bigger, streach_near]

count = 4;

for i in range(count): 
    plt.subplot(2, 2, i + 1)
    plt.table(Titles[i])
    plt.imshow(images[i])

plt.show()

