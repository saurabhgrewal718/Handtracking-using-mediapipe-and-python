import math
import cv2
import time
import numpy as np
import handtrackingModule as htm
import wmi

brightness = 40  # percentage [0-100] For changing thee screen
c = wmi.WMI(namespace='wmi')
methods = c.WmiMonitorBrightnessMethods()[0]
methods.WmiSetBrightness(brightness, 0)

#
# minVol = volrange[0]
# maxVol = volrange[1]

#
# detector = htm.handDetector(detectionCon=0.8)
# wCam,hCam = 1280,720
# cap = cv2.VideoCapture(0)
# cap.set(3,wCam)
# cap.set(4,hCam)
# pTime = 0
# vol=0
# volBar = 400
#
# while True:
#     success,img = cap.read()
#     cTime = time.time()
#     fps = 1/(cTime-pTime)
#     pTime = cTime
#     cv2.putText(img,str(int(fps)), (10,70),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,255),3)
#
#     img = detector.findHands(img)
#     lmList = detector.findPosition(img,draw=False)
#     if len(lmList) != 0:
#         x1,y1 = lmList[4][1],lmList[4][2]
#         x2,y2 = lmList[8][1],lmList[8][2]
#         cx,cy = (x1+x1)//2,(y1+y2)//2
#
#
#         cv2.circle(img,(x1,y1),15,(255,0,0),cv2.FILLED)
#         cv2.circle(img,(x2,y2),15,(255,0,0),cv2.FILLED)
#         cv2.line(img,(x1,y1),(x2,y2),(255,9,255),3)
#         cv2.circle(img,(cx,cy),15,(255,0,0),cv2.FILLED)
#         length = math.hypot(x2-x1,y2-y1)
#         # print(length)
#         #
#         # vol = np.interp(length,[16,150],[minVol,maxVol])
#         # volBar = np.interp(length,[16,150],[400,150])
#         # print(int(length),vol)
#         # volume.SetMasterVolumeLevel(vol, None)
#         # cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
#         # cv2.rectangle(img,(50,int(volBar)),(85,400),(0,255,0),cv2.FILLED)
#
#
#
#
#         if length<20:
#             cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
#         if length>140:
#             cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
#
#
#
#
#     cv2.imshow("IMG",img)
#     cv2.waitKey(1)