# show img

import cv2

img = cv2.imread("image/cat.jpg")

cv2.imshow("Show", img)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()