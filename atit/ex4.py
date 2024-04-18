# รูปแบบ img
# 0 สีเทา
# 1 ภาพสี
# -1 
import cv2

img = cv2.imread("image/cat.jpg",0)

imgresize = cv2.resize(img,(400,400))

cv2.imshow("Show", imgresize)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()