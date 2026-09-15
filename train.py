from ultralytics import YOLO

if __name__ == "__main__":
  # Sahi active weights folder ka path dein jahan last.pt mojood hai
  model = YOLO(r"C:\content\drive\MyDrive\yolov8_runs\train\weights\last.pt")

  # Training resume karein
  model.train(
      data=r"C:\Users\NICAT\Desktop\aerialdataset\new_datasetaerial1\data.yaml",
      resume=True,
      device=0,
  )