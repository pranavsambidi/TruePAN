Tech Stack: Python | Flask | YOLOv8 | TensorFlow | Keras | EasyOCR | OpenCV | HTML | CSS | Bootstrap

Overview:
• TruePAN is a deep learning-powered web application developed to automate and validate Indian PAN card authenticity. The system combines modern computer vision, optical character recognition (OCR), and machine learning techniques to detect fraudulent or tampered PAN cards based on visual and textual verification.
• I built this project using Flask as the backend framework, integrating a YOLOv8 object detection model to localize key document components (like the official logo and issuing authority) and EasyOCR to extract textual content. To ensure brand/logo authenticity, a custom-trained CNN model (Keras/TensorFlow) was implemented, distinguishing real logos from fake imitations.
• The application has a clean, user-friendly frontend built with HTML, CSS, and Bootstrap, allowing users to upload PAN card images and instantly get validation results (Valid/Invalid). Caching is smartly handled to prevent re-displaying old images, and reloading the app resets the state for a fresh verification session.

Key Highlights:
• Trained a custom YOLOv8 model to detect PAN card fields (Logo, Department text).
• Built a binary CNN classifier to verify if the detected logo is authentic or fake.
• Integrated EasyOCR to ensure the textual portion says "INCOME TAX DEPARTMENT".
• Designed a clean and responsive frontend with real-time feedback on document status.
