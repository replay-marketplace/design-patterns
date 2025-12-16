import cv2

image = cv2.imread('image.jpg')

# Apply grayscale filter

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply blur filter

blur = cv2.GaussianBlur(gray, (5, 5), 0)