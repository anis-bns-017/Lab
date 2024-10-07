import cv2
import numpy as np

# Create two binary images (for demonstration)
img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

# Draw a white square on the first image
cv2.rectangle(img1, (50, 50), (250, 250), 255, -1)

# Draw a white circle on the second image
cv2.circle(img2, (150, 150), 100, 255, -1)

# Perform bitwise AND operation
bitwise_and = cv2.bitwise_and(img1, img2)

# Perform bitwise OR operation
bitwise_or = cv2.bitwise_or(img1, img2)

# Perform bitwise XOR operation
bitwise_xor = cv2.bitwise_xor(img1, img2)

# Perform bitwise NOT operation (on img1)
bitwise_not = cv2.bitwise_not(img1)

# Show the results
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT", bitwise_not)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
