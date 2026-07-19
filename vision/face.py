import cv2
import mediapipe as mp


class FaceDetector:
    def __init__(self):
        self.mp_face = mp.solutions.face_detection
        self.mp_draw = mp.solutions.drawing_utils

        self.face_detection = self.mp_face.FaceDetection(
            model_selection=0,
            min_detection_confidence=0.5
        )

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.face_detection.process(rgb)

        face_boxes = []

        if result.detections:
            h, w, _ = frame.shape

            for detection in result.detections:
                bbox = detection.location_data.relative_bounding_box

                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                width = int(bbox.width * w)
                height = int(bbox.height * h)

                face_boxes.append({
                    "x": x,
                    "y": y,
                    "w": width,
                    "h": height
                })

        return result, face_boxes

    def draw(self, frame, result):
        if result.detections:
            for detection in result.detections:
                self.mp_draw.draw_detection(frame, detection)

        return frame

    def close(self):
        self.face_detection.close()
