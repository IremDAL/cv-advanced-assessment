from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")  


    model.train(
        data="training/dataset.yaml",
        epochs=50,
        imgsz=640,
        batch=8,
        pretrained=True,
        workers=2,
        device="cpu",
        project="training/logs",
        name="yolo8-coco-subset",
    )


    model.export(format="onnx") 

if __name__ == "__main__":
    main()
