import math

import cv2
import mediapipe as mp
import time

import numpy as np

import contour
import object_size

from PyQt5.QtGui import QImage
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

def scapulaAP(self):
    ratio = contour.distance_measurement()
    scale = 1/(ratio*0.393701)

    mpDraw = mp.solutions.drawing_utils
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()

    #path = 'edited.jpg'
    demo = True
    if demo:
        cap = cv2.VideoCapture('pose5.mp4')
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
                    #cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                if id == 12:
                    p2 = (cx, cy)
                    #cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                if id == 21:
                    p3 = (cx, cy)
                    #cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                if id == 22:
                    p4 = (cx, cy)
                    #cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                if id == 23:
                    p5 = (cx, cy)
                    # cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
                if id == 24:
                    p6 = (cx, cy)
                    # cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        #cv2.line(img, p1, p2, (255, 0, 255), 2)
        #cv2.line(img, p3, p4, (255, 0, 255), 2)
        #cv2.line(img, p1, p3, (255, 0, 255), 2)
        #cv2.line(img, p2, p4, (255, 0, 255), 2)

        #scale = contour.distance_measurement()
        '''
        patient_lateral_width = math.dist(p1, p2)
        shoulder = round(patient_lateral_width/scale*2.54)
        cv2.putText(img, '{}cm'.format(shoulder), (p1[0] + 50 , p1[1] - 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                    (255, 0, 255), 2)
    
        '''
        xm = (p1[0] + p2[0])//2 - round(2*scale)
        cv2.line(img, (xm, 0), (xm, img.shape[0]), (0, 0, 255), 2)

        leftsh = p1[0] - xm
        rightsh = xm - p2[0]

        check = abs(leftsh - rightsh)

        '''
        if check > 0.05*(leftsh+rightsh):
            cv2.putText(img, 'Rotation', (1500, 50), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        else:
            cv2.putText(img, 'No Rotation', (1500, 50), cv2.FONT_HERSHEY_COMPLEX, 2,
                        (255, 255, 255), 2)
        '''

        #ym = (p1[1] + p3[1])//2
        #cv2.line(img, (0, ym), (img.shape[1], ym), (255, 255, 255), 2)

        ym1 = (p1[1] + round(2*scale))
        cv2.line(img, (0, ym1), (img.shape[1], ym1), (0, 0, 255), 2)


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)

        r1x = xm - round(6*scale)
        r1y = ym1 - round(8.5*scale)

        r2x = xm + round(6*scale)
        r2y = ym1 + round(8.5*scale)



        #shapes = cv2.rectangle(img, (r1x,r1y), (r2x,r2y), (242, 241, 74), cv2.FILLED)

        #out = img.copy()
        #alpha = 0.5
        #mask = shapes.astype(bool)
        #out[mask] = cv2.addWeighted(shapes, alpha, shapes, 1 - alpha, 0)[mask]

        x, y, w, h = 100, 100, 200, 100
        sub_img = img[r1y:r2y, r1x:r2x]
        white_rect = np.ones(sub_img.shape, dtype=np.uint8) * 255

        res = cv2.addWeighted(sub_img, 0.5, white_rect, 0.5, 1.0)

        img[r1y:r2y, r1x:r2x] = res
        #cv2.imshow("Image", img)
        #cv2.imshow('Res', res)
        #cv2.imshow('Output', out)
        cv2.waitKey(1)

        rgbImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgbImage.shape
        bytesPerLine = ch * w
        convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
        p = convertToQtFormat.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
        self.ImageUpdate.emit(p)
