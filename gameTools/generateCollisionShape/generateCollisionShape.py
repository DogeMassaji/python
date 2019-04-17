# -*- coding: UTF-8 -*-
import numpy
import cv2.cv2 as cv2
import os


def main():
    global src_path
    global tgt_path
    path = os.path.dirname(os.path.abspath(__file__))
    src_path = path + '\\src\\'
    tgt_path = path + '\\tgt\\'

    for src_file in os.listdir(src_path):
        f = os.path.join(src_path, src_file)
        if os.path.isdir(f) \
            or os.path.splitext(src_file)[1] != '.png':
            continue
        generateCollisionShape(f)


def generateCollisionShape(file):
    img = cv2.imread(file)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 1, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
                                                  cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    #epsilon = 0.1 * cv2.arcLength(cnt, True)
    approxs = [
        cv2.approxPolyDP(cnt, 0.1 * cv2.arcLength(cnt, True), True)
        for cnt in contours
    ]

    showApprox = cv2.polylines(img, approxs, 0, (0, 255, 0), 1)
    #showCnt = cv2.drawContours(img, contours, 0, (0, 255, 0), 1)

    while (1):
        #cv2.imshow('contours', showCnt)
        cv2.imshow('approx', showApprox)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
