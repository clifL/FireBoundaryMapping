# Credit of this script goes to GR Tech School (https://www.youtube.com/watch?v=2uxfqlDbVV4&ab_channel=GRTechSchool)

import cv2
import numpy as np

# 0 - means web cam
video = cv2.VideoCapture("Videos\City1.mp4")

while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (1000,600))
    # Blurring the video which eliminates the noises
    blur = cv2.GaussianBlur(frame, (15,15), 0)
    # Get HSV colour of the blurred frame
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    # Declare Lower and Upper Bound of a fire characteristic
    lower = [18,50,50]
    upper = [35,255,255]

    # Apparently opencv cannot read the array data directly, it need to use numpy for data parsing
    lower = np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')
    # Detection (Basically, we are looking for these two types of colour inside the frame (In HSV format))
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(frame, hsv, mask=mask)
    number_of_total = cv2.countNonZero(mask)
    if int(number_of_total) > 15000:
        print("Fire Detected")

    if ret == False:
        break
    
    cv2.imshow("Output", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
video.release()