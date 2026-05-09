import logging

logger = logging.getLogger(__name__)

class DeltaDecision:
    def __init__(self, frame_width=640, zone_margin=0.15):
        self.left_bound  = frame_width * (0.5 - zone_margin)
        self.right_bound = frame_width * (0.5 + zone_margin)

    def decide(self, scene_data):
        if scene_data is None:
            return "SEARCH"

        cx = scene_data.get("cx")
        if cx is None:
            logger.error("scene_data missing 'cx' key")
            return "SEARCH"

        if cx < self.left_bound:
            return "LEFT"
        elif cx > self.right_bound:
            return "RIGHT"
        else:
            return "FORWARD"