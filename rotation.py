import cv2
import numpy as np

# Load the image
image = cv2.imread('images/elephant.png')

# Get image dimensions
(h, w) = image.shape[:2]

# Calculate the center of the image
center = (w // 2, h // 2)

# Define the rotation angle and scale
angle = 180  # Rotate by 45 degrees
scale = 1.0

# Get the rotation matrix
M = cv2.getRotationMatrix2D(center, angle, scale)

# Perform the rotation
rotated_image = cv2.warpAffine(image, M, (w, h))

# Display the original and rotated images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
