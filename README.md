# Smart Aerial Vehicle Detection & Monitoring System (YOLOv8)

This repository contains the complete implementation of an aerial vehicle detection and monitoring system built using **YOLOv8**. The model is specifically trained to detect, localize, and classify multiple vehicle categories (Cars, Buses, and Heavy-Vehicles) from complex aerial and drone imagery.

---

## 📊 Visual Results & Inferences
*(Preview of the model's performance on real-world aerial imagery with high-confidence bounding box detections)*

### 1. Real-World Aerial Inference
> Bounding box predictions demonstrating robust detection on dense aerial traffic data with high confidence scores (>0.85–0.93). Check the `results/` folder in this repository for full-size visual outputs.

---

## 🚀 Project Overview
* **Model Framework:** YOLOv8 (Custom configured)
* **Training Duration:** 80 Epochs
* **Target Classes:** `car`, `bus`, `heavy-vehicle`
* **Performance Highlights:** Achieved strong validation metrics (Car mAP50: 83.3%, Bus: 67.6%, Heavy-Vehicle: 57.6%).

## 📦 System Dependencies & Requirements
To run this project successfully, ensure you have the following installed in your Python environment:
* **Python:** `3.8` or higher
* **Ultralytics (YOLOv8):** `ultralytics>=8.0.0`
* **OpenCV:** `opencv-python` (for image processing and bounding box rendering)
* **Pandas & NumPy:** For data handling and metric logging
* **PyTorch:** Compatible with your hardware (CUDA recommended for training/inference)

Install all core requirements via terminal:
```bash
pip install ultralytics opencv-python pandas numpy torch
