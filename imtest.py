import cv2

img = cv2.imread('sea.jpg', 1)

cv2.imshow('Test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
