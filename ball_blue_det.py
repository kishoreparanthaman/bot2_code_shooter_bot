import cv2

blue_l = (80, 50, 0)
blue_u = (135,255,225)


def ball_blue_det(img):

    blur = cv2.GaussianBlur(img, (7, 7), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, blue_l, blue_u)
    cv2.erode(mask, None, iterations=2)
    cv2.dilate(mask, None, iterations=2)

    cnt, _ = cv2.findContours(
        mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    center = None

    if len(cnt) > 0:
        c = max(cnt, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))

    return center
