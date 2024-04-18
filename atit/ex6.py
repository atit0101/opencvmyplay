import cv2

cap = cv2.VideoCapture("")

while (True):
    check, frame = cap.read()
    cv2.imshow("show",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()