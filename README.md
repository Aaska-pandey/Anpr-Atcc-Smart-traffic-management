🚦 Smart Traffic Monitoring & Violation Detection System
ANPR • ATCC • Accident Detection • Helmet Detection • Triple Riding • Heatmap Visualization

This project is a complete AI-powered traffic monitoring system built using Flask, Python, YOLO, and OpenCV.
It automates and detects multiple traffic-related activities such as:

Number plate recognition

Vehicle counting and classification

Accident detection

Helmet violation detection

Triple riding detection

Traffic violation tracking

Heatmap-based traffic visualization

The system includes a web dashboard, MySQL database, and multiple video-processing modules.

⭐ Features
🔹 1) ANPR (Automatic Number Plate Recognition)

Detects vehicle number plates from video

Uses YOLO + OCR model

Saves plate details into MySQL database

Stores snapshots of detected vehicles

🔹 2) ATCC (Automatic Traffic Counting & Classification)

Detects and classifies vehicles (car, bus, truck, bike)

Counts vehicles in real-time

Tracks traffic density

Supports traffic signal optimization logic

🔹 3) Accident Detection

AI-based accident identification

Detects collisions, falls, and emergency situations

Multi-threaded processing for multiple videos

Shows output using OpenCV GUI

🔹 4) Helmet Violation Detection

Detects riders without helmets

Suitable for police monitoring

Works for crowded or moving traffic

🔹 5) Triple Riding Detection

Detects 3 or more people on a two-wheeler

Highlights the violation with bounding boxes

🔹 6) Traffic Violation Detection

Detects red light jump

Detects stop line crossing

Helps enforce traffic rules

🔹 7) Heatmap Visualization

Shows crowded or busy areas in traffic

Detects vehicle movement patterns

Useful for urban planning & congestion analysis

🔹 8) Web Frontend (Flask Dashboard)

Upload videos

Start different detection modules

Search detected number plates

View history, images, and timestamps

Clean UI for multi-module control


🛠 Tech Stack
Frontend

HTML

CSS

Flask 

Backend

Flask

Python

OpenCV

YOLO (Ultralytics)

NumPy

EasyOCR / pytesseract

Multi-threading

Database

MySQL
