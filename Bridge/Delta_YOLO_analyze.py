class DeltaAnalyze:
    def __init__(self, frame_width=640):
        self.frame_width = frame_width

    def select_target(self, detections):
        if not detections:
            return None

        return max(detections, key=lambda d: (d[2]-d[0]) * (d[3]-d[1]))

    def get_scene_data(self, target):
        if target is None:
            return None

        x1, y1, x2, y2, conf, cls = target

        return {
            "cx": (x1 + x2) // 2,
            "cy": (y1 + y2) // 2,
            "size": (x2 - x1) * (y2 - y1),
            "conf": conf,
            "cls": cls
        }
