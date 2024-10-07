import cv2
import numpy as np

# Create two binary images
img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

# Draw a white square on the first image
cv2.rectangle(img1, (50, 50), (250, 250), 255, -1)

# Draw a white circle on the second image
cv2.circle(img2, (150, 150), 100, 255, -1)

# Add the images
added_img = cv2.add(img1, img2)

# Subtract img2 from img1
subtracted_img = cv2.subtract(img1, img2)

# Display the results
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Added Image", added_img)
cv2.imshow("Subtracted Image", subtracted_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
