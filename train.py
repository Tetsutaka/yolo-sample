from ultralytics import YOLO

def train_model(yaml_path, weight="yolov8n.pt", data_yaml="./data.yaml", epochs=200, imgsz=640):
    model = YOLO(yaml_path).load(weight)
    model.train(data=data_yaml, epochs=epochs, imgsz=imgsz)

def main():
    try:
        train_model("yolov8n.yaml")
    except BaseException as e:
        print(e)

# model = YOLO("yolov8n.yaml").load("yolov8n.pt")
# model.train(data="./data.yaml", epochs=200, imgsz=640)
# del model

# try:
#     model = YOLO("yolov8s.yaml").load("yolov8s.pt")
#     model.train(data="./data.yaml", epochs=200, imgsz=640)
#     del model
# except BaseException as e:
#     print(e)


# try:
#     model = YOLO("yolov8x.yaml").load("yolov8x.pt")
#     model.train(data="./data.yaml", epochs=200, imgsz=640)
#     del model
# except BaseException as e:
#     print(e)

# try:
#     model = YOLO("yolov8s-seg.yaml").load("yolov8s.pt")
#     model.train(data="./data.yaml", epochs=200, imgsz=640)
#     del model
# except BaseException as e:
#     print(e)
