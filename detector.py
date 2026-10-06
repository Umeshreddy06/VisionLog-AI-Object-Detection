import cv2
import time
from collections import defaultdict
from ultralytics import YOLO

class ObjectDetector:
    """Modular YOLO detector with class and confidence filtering."""

    def __init__(self, model_path="yolov8n.pt", confidence=0.70, selected_classes=None):
        self.model = YOLO(model_path)
        self.confidence = float(confidence)
        self.selected_classes = selected_classes or []
        self.class_names = self.model.names

    def set_config(self, confidence=None, selected_classes=None):
        if confidence is not None:
            self.confidence = float(confidence)
        if selected_classes is not None:
            self.selected_classes = selected_classes

    def detect(self, frame):
        results = self.model.predict(source=frame, conf=self.confidence, verbose=False)
        annotated = frame.copy()
        detections = []

        if not results or results[0].boxes is None:
            return annotated, detections

        for box in results[0].boxes:
            cls_id = int(box.cls[0].item())
            confidence = float(box.conf[0].item())
            name = self.class_names[cls_id]

            if self.selected_classes and name not in self.selected_classes:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            w, h = max(0, x2-x1), max(0, y2-y1)

            cv2.rectangle(annotated, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(
                annotated, f"{name} {confidence:.0%}",
                (x1, max(25,y1-8)), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (0,255,0), 2
            )

            detections.append({
                "object_class": name,
                "confidence": confidence,
                "bbox_x": x1,
                "bbox_y": y1,
                "bbox_w": w,
                "bbox_h": h,
            })

        return annotated, detections

class DetectionLogger:
    def __init__(self, cooldown_seconds=1.0):
        self.cooldown_seconds = cooldown_seconds
        self.last_logged = defaultdict(float)

    def should_log(self, detection):
        now = time.time()
        key = detection["object_class"]
        if now - self.last_logged[key] >= self.cooldown_seconds:
            self.last_logged[key] = now
            return True
        return False
