# Smart Aerial Vehicle Detection & Monitoring System (YOLOv8)

This repository contains the complete implementation of an aerial vehicle detection and monitoring system built using **YOLOv8**. The model is specifically trained to detect, localize, and classify multiple vehicle categories (Cars, Buses, and Heavy-Vehicles) from complex aerial and drone imagery.

## 🚀 Project Overview
* **Model Framework:** YOLOv8 (Custom configured)
* **Training Duration:** 80 Epochs
* **Target Classes:** `car`, `bus`, `heavy-vehicle`
* **Performance Highlights:** Achieved strong validation metrics and high-confidence bounding box detections on dense real-world aerial traffic data.

## 📦 System Dependencies & Requirements
To run this project successfully, ensure you have the following installed in your Python environment:
* **Python:** `3.8` or higher
* **Ultralytics (YOLOv8):** `ultralytics>=8.0.0`
* **OpenCV:** `opencv-python` (for image processing and bounding box rendering)
* **Pandas & NumPy:** For data handling and metric logging
* **PyTorch:** Compatible with your hardware (CUDA recommended for training/inference)

You can install all core requirements via terminal:
```bash
pip install ultralytics opencv-python pandas numpy torch