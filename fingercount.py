import cv2
import time
import os
import handtrackingModule as htm

wCam,hCam = 648,480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

folderpath = "fingers"
myList = os.listdir(folderpath)
print(myList)

detector = htm.handDetector(detectionCon=0.75)

overlay_list = []
for im in myList:
    image = cv2.imread(f'{folderpath}/{im}')
    overlay_list.append(image)
print("the len is : ",len(overlay_list))
pTime = 0

tipIds = [4,8,12,16,20]
while True:
    success,img = cap.read()
    img = detector.findHands(img)
    imlist = detector.findPosition(img,draw=False)

    if len(imlist) !=0:
        fingers = []
        if imlist[tipIds[0]][1] < imlist[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1,5):
            if imlist[tipIds[id]][2] < imlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)


        totalfingers = fingers.count(1)
        print(totalfingers)
        cv2.putText(img,f'{int(totalfingers)}',(400,100),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
        h,w,c = overlay_list[totalfingers].shape
        img[0:h,0:w] = overlay_list[totalfingers]
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,f'FPS : {int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow('Image',img)
    cv2.waitKey(1)