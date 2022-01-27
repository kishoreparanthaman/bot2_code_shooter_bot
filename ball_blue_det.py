import cv2
import numpy as np


def nothing(x):
    pass


# blue_l = (110, 50, 50)
# blue_u = (130,255,255)
cv2.namedWindow('trackbar')
cv2.createTrackbar('l_h', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('l_s', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('l_v', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('u_h', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('u_s', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('u_v', 'trackbar', 0, 255, nothing)


def ball_blue_det(img):

    while True:
        blur = cv2.GaussianBlur(img, (7, 7), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        l_h = cv2.getTrackbarPos('l_h', 'trackbar')
        l_s = cv2.getTrackbarPos('l_s', 'trackbar')
        l_v = cv2.getTrackbarPos('l_v', 'trackbar')
        u_h = cv2.getTrackbarPos('u_h', 'trackbar')
        u_s = cv2.getTrackbarPos('u_s', 'trackbar')
        u_v = cv2.getTrackbarPos('u_v', 'trackbar')
        blue_l = np.array([l_h, l_s, l_v])
        blue_u = np.array([u_h, u_s, u_v])
        mask = cv2.inRange(hsv, blue_l, blue_u)
        # cv2.erode(mask, None, iterations=2)
        # cv2.dilate(mask, None, iterations=2)

        cv2.imshow('mask', mask)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('q'):
            cv2.destroyAllWindows()
            break

    # cnt, _ = cv2.findContours(
    #     mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # center = None

    # if len(cnt) > 0:
    #     c = max(cnt, key=cv2.contourArea)
    #     ((x, y), radius) = cv2.minEnclosingCircle(c)
    #     center = (int(x), int(y))

    # return center, mask
