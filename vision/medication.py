class MedicationDetector:
    def __init__(self):
        pass

    def detect(self, frame):
        h, w, _ = frame.shape

        center_x = w // 2
        center_y = h // 2

        medication_box = {
            "x": center_x - 50,
            "y": center_y - 50,
            "w": 100,
            "h": 100,
            "center": (center_x, center_y)
        }

        return medication_box

    def draw(self, frame, medication_box):
        import cv2

        x = medication_box["x"]
        y = medication_box["y"]
        w = medication_box["w"]
        h = medication_box["h"]
        center = medication_box["center"]

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.circle(frame, center, 6, (0, 0, 255), -1)
        cv2.putText(frame, "Medication", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        return frame
