import cv2  # OpenCV library for computer vision (video capture, image display, drawing, etc.)

# Import custom modules that represent different parts of the AI pipeline
from Bridge.Delta_YOLO import Delta_YOLO              # Handles object detection (YOLO-based)
from Bridge.Delta_YOLO_analyze import DeltaAnalyze    # Processes detections and extracts meaning
from Bridge.Delta_decision import DeltaDecision       # Makes decisions based on analyzed data
from Delta_Sensors import DeltaSensors                # Reads external sensor input (e.g., safety override)


class DeltaBrain:
    """
    DeltaBrain is the central orchestrator of the system.
    It connects perception (YOLO), understanding (Analyze),
    decision-making (Decision), and real-world constraints (Sensors).

    Think of this class as the "brain" that continuously:
    1. Sees the world (camera input)
    2. Understands what it sees
    3. Decides what to do
    4. Applies safety overrides if needed
    5. Displays the result
    """

    def __init__(self):
        """
        Constructor initializes all major subsystems.
        Each subsystem is modular, allowing easy replacement or upgrades.
        """

        # YOLO-based object detection module
        # Responsible for detecting objects in each video frame
        self.yolo = Delta_YOLO()

        # Analysis module
        # Responsible for selecting important targets and extracting scene meaning
        self.analyze = DeltaAnalyze()

        # Decision-making module
        # Responsible for choosing an action based on analyzed data
        self.decision = DeltaDecision()

        # Sensor module
        # Responsible for reading real-world sensor data (e.g., emergency stop)
        self.sensors = DeltaSensors()

    def run(self, source=0):
        """
        Main loop of the system.

        Parameters:
        - source: video input source
            0 = default webcam
            or a video file path

        This function continuously processes video frames until stopped.
        """

        # Initialize video capture from the given source
        cap = cv2.VideoCapture(source)

        # Infinite loop to process frames continuously
        while True:

            # Read a frame from the video source
            ret, frame = cap.read()

            # If frame capture failed (e.g., end of video or camera disconnected)
            if not ret:
                break  # Exit the loop safely

            # ---------------------------------------------------------
            # 1. OBJECT DETECTION (YOLO)
            # ---------------------------------------------------------
            # Detect objects in the current frame
            # Output: list of detections (bounding boxes, classes, confidence, etc.)
            detections = self.yolo.get_detection(frame)

            # ---------------------------------------------------------
            # 2. ANALYSIS (UNDERSTANDING THE SCENE)
            # ---------------------------------------------------------

            # Select the most important object (target) from detections
            # Example: closest person, highest confidence object, etc.
            target = self.analyze.select_target(detections)

            # Extract structured information about the scene
            # Example: distance, position, movement, object type, etc.
            scene_data = self.analyze.get_scene_data(target)

            # ---------------------------------------------------------
            # 3. DECISION MAKING
            # ---------------------------------------------------------

            # Decide what action to take based on scene data
            # Example outputs: "MOVE_FORWARD", "TURN_LEFT", "STOP", etc.
            decision = self.decision.decide(scene_data)

            # ---------------------------------------------------------
            # 4. SENSOR OVERRIDE (SAFETY LAYER)
            # ---------------------------------------------------------

            # Read sensor state (e.g., obstacle sensors, emergency switches)
            sensor_state = self.sensors.DeltaTen()

            # If sensors detect a critical condition, override AI decision
            # This ensures safety always has higher priority than AI logic
            if sensor_state == "STOP!":
                decision = "STOP"  # Force stop regardless of AI decision

            # Output the final decision to console (for debugging/logging)
            print("Decision:", decision)

            # ---------------------------------------------------------
            # 5. VISUALIZATION (DRAW RESULTS)
            # ---------------------------------------------------------

            # Draw bounding boxes, labels, and target highlighting on frame
            frame = self.yolo.draw(frame, detections, target)

            # Display the processed frame in a window
            cv2.imshow("DeltaBrain", frame)

            # Wait for 1 millisecond for key press
            # If ESC key (ASCII 27) is pressed → exit loop
            if cv2.waitKey(1) & 0xFF == 27:
                break

        # ---------------------------------------------------------
        # CLEANUP (IMPORTANT!)
        # ---------------------------------------------------------

        # Release the video capture resource (camera/file)
        cap.release()

        # Close all OpenCV windows to free resources
        cv2.destroyAllWindows()
