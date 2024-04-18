#เปิดวิดีโอด้วย OpenCV
import cv2 
import time
from datetime import datetime, timezone, timedelta


# cap = cv2.VideoCapture("image/Mark.mp4")
cap = cv2.VideoCapture("")

tz = timezone(timedelta(hours = 7))

prev_frame_time = 0
new_frame_time = 0

while (cap.isOpened()):
    check , frame = cap.read()
    if check :

        # start = time.time()
        # s = time.gmtime(start)
        # r_time = datetime.now(tz=tz)
        # s_time = r_time - timedelta(seconds=30)
        # seconds = r_time - s_time


        # show = cv2.putText(frame,f"{r_time.strftime('%Y-%m-%d %H:%M:%S')}",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)
        # show = cv2.putText(frame,f"{s_time.strftime('%Y-%m-%d %H:%M:%S')}",(100,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)

        new_frame_time = time.time()
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
        fps = str(int(fps))

        show = cv2.putText(frame,f"{fps}",(100,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)
        show = cv2.putText(frame,f"{prev_frame_time}",(100,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)
        show = cv2.putText(frame,f"{new_frame_time}",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)


        cv2.imshow("Output",show)
        if cv2.waitKey(24) & 0xFF == ord("e"):
            break
    else :
        break

# end = time.time()
# seconds = end - start
# fps = num_frames / seconds
# frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# print("Start:{}".format(start))
# print("End:{}".format(end))
# print("FPS:{}".format(fps))
# print("NUM_F:{}".format(num_frames))

cap.release()
cv2.destroyAllWindows()

