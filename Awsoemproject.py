import cv2
import time
import PoseModule as pm



cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.poseDetection()

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList)!=0:
        print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (150, 0, 0), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 58), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0, 255, 0), 2)

    cv2.imshow("img", img)
    cv2.waitKey(1)
