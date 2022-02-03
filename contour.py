import cv2
import numpy as np

def getContours(img, cThr=[100,100],showCanny=True,minArea = 1000,filter=0,draw=False):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, cThr[0],cThr[1])
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel, iterations=3)
    imgThre = cv2.erode(imgDial,kernel, iterations=2 )
    if showCanny:  cv2.imshow('Canny', imgThre)

    contours, hierarchy = cv2.findContours(imgThre,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    finalContours = []
    for i in contours:
        area = cv2.contourArea(i);
        #print(area)
        if area > minArea:
            peri = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02*peri,True)
            bbox = cv2.boundingRect(approx)

            if filter>0:
                if len(approx) == filter:
                    finalContours.append((len(approx), area, approx, bbox, i))
            else:
                finalContours.append((len(approx), area, approx, bbox, i))
    finalContours = sorted(finalContours, key = lambda x:x[1],reverse=True)

    if draw:
        for con in finalContours:
            cv2.drawContours(img,con[4],-1,(0,0,255),3)

    return img, finalContours

def reorder(myPoints):
    # print(myPoints.shape)
    myPointsNew = np.zeros_like(myPoints)
    myPoints = myPoints.reshape((4, 2))
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1]= myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew
def warpImg(img, points, w, h, pad=20):
    # print(points)
    points = reorder(points)
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarp = cv2.warpPerspective(img, matrix, (w, h))
    imgWarp = imgWarp[pad:imgWarp.shape[0]-pad,pad:imgWarp.shape[1]-pad]
    return imgWarp

def findDis(pts1,pts2):
    return ((pts2[0] - pts1[0])**2 + (pts2[1] - pts1[1])**2)**0.5

def distance_measurement():
    webcam = False
    path = 'pose5.jpg'
    cap = cv2.VideoCapture(0)
    cap.set(10,160)
    cap.set(3,1920) #1600
    cap.set(4,1080) #1200
    scale = 1
    #wP = 210*scale
    #hP = 297*scale

    #cap = cv2.VideoCapture('pose3.mp4')

    while True:
        #if webcam: success, img = cap.read()
        #else: img = cv2.imread(path)

        #success, img = cap.read()
        img = cv2.imread(path)

        imgContours, conts = getContours(img, minArea=3000, filter=4, cThr=[20,50], draw=False)
        if len(conts) != 0:
            #for obj in conts:
            obj = conts[0]
            cv2.polylines(imgContours, [obj[2]], True, (0, 255, 0), 2)
            nPoints = reorder(obj[2])
            ref_Length = findDis(nPoints[0][0], nPoints[2][0])
            scale = 29.7/ref_Length
            #print(ref_Length)
            print(scale)

            a4_width = round(findDis(nPoints[0][0], nPoints[1][0])*scale)
            a4_height = round(findDis(nPoints[0][0], nPoints[2][0]) * scale)
            #print(find_length)
            cv2.arrowedLine(img, (nPoints[0][0][0],nPoints[0][0][1]),(nPoints[1][0][0],nPoints[1][0][1]), (255,0,255),3,8,0,0.05)
            cv2.arrowedLine(img, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                            (255, 0, 255), 3, 8, 0, 0.05)
            x,y,w,h = obj[3]
            cv2.putText(img,'{}cm'.format(a4_width), (x+30, y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL,1, (255,0,255), 2)
            cv2.putText(img, '{}cm'.format(a4_height), (x - 70, y + h//2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                        (255, 0, 255), 2)

        #cv2.imshow('Warp', imgContours)
        # print(conts)

        """
        if len(conts) !=0 :
            print("Success")
            biggest = conts[0][0]
            #print(biggest)
            #imgWarp = warpImg(img,biggest,wP,hP)
            #cv2.imshow('Warp',imgWarp)
            imgContours2, conts2 = getContours(img, minArea=1000, filter=4, cThr=[50,50], draw=True)
            if len(conts)!=0:
                for obj in conts2:
                    cv2.polylines(imgContours2,[obj[2]], True, (0,255,0),  2)
            cv2.imshow('Warp', imgContours)
            """
        cv2.imshow('Original', img)
        cv2.waitKey(1)

        return scale

