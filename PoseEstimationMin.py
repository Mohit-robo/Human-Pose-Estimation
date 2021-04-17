import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils


cap = cv2.VideoCapture('Pexels Videos 2722910.mp4')
# cap = cv2.VideoCapture(0)
# cap.set(3,200)
# cap.set(4,200)
pTime =0
while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape
            print(id,lm)
            cx,cy=int(lm.x*w),int (lm.y*h)
            cv2.circle(img,(cx,cy),5,(0,0,100),cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime


    cv2.putText(img,str(int(fps)),(70,58),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(0,255,0),2)


    cv2.imshow("img",img)
    cv2.waitKey(1)