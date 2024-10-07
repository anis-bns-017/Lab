import cv2
import numpy as np

# Load the images
image1 = cv2.imread('images/dog.jpg')
image2 = cv2.imread('images/dog2.jpg')
image3 = cv2.imread('images/elephant.png')
image4 = cv2.imread('images/nature.png')

# Resize images to the same dimensions (optional)
width = 300
height = 300
image1_resized = cv2.resize(image1, (width, height))
image2_resized = cv2.resize(image2, (width, height))
image3_resized = cv2.resize(image3, (width, height))
image4_resized = cv2.resize(image4, (width, height))

# Merge images into a 2x2 grid
top_row = np.hstack((image1_resized, image2_resized))  # Concatenate horizontally
bottom_row = np.hstack((image3_resized, image4_resized))  # Concatenate horizontally
merged_image = np.vstack((top_row, bottom_row))  # Concatenate vertically

# Display the merged image
cv2.imshow('Merged Image', merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
