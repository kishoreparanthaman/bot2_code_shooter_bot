import cv2
import imutils
# from lagori_det import lagori_det
from ball_blue_det import ball_blue_det
from ball_red_det import ball_red_det
from ball_green_det import ball_green_det

img = cv2.imread('ball.jpeg')
img = imutils.resize(img, width=500)

center_green = ball_green_det(img)
center_red = ball_red_det(img)
center_blue = ball_blue_det(img)
print(center_red, center_green, center_blue)

cv2.imshow('img', img)
key = cv2.waitKey(0) & 0xFF
if key == 'q':
    cv2.destroyAllWindows()

