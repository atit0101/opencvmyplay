import tensorflow_hub as hub
import cv2
import numpy
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("")
width = 1028
height = 1028


if (cap.isOpened() == False):
    print("Error opening video")

# inp = cv2.resize(cap, (width , height ))

rgb = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)

# COnverting to uint8
rgb_tensor = tf.convert_to_tensor(rgb, dtype=tf.uint8)

#Add dims to rgb_tensor
rgb_tensor = tf.expand_dims(rgb_tensor , 0)

# while(cap.isOpened()):
#     ret, frame = cap.read()
    
#     if ret == True:
#         cv2.imshow('video',rgb)

#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
#     else: 
#         break

# cap.release()
# cv2.destroyAllWindows()
