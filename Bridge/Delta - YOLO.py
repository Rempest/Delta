from ultralytics import YOLO
import cv2
# new class to the YOLO intergration
class Delta_Vision:
  def __init__(self, model_path = 'yolov8n.pt'):
    self.model = YOLO(model_path)
# detection an objest
  def get_detection(self, frame):
    results = self.model(frame, verbose = False)[0]
    self.detection = []
# object's cycle to the detection array 
    for box in results.boxes:
      x1, y1, x2, y2 = map(int, box.xyxy[0])
      conf = float(box.conf[0])
      cls = int(box.cls[0])
      detection.append(x1, y1, x2, y2, conf, cls)
      return detecton
  # conditional if object is false
    def draw(self, frame, detection, target = None):
      for (x1, y1, x2, y2, conf, cls) in detection:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (100, 100, 100), 1)
      if target:
        x1, y1, x2, y2, conf, cls = target
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"TARGET {conf:.2f}",
        (x1, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
        return frame
      
