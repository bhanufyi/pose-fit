import cv2
import mediapipe as mp


cap = cv2.VideoCapture("videos/bicep.mp4")

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

while True:
      ret, frame = cap.read()
      if ret:
          frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          results = pose.process(frameRGB)
          lmList = []
          if results.pose_landmarks:
              mpDraw.draw_landmarks(frame,results.pose_landmarks, mpPose.POSE_CONNECTIONS)
              for _id, lm in enumerate(results.pose_landmarks.landmark):
                  h,w,c = frame.shape
                  cx, cy = int(lm.x * w), int(lm.y * h)
                  lmList.append([_id, cx, cy])
                   #cv2.circle(frame, (cx, cy), 5, (255,0,255), cv2.FILLED)
                  print(_id,lm)
              cv2.circle(frame, (lmList[14][1], lmList[14][2]), 5, (255,0,255), cv2.FILLED)
          cv2.imshow("Video", frame)
          # cv2 reads in BGR and we need RGB for mediapipe
          if cv2.waitKey(1) & 0xFF == ord('1'):
              break
      else:
          break