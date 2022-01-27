from distutils.log import error
from email.policy import default
from argparse import ArgumentParser
import cv2
import time

from sqlalchemy import true
import picamera
from picamera.array import PiRGBArray
import argparse
import imutils
from collections import deque


tolerance=17
X_lock=0
Y_lock=0

colorUpper=(44,255,255)
colorLower=(24,100,100)

ap=argparse ArgumentParser()          #openCv initialization
ap.add_argument("-b","--buffer",type=int,default=64,help="max buffer size")

args=vars(ap.parse_args())
pts=deque(maxlen=args["buffer"])


camera=picamera.PiCamera()
camera.resolution=(640,480)
camera.framerate=20
rawCapture=PiRGBArray(camera,size=(640,480))

for frame in camera.capture_continous(rawCapture,format="bgr",use_video_port=True):
    frame_image=frame.array

    hsv=cv2.cvtColor(frame_image,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,colorLower,colorUpper)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts)>0:
        c=max(cnts,key=cv2.contourArea)
        ((X,Y),radius)=cv2.minEnclosingCircle(c)

        if Y<(240-tolerance):
            error=(240-Y)/5
            #print(`up (error:%d)`%(error))
            Y_lock=0
        elif Y>(240+tolerance):
            error=(Y-240)/5
            Y_lock=0
        else:
            Y_lock=1
        
        if X<(320-tolerance):
            error=(320-X)/5
            X_lock=0
        elif X>(320+tolerance):
            error=(X-240)/5
            X_lock=0
        else:
            X_lock=1
        
        if X_lock==1 and Y_lock==1:
            print('locked:Fire!')
        else:
            print('detected but not locked:Hold!')
            pass
    
    rawCapture.truncate(0)


