# TruePAN - Reliable PAN Card Verification System

TruePAN is an intelligent document verification system that validates Indian PAN cards using advanced computer vision and deep learning techniques. 
This application leverages YOLO for object detection, EasyOCR for text extraction, and a deep learning classifier for authenticity checks.

---

# Features

- Upload PAN card images for verification  
- YOLOv8-based detection of card elements  
- OCR text extraction using EasyOCR  
- Authenticity check using pre-trained ML models  
- Clean result display and user-friendly UI  
- Stores uploaded images securely  
- Invalidates forged or tampered PAN cards

---

#Tech Stack

- Frontend: HTML | CSS | Bootstrap  
- Backend: Python | Flask  
- Libraries: OpenCV | EasyOCR | TensorFlow | Keras | Ultralytics YOLOv8  
- Deployment: Render (or Railway, Google Cloud Run, etc.)

---

#Getting Started

# 1. Clone the Repository

```bash
git clone https://github.com/pranavsambidi/TruePAN.git
cd docverify
```

# 2. Install Dependencies

Make sure you have Python 3.8+ and pip installed. Then run:

```bash
pip install -r requirements.txt
```

# 3. Run the App

```bash
python app.py
```

Go to `http://localhost:5000` to view the app in your browser.

---

# 📁 Project Structure

```
docverify/
├── static/
│   ├── image/                  # Uploaded image folder
│   └── tracking.jpg            # Favicon
├── templates/
│   └── index.html              # Main UI template
├── model/
│   ├── yolo_model/             # YOLO weights and config
│   └── verifier_model.h5       # Trained authenticity classifier
├── app.py                      # Flask backend
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

# Deployment on Render

1. Push the project to a GitHub repository
2. Go to [https://render.com](https://render.com) → Create new Web Service
3. Connect your GitHub repo
4. Set:
   - Start Command: `python app.py`
   - Build Command: *(leave blank or use `pip install -r requirements.txt`)*
   - Environment: Python 3.x
5. Set Environment Variables if needed
6. Deploy!

> ⚠️ If using large models, consider upgrading to a plan with higher memory.

---

#AI Models Used

- YOLOv8: Fast and accurate object detection for PAN elements  
- EasyOCR: Lightweight and effective OCR for multi-lingual text  
- TensorFlow Model: Trained classifier to verify real vs fake PANs

---
