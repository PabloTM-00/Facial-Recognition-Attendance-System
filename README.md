# Real-time Face Recognition Attendance System

This project is a real-time face recognition attendance system built using Python, OpenCV, and dlib. It captures faces from a webcam, compares them with known faces stored as images, and automatically marks attendance in a CSV file.

## Features
- Real-time face detection and recognition via webcam.
- Easily add new known faces by placing images in the `ImagesAttendance` folder.
- Automatic attendance logging with timestamps.
- Visual bounding boxes and names displayed on recognized faces.

## Requirements
- Python 3.8 or higher.
- The following Python packages:
  - click==8.1.8
  - colorama==0.4.6
  - dlib (requires manual installation from a wheel due to system compatibility)
  - face-recognition==1.3.0
  - face_recognition_models==0.3.0
  - numpy==1.24.4
  - opencv-python==4.12.0.88
  - pillow==10.4.0

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/PabloTM-00/Facial-Recognition-Attendance-System.git
   cd Facial-Recognition-Attendance-System
  
2. **(Optional but recommended) Create and activate a virtual environment:**

   * **Windows:**

     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

   * **macOS/Linux:**

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install dlib manually (if needed):**

   Since `dlib` can be tricky to install via `pip`, download the appropriate precompiled wheel for your Python version and OS (e.g., `dlib-19.22.99-cp38-cp38-win_amd64.whl`) from a trusted source, then install it manually:

   ```bash
   pip install path/to/dlib-19.22.99-cp38-cp38-win_amd64.whl
   ```
## Usage
- Add clear, frontal face images of people you want to recognize inside the `ImagesAttendance` folder. The image filenames will be used as the person's name.
- Run the main Python script:
  ```bash
  python AttendanceProject.py
- The webcam will open and detect faces in real time.
- When a known face is detected, their name and attendance timestamp will be logged in `Attendance.csv`.
- The program will display the webcam feed with rectangles and names on recognized faces.

## Notes
- Make sure your webcam is accessible and not used by other applications.
- The attendance CSV file is created in the project root directory.
- The system relies on face encodings extracted from images; lighting and image quality affect accuracy.
- You can stop the program by closing the webcam window or pressing Ctrl+C in the terminal.

Feel free to open issues or contribute with improvements!
