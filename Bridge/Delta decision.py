# DeltaDecision.py
class DeltaDecision:
    def __init__(self, frame_width=640, zone_margin=0.15):
        self.left_bound  = frame_width * (0.5 - zone_margin)  # ~272
        self.right_bound = frame_width * (0.5 + zone_margin)  # ~368

    def decide(self, scene_data):
        if scene_data is None:
            return "SEARCH"
        cx = scene_data["cx"]
        if cx < self.left_bound:
            return "LEFT"
        elif cx > self.right_bound:
            return "RIGHT"
        else:
            return "FORWARD"
