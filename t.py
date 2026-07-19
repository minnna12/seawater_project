import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    h, w, _ = frame.shape

    if results.multi_hand_landmarks:
        for hand_idx, hand_landmarks in enumerate(results.multi_hand_landmarks):

            # 관절 좌표 출력
            for idx, lm in enumerate(hand_landmarks.landmark):
                cx = int(lm.x * w)
                cy = int(lm.y * h)

                print(
                    f"Hand:{hand_idx} "
                    f"Joint:{idx} "
                    f"X:{cx} Y:{cy} Z:{lm.z:.4f}"
                )

                cv2.circle(frame, (cx, cy), 4, (0, 255, 0), -1)

            # 손 뼈대 그리기
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
