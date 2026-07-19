import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self, max_num_hands=2):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            max_num_hands=max_num_hands,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        hand_points = []

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                points = []

                for idx, lm in enumerate(hand_landmarks.landmark):
                    points.append({
                        "id": idx,
                        "x": lm.x,
                        "y": lm.y,
                        "z": lm.z
                    })

                hand_points.append(points)

        return result, hand_points

    def draw(self, frame, result):
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

        return frame

    def close(self):
        self.hands.close()
