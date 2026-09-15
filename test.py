from ultralytics import YOLO

if __name__ == "__main__":
  # Best weights load karein jo training ke baad save hue hain
  model = YOLO(r"C:/content/drive/MyDrive/yolov8_runs/train/weights/best.pt")

  # Apne test images wale folder ya kisi aik image ka path yahan dein
  results = model.predict(
      source=r"C:/Users/NICAT/Desktop/test images",  # Ya jo folder abhi aapne check kiya (770 images wala)
      conf=0.25,  # Confidence threshold (25% se oopar wale detections show honge)
      save=True,  # Detected images ko bounding boxes ke sath save karne ke liye
      imgsz=1024,  # Training wala image size
  )

  print(
      "Testing mukammal ho gayi! Results 'runs/detect/predict' folder mein save"
      " ho gaye hain."
  )