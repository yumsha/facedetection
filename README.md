# Face Recognition Wannabe

This project is a simple face recognition app using OpenCV and the [face_recognition](https://github.com/ageitgey/face_recognition) library.

## Features
- Detects faces from a webcam feed.
- Compares detected faces against a known dataset.
- Labels recognized faces with their names, unknown faces as "Unknown".
- Draws bounding boxes around detected faces.

## Requirements
- Python 3.8+
- OpenCV (`cv2`)
- face_recognition library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/face-recognition-wannabe.git
   cd face-recognition-wannabe
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python face_recognition
   ```

3. Add your reference images to the `images/` folder.

## Usage
Run the script:
```bash
python main.py
```

- Press `q` to quit the webcam.

## Project Structure
```
.
├── images/
│   └── riza.jpg
├── main.py
└── README.md
```

## Acknowledgements
- Thanks to [Adam Geitgey](https://github.com/ageitgey) for the amazing [face_recognition](https://github.com/ageitgey/face_recognition) library.
