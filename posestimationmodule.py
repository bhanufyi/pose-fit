import cv2
import mediapipe as mp
import math

class PoseDetector:
    def __init__(self,
                 mode=False,
                 complexity=1,
                 smooth_landmarks=True,
                 enable_segmentation=False,
                 smooth_segmentation=True,
                 detection_confidence=0.5,
                 tracking_confidence=0.5):
        self.pose = mp.solutions.pose.Pose(
            static_image_mode=mode,
            model_complexity=complexity,
            smooth_landmarks=smooth_landmarks,
            enable_segmentation=enable_segmentation,
            smooth_segmentation=smooth_segmentation,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.drawing_utils = mp.solutions.drawing_utils
        self.lmList = []  # Initialize lmList as an instance attribute

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks and draw:
            self.drawing_utils.draw_landmarks(img, self.results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []  # Clear the lmList before populating it
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        return self.lmList

    def findAngle(self, img, p1, p2, p3, draw=True):
        if not self.lmList or len(self.lmList) <= max(p1, p2, p3):
            raise ValueError("Invalid landmarks for calculating angle. Ensure findPosition() is called first.")
        
        _, x1, y1 = self.lmList[p1]
        _, x2, y2 = self.lmList[p2]
        _, x3, y3 = self.lmList[p3]
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        angle = angle + 360 if angle < 0 else angle

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            for x, y in [(x1, y1), (x2, y2), (x3, y3)]:
                cv2.circle(img, (x, y), 10, (0, 0, 255), 2)
                cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 - 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        
        return angle
