import cv2
import time
import numpy as np
import posestimationmodule as pm

# Constants
BAR_COLOR_DEFAULT = (255, 100, 100)
BAR_COLOR_UP = (100, 255, 100)
BAR_COLOR_DOWN = (100, 100, 255)
FPS_POSITION = (30, 60)
COUNTER_POSITION = (30, 450)

# Initialize variables
cap = cv2.VideoCapture("videos/bicep.mp4")
detector = pm.PoseDetector()
count = 0
direction = 0
previous_time = 0


def draw_text_with_background(
    img,
    text,
    pos,
    font=cv2.FONT_HERSHEY_PLAIN,
    scale=3,
    color=(255, 255, 255),
    bg_color=(0, 255, 0),
    thickness=3,
):
    """Utility function to draw text with a rectangle background."""
    x, y = pos
    (w, h), _ = cv2.getTextSize(text, font, scale, thickness)
    offset = 10
    x1, y1 = x - offset, y + offset
    x2, y2 = x + w + offset, y - h - offset
    cv2.rectangle(img, (x1, y1), (x2, y2), bg_color, cv2.FILLED)
    cv2.putText(img, text, (x, y), font, scale, color, thickness)


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Pose Detection
    frame = detector.findPose(frame)
    lmList = detector.findPosition(frame, draw=False)
    if lmList:
        # Calculate Angle
        angle = detector.findAngle(frame, 12, 14, 16, draw=True)
        progress = np.interp(angle, (190, 300), (0, 100))
        bar_position = np.interp(angle, (190, 300), (650, 100))
        bar_color = BAR_COLOR_DEFAULT

        # Update Counter and Direction
        if progress == 100 and direction == 0:
            count += 0.5
            direction = 1
            bar_color = BAR_COLOR_UP
        elif progress == 0 and direction == 1:
            count += 0.5
            direction = 0
            bar_color = BAR_COLOR_DOWN

        # Display Counter
        draw_text_with_background(frame, str(int(count)), COUNTER_POSITION, scale=10)

        # Display Progress Bar
        cv2.rectangle(frame, (1100, 100), (1175, 650), bar_color, 3)
        cv2.rectangle(
            frame, (1100, int(bar_position)), (1175, 650), bar_color, cv2.FILLED
        )
        cv2.putText(
            frame,
            f"{int(progress)}%",
            (1100, 75),
            cv2.FONT_HERSHEY_PLAIN,
            4,
            bar_color,
            4,
        )

    # Calculate and Display FPS
    current_time = time.time()
    fps = 1 / (current_time - previous_time) if previous_time > 0 else 0
    previous_time = current_time
    draw_text_with_background(frame, f"FPS: {int(fps)}", FPS_POSITION)

    # Show Frame
    cv2.imshow("Bicep Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord("1"):
        break

cap.release()
cv2.destroyAllWindows()
