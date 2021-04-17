import cv2
import mediapipe as mp
import time



# cap = cv2.VideoCapture(0)
# cap.set(3,200)
# cap.set(4,200)
class poseDetection():

    def  __init__(self,mode = False,upBody =False,smooth =  True,detectionCon = 0.5,trackCon = 0.5):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findPose(self,img,draw =True):

        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)

        return img
    def findPosition(self,img,draw = True):
        lmList = []
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                # print(id,lm)
                cx,cy=int(lm.x*w),int (lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),5,(0,0,100),cv2.FILLED)
        return lmList




def main():
    cap = cv2.VideoCapture('Pexels Videos 2722910.mp4')
    pTime =0
    detector = poseDetection()

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img,draw=False)
        if len(list)!=0:
            print(lmList[14])
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (150, 0, 0), cv2.FILLED)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 58), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0, 255, 0), 2)

        cv2.imshow("img", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()























