from ultralytics import YOLO
import cv2

class Delta_YOLO:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)

    def get_detection(self, frame):
        results = self.model(frame, verbose=False)[0]
        detections = []

        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])

            detections.append((x1, y1, x2, y2, conf, cls))

        return detections

    def draw(self, frame, detections, target=None):
        for (x1, y1, x2, y2, conf, cls) in detections:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (100, 100, 100), 1)

        if target:
            x1, y1, x2, y2, conf, cls = target
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"TARGET {conf:.2f}",
                        (x1, y1 - 8),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 1)

        return frame
