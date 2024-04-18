import cv2
import numpy

while True :
    img = cv2.imread("image/ball2d.jpg")
    img = cv2.resize(img,(400,400))

    if cv2.waitKey(0) & 0xFF == ord("e"):
        break

    cv2.imshow("Show",img)


cv2.destroyAllWindows()