import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the image (assuming it's already grayscale)
# If it's not grayscale, convert it using cv2.imread('path_to_image', cv2.IMREAD_GRAYSCALE)
image = cv2.imread('images/dog.jpg', cv2.IMREAD_GRAYSCALE)

# Step 2: Define a function to calculate tf1 and tf2
def calculate_tf1_tf2(image, threshold):
    tf1 = np.sum(image <= threshold)  # Count of pixels less than or equal to the threshold
    tf2 = np.sum(image > threshold)   # Count of pixels greater than the threshold
    return tf1, tf2

# Step 3: Find the threshold where tf1 is near 2 * tf2
best_threshold = None
for threshold in range(256):
    tf1, tf2 = calculate_tf1_tf2(image, threshold)
    
    # Check to avoid division by zero when tf2 is 0
    if tf2 > 0:
        if tf1 / tf2 >= 2.0:  # Looking for tf1 being roughly 2 times tf2
            best_threshold = threshold
            break

# Step 4: Handle the case when no threshold satisfies the condition
if best_threshold is None:
    # Use a default threshold, like 128, or take the median intensity
    best_threshold = 128
    print("No threshold found satisfying tf1 ≈ 2 * tf2. Using default threshold of 128.")

# Step 5: Generate the binary image using the found threshold
binary_image = (image > best_threshold).astype(np.uint8) * 255

# Step 6: Display the binary image
plt.imshow(binary_image, cmap='gray')
plt.title(f'Binary Image (Threshold: {best_threshold})')
plt.show()
