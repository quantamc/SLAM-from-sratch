#!/usr/bin/env python3
import cv2
import time
from display import Display

W = 1920/2
H = 1020/2

display = Display(W, H)

def process_frame(img):
    # too much resolution so will have to resize
    img = cv2.resize(img, (W, H))
    display.paint(img)


if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")

    while cap.isOpened():
        ret, frame  = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break




#print("hello world") 