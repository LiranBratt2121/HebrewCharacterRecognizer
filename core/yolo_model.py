from ultralytics import YOLO

class YoloModel:
    def __init__(self, model_weights="weights/best.pt") -> None:
        self.model = YOLO(model_weights)

    def predict_class(self, image_path: str, conf=0.2) -> str:
        result = self.model.predict(source=image_path, conf=conf, verbose=False, max_det=1)[0]
        class_name = result.names.get(result.boxes.cls[0].item(), 'Unknown')
        return class_name
