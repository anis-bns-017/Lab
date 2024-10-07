import cv2
img = cv2.imread("images/dog.jpg", cv2.IMREAD_GRAYSCALE)

filename = "images/dogs_copy.jpg"
v = cv2.imwrite(filename, img);

if v == True:
    print("Image has been saved")
else:
    print("Failed to save the image")