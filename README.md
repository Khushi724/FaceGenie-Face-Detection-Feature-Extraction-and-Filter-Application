# Face Detection, Feature Extraction, and Filter Application

## Overview
This project leverages OpenCV and Dlib to perform real-time face detection, feature extraction, and color filtering. It detects faces, extracts key facial landmarks, and applies a user-defined color filter using OpenCV trackbars. The program supports both live webcam feed and static images for processing.

## Features
- **Real-Time Face Detection**: Utilizes Dlib's `get_frontal_face_detector` to locate faces efficiently.
- **Facial Landmark Extraction**: Extracts 68 key facial landmarks using a pre-trained Dlib model.
- **Customizable Color Filters**: Allows users to apply dynamic color filters, such as lip color enhancement, via interactive trackbars.
- **Supports Webcam and Image Input**: Users can choose between processing live webcam feed or a pre-specified image.
- **Smooth Blurring & Blending**: The applied color filter undergoes Gaussian blurring for a natural appearance.

## Installation
### Prerequisites
Before running the project, ensure you have the necessary dependencies installed:

```bash
pip install opencv-python numpy dlib
```

Additionally, download the Dlib pre-trained facial landmark model `shape_predictor_68_face_landmarks.dat` from [Dlib's Model Repository](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2). Extract and place the file in the project directory.

### Important Note on Dlib Compatibility
Dlib is known to work best with older versions of Python (e.g., Python 3.6 or 3.7). If you encounter compatibility issues, consider setting up a virtual environment with an older Python version using the following steps:

```bash
# Create a virtual environment with Python 3.7
python3 -m venv dlib_env
source dlib_env/bin/activate  # On Windows, use: dlib_env\Scripts\activate
pip install opencv-python numpy dlib
```

Ensure you activate the virtual environment before running the script.

## Usage
### Running the Application
1. **Using a Webcam**:
   - Set `USE_WEBCAM = True` in the script.
   - Ensure your webcam is properly connected.

2. **Using an Image**:
   - Set `USE_WEBCAM = False` in the script.
   - Specify the image path by modifying `IMAGE_PATH`.

To execute the script, run:
```bash
python main.py
```

### Controls
- The program opens a trackbar window labeled "BGR," where users can adjust the Blue, Green, and Red values in real time.
- The applied filter will change dynamically based on the selected color values.

## Code Structure
- `initialize_trackbar()`: Initializes a trackbar window to control BGR values interactively.
- `get_trackbar_values()`: Retrieves the current BGR values from trackbars for color adjustment.
- `apply_mask(image, points)`: Applies a binary mask over a specified facial region (e.g., lips) for color modification.
- `process_frame(image)`: Detects faces, extracts landmarks, applies color filtering, and displays the processed image.
- `main()`: Manages the program loop, continuously fetching frames from the webcam or loading the specified image.

## Notes
- If using a webcam, ensure it is properly connected and accessible.
- The `shape_predictor_68_face_landmarks.dat` file must be present in the working directory for facial landmark extraction to work.
- The Gaussian blur ensures a smooth and natural blending effect for the applied filter.
- Performance may vary depending on system specifications and webcam quality.

## Future Enhancements
- Implement additional facial filters such as eyebrow recoloring or skin smoothing.
- Improve performance using GPU acceleration with OpenCV’s CUDA capabilities.
- Expand to real-time facial expression detection and modification.

## License
This project is open-source and available for modification and distribution. Feel free to enhance and customize it based on your needs.

---
**Author**: Khushi Agarwal

