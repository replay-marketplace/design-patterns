import cv2

image = cv2.imread('image.jpg')

# Apply grayscale filter

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the image

cv2.imwrite('gray_image.jpg', gray)