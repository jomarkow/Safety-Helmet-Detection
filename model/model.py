from ultralytics import YOLO

model = YOLO("D:/Documentos/REPOSITORIOS/HardHat/output/best.pt")

model.train(data="data.yaml", epochs=10) 
metrics = model.predict("D:/Documentos/REPOSITORIOS/HardHat/data/images/hard_hat_workers0.png")
path = model.export(format="onnx")