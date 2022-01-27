import cv2

def lagori_det(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]

    cnt, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    centers = []

    for c in cnt:
        approx = cv2.approxPolyDP(c, 0.04 * cv2.arcLength(c, True), True)

        if len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            center = (x + w / 2, y + h / 2)
            centers.append(center)

    return centers, thresh