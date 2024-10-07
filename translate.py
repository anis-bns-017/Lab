import cv2
import numpy as np

# Load the image
image = cv2.imread('images/dog2.jpg')

# Define the translation matrix
tx, ty = 100, 50  # Translate 100 pixels right and 50 pixels down
M = np.float32([[1, 0, tx], [0, 1, ty]])

# Perform the translation
translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# Display the original and translated images
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
