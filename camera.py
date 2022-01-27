from lagori_det import lagori_det
from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import time
from ball_green_det import ball_green_det
from ball_blue_det import ball_blue_det
from ball_red_det import ball_red_det
from lagori_det import lagori_det

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    image = frame.array

    center_green = ball_green_det(image)
    center_red = ball_red_det(image)
    center_blue = ball_blue_det(image)

    centers_lagori = lagori_det(image)

    rawCapture.truncate(0)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
