#!/usr/bin/env python3
import cv2
import time
from display import Display
from extractor import Extractor
import numpy as np

W = 1920/2
H = 1020/2

F = 1
display = Display(W, H)
K = np.array([[F,0,W//2], [0,F,H//2], [0,0,1]])
fe = Extractor(K)

def process_frame(img):
    # too much resolution so will have to resize
    img = cv2.resize(img, (W, H))
    matches = fe.extract(img)
    
    print("%d matches" % (len(matches)))

    for pt1, pt2 in matches:
        u1,v1 = fe.denormalize(pt1)
        u2,v2 = fe.denormalize(pt2)

        cv2.circle(img, (u1,v1), color=(0,255,0), radius=3)
        cv2.line(img, (u1,v1), (u2,v2), color=(255,0,0))


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
