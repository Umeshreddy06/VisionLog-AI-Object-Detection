# 🤖 VisionLog AI — Real-Time Object Detection & Logging Platform

> Assignment 5 submission project built with Python, OpenCV, Ultralytics YOLO, Streamlit and MySQL.

## 🌐 Project Links

Replace these placeholders after publishing:

- **Live Deployment:** `https://YOUR-APP-NAME.streamlit.app`
- **GitHub Repository:** `https://github.com/YOUR-USERNAME/Real-Time-Object-Detection`
- **Demo Video:** `YOUR-YOUTUBE-OR-GOOGLE-DRIVE-LINK`
- **Medium Article:** `YOUR-MEDIUM-ARTICLE-LINK`

## ✨ What makes this project complete

- YOLOv8n object detection
- Configurable confidence threshold
- Object/class filtering
- OpenCV bounding boxes and labels
- Browser camera support for cloud deployment
- Image upload mode for reliable public demos
- MySQL detection-event logging
- Recent event dashboard
- Modular Python architecture
- Secure environment-variable database configuration
- GitHub-ready documentation

## 🏗️ Architecture

```text
                   ┌──────────────────────┐
                   │     Streamlit UI     │
                   │       ui.py          │
                   └──────────┬───────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
        ┌────────▼────────┐       ┌────────▼────────┐
        │  YOLO Detector  │       │  MySQL Database │
        │   detector.py   │       │   database.py   │
        └────────┬────────┘       └────────┬────────┘
                 │                         │
        ┌────────▼────────┐       ┌────────▼────────┐
        │ OpenCV Frames   │       │ detection_logs  │
        └─────────────────┘       └─────────────────┘
```

## 📁 Project Structure

```text
Real-Time-Object-Detection/
├── main.py
├── ui.py
├── detector.py
├── database.py
├── database_schema.sql
├── requirements.txt
├── .env.example
├── .gitignore
├── .streamlit/
│   └── config.toml
├── packages.txt
└── README.md
```

## 🚀 Local Setup

```bash
python -m venv venv
```

Windows:

```cmd
venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Create `.env` from `.env.example`:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=vision_platform
```

Never commit `.env`.

## 🗄️ MySQL Setup

Run `database_schema.sql` in MySQL Workbench/phpMyAdmin.

The schema creates:

```text
vision_platform
└── detection_logs
    ├── log_id
    ├── timestamp
    ├── object_class
    ├── confidence
    ├── bbox_x
    ├── bbox_y
    ├── bbox_w
    └── bbox_h
```

## ☁️ Streamlit Deployment

1. Push this repository to GitHub.
2. Open Streamlit Community Cloud.
3. Create a new app.
4. Select the GitHub repository.
5. Set the main file to `main.py`.
6. Add the database connection values as Streamlit secrets/environment variables.
7. Deploy.
8. Copy the generated `streamlit.app` URL into the submission form.

### Important deployment note

A cloud application cannot access the webcam connected to your personal laptop through `cv2.VideoCapture(0)`. This version therefore uses Streamlit's browser camera input for the deployed demo. Local OpenCV processing remains available through the detector module.

For a completely cloud-hosted MySQL database, use a reachable MySQL service rather than `localhost`.

## 🎥 Recommended Demo

Show these in 1–2 minutes:

1. GitHub repository.
2. Live deployed Streamlit URL.
3. Object/class filter.
4. Confidence threshold.
5. Camera/image detection.
6. Bounding box and confidence.
7. Recent MySQL logs.
8. GitHub README and project architecture.

## 📝 Medium Article Outline

### 1. Introduction
Explain the purpose of VisionLog AI.

### 2. Computer Vision & YOLO
Explain OpenCV, YOLO, classes, bounding boxes and confidence.

### 3. Modular Architecture
Explain `ui.py`, `detector.py`, `database.py`, and `main.py`.

### 4. Database Integration
Explain the `detection_logs` schema and real-time event insertion.

### 5. Streamlit UI
Explain camera input, object filtering, confidence threshold and log table.

### 6. Deployment
Explain GitHub → Streamlit deployment and why browser camera input is used.

### 7. Challenges & Solutions
Discuss camera access, model download, database connectivity and deployment.

### 8. Final Result
Add screenshots plus GitHub, deployment and demo links.

## ✅ Assignment 5 Checklist

- [x] Python
- [x] OpenCV
- [x] Ultralytics YOLO
- [x] Object configuration/filter
- [x] Confidence threshold
- [x] Bounding boxes
- [x] Streamlit dashboard
- [x] MySQL schema
- [x] MySQL event logging
- [x] Modular architecture
- [x] `.env` protection
- [x] Deployment-compatible camera input
- [ ] Public GitHub repository URL
- [ ] Live deployment URL
- [ ] Demo video URL
- [ ] Medium article URL
- [ ] Google Form submission

## 🔐 Security

Do not upload database passwords, API keys, `.env`, or Streamlit secrets to GitHub.
