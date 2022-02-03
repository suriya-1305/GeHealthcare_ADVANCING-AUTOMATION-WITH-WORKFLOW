import math

import cv2
import mediapipe as mp
import time

import numpy as np
from PyQt5.QtGui import QImage
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

import contour
import object_size

def chestPA(self):
    demo = True
    scale = object_size.pixelRet('edited.jpg', 8.3)
    #scale = object_size.pixelRet('pose6.jpg', 8.3)

    mpDraw = mp.solutions.drawing_utils
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()

    #path = 'edited.jpg'
    if demo:
        cap = cv2.VideoCapture('pose3.mp4')
    #cap = cv2.VideoCapture('pose6.mp4')
    else:
        cap = cv2.VideoCapture(0)
    pTime = 0
    while True:
        success, img = cap.read()
        #img = cv2.imread(path)
        if img is None:
            break
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        # print(results.pose_landmarks.landmark[1])
        if results.pose_landmarks:
            # mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 11:
                    p1 = (cx, cy)
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                if id == 12:
                    p2 = (cx, cy)
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                if id == 21:
                    p3 = (cx, cy)
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                if id == 22:
                    p4 = (cx, cy)
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                if id == 23:
                    p5 = (cx, cy)
                    # cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
                if id == 24:
                    p6 = (cx, cy)
                    # cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        cv2.line(img, p1, p2, (255, 0, 255), 2)
        cv2.line(img, p3, p4, (255, 0, 255), 2)
        cv2.line(img, p1, p3, (255, 0, 255), 2)
        cv2.line(img, p2, p4, (255, 0, 255), 2)

        #scale = contour.distance_measurement()
        patient_lateral_width = math.dist(p1, p2)
        shoulder = round(patient_lateral_width/scale*2.54)
        cv2.putText(img, '{}cm'.format(shoulder), (p1[0] + 50 , p1[1] - 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                    (255, 0, 255), 2)

        xm = (p1[0] + p2[0])//2
        cv2.line(img, (xm, 0), (xm, img.shape[0]), (255, 255, 255), 2)

        leftsh = (xm - p1[0 ])/scale
        rightsh = (p2[0] - xm)/scale

        #print(leftsh)
        #print(rightsh)
        check = abs(leftsh - rightsh)

        if check > 0.05*(leftsh+rightsh):
            cv2.putText(img, 'Rotation', (1500, 50), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        else:
            cv2.putText(img, 'No Rotation', (1500, 50), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)

        cv2.putText(img, 'SID : 72 in', (1500, 150), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 255, 255), 2)

        #ym = (p1[1] + p3[1])//2
        #cv2.line(img, (0, ym), (img.shape[1], ym), (255, 255, 255), 2)

        ym1 = (p1[1] + round(5*scale))
        cv2.line(img, (0, ym1), (img.shape[1], ym1), (0, 255, 0), 2)

        cv2.putText(img, 'T7', (50, ym1 - 50), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 255, 255), 2)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)


        chestwidth = round(0.8*shoulder)

        if chestwidth >= 14 and chestwidth <16:
            cv2.putText(img, 'kVp : 85', (1500, 250), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
            cv2.putText(img, 'mAs : 4', (1500, 350), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        elif chestwidth >= 16 and chestwidth <18:
            cv2.putText(img, 'kVp : 85', (1500, 250), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
            cv2.putText(img, 'mAs : 6', (1500, 350), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        elif chestwidth >= 18 and chestwidth <20:
            cv2.putText(img, 'kVp : 85', (1500, 250), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
            cv2.putText(img, 'mAs : 8', (1500, 350), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        elif chestwidth >= 20 and chestwidth <22:
            cv2.putText(img, 'kVp : 100', (1500, 250), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
            cv2.putText(img, 'mAs : 2', (1500, 350), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        elif chestwidth >= 22 and chestwidth <24:
            cv2.putText(img, 'kVp : 100', (1500, 250), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
            cv2.putText(img, 'mAs : 3', (1500, 350), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        elif chestwidth >= 24 and chestwidth <26:
            cv2.putText(img, 'kVp : 100', (1500, 250), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
            cv2.putText(img, 'mAs : 4', (1500, 350), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        elif chestwidth >= 26 and chestwidth <28:
            cv2.putText(img, 'kVp : 110', (1500, 250), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
            cv2.putText(img, 'mAs : 6', (1500, 350), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        elif chestwidth >= 28 and chestwidth <30:
            cv2.putText(img, 'kVp : 110', (1500, 250), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
            cv2.putText(img, 'mAs : 9', (1500, 350), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        elif chestwidth >= 30 and chestwidth <32:
            cv2.putText(img, 'kVp : 110', (1500, 250), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
            cv2.putText(img, 'mAs : 12', (1500, 350), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        elif chestwidth >= 32 and chestwidth <34:
            cv2.putText(img, 'kVp : 110', (1500, 250), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
            cv2.putText(img, 'mAs : 18', (1500, 350), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        elif chestwidth >= 34:
            cv2.putText(img, 'kVp : 110', (1500, 250), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
            cv2.putText(img, 'mAs : 24', (1500, 350), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)


        '''
        shapes = np.zeros_like(img, np.uint8)
        cv2.rectangle(img, p1, p4, (242, 241, 74), cv2.FILLED)
    
        out = img.copy()
        alpha = 0.2
        mask = shapes.astype(bool)
        out[mask] = cv2.addWeighted(img, alpha, shapes, 1 - alpha, 0)[mask]
    
        '''

        r1x = xm - round(7 * scale)
        r1y = ym1 - round(8.5 * scale)

        r2x = xm + round(6 * scale)
        r2y = ym1 + round(8.5 * scale)
        x, y, w, h = 100, 100, 200, 100
        sub_img = img[r1y:r2y, r1x:r2x]
        white_rect = np.ones(sub_img.shape, dtype=np.uint8) * 255

        res = cv2.addWeighted(sub_img, 0.5, white_rect, 0.5, 1.0)

        img[r1y:r2y, r1x:r2x] = res

        #cv2.imshow("Image", img)
        #cv2.imshow('Shapes', shapes)
        #cv2.imshow('Output', out)
        cv2.waitKey(1)

        rgbImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgbImage.shape
        bytesPerLine = ch * w
        convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
        p = convertToQtFormat.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
        self.ImageUpdate.emit(p)
