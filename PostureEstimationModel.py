import cv2
import numpy as np
import mediapipe as mp
from src import calculate_angle as ca
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)
counter = 0
stage = None
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        try:
            landmarks = results.pose_landmarks.landmark
            shoulder_left = [
                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
            ]
            elbow_left = [
                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
            ]
            wrist_left = [
                landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y
            ]
            shoulder_right = [
                landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y
            ]
            elbow_right = [
                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y
            ]
            wrist_right = [
                landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y
            ]
            angle_left = ca.calculate_angle(shoulder_left, elbow_left, wrist_left)
            angle_right = ca.calculate_angle(shoulder_right, elbow_right, wrist_right)
            cv2.putText(image,
                        str(angle_left),
                        tuple(np.multiply(elbow_left, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2,
                        cv2.LINE_AA)
            cv2.putText(image,
                        str(angle_right),
                        tuple(np.multiply(elbow_right, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2,
                        cv2.LINE_AA)
            if angle_left > 160 and angle_right > 160:
                stage = 'down'
            if (angle_left < 35 or angle_right < 35) and stage == 'down':
                stage = 'up'
                counter += 1
        except:
            pass
        mp_drawing.draw_landmarks(image,
                                  results.pose_landmarks,
                                  mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66),
                                                         thickness=2,
                                                          circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245, 66, 230),
                                                         thickness=2,
                                                         circle_radius=2))
        cv2.imshow('Posture Estimation', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()