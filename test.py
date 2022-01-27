import cv2
import imutils
# from lagori_det import lagori_det
from ball_blue_det import ball_blue_det
from ball_red_det import ball_red_det
from ball_green_det import ball_green_det

img = cv2.imread('ball.jpeg')
imutils.resize(img, width=400)
# cv2.imshow('img', img)

ball_blue_det(img)
# print(center)

# cv2.imshow('new_img', new_img)
# key = cv2.waitKey(0) & 0xFF
# if key == 'q':
#     cv2.destroyAllWindows()

# key = cv2.waitKey(0) & 0xFF
# if key == ord('q'):
#     cv2.destroyAllWindows()

