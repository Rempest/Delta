import cv2
from Bridge.Delta_YOLO import Delta_YOLO
from Bridge.Delta_YOLO_analyze import DeltaAnalyze
from Bridge.Delta_decision import DeltaDecision
from Delta_Sensors import DeltaSensors

class DeltaBrain:
    def __init__(self):
        self.yolo = Delta_YOLO()
        self.analyze = DeltaAnalyze()
        self.decision = DeltaDecision()
        self.sensors = DeltaSensors()

    def run(self, source=0):
        cap = cv2.VideoCapture(source)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            #1. YOLO
            detections = self.yolo.get_detection(frame)

            #2. ANALYZE
            target = self.analyze.select_target(detections)
            scene_data = self.analyze.get_scene_data(target)

            #3. DECISION
            decision = self.decision.decide(scene_data)

             #4. SENSORS OVERRIDE
            sensor_state = self.sensors.DeltaTen()
            if sensor_state == "STOP!":
                decision = "STOP"

            print("Decision:", decision)

            #5. DRAW
            frame = self.yolo.draw(frame, detections, target)

            cv2.imshow("DeltaBrain", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
