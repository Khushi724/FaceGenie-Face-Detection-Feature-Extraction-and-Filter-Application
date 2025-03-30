import cv2
import numpy as np
import dlib
import os

# Configuration
USE_WEBCAM = True
IMAGE_PATH = r"khushi.jpg"

# Initialize webcam or load image
cap = cv2.VideoCapture(0) if USE_WEBCAM else None

# Load face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Trackbar utility function
def on_trackbar_change(value):
    pass

# Create a window for color adjustment
def initialize_trackbar():
    cv2.namedWindow("BGR")
    cv2.resizeWindow("BGR", 640, 240)
    cv2.createTrackbar("Blue", "BGR", 0, 255, on_trackbar_change)
    cv2.createTrackbar("Green", "BGR", 0, 255, on_trackbar_change)
    cv2.createTrackbar("Red", "BGR", 0, 255, on_trackbar_change)

def get_trackbar_values():
    """Fetches current trackbar values for Blue, Green, and Red."""
    b = cv2.getTrackbarPos("Blue", "BGR")
    g = cv2.getTrackbarPos("Green", "BGR")
    r = cv2.getTrackbarPos("Red", "BGR")
    return (b, g, r)

def apply_mask(image, points):
    """Applies a mask to the given image based on provided points."""
    mask = np.zeros_like(image)
    mask = cv2.fillPoly(mask, [points], (255, 255, 255))
    return cv2.bitwise_and(image, mask)

def process_frame(image):
    """Processes the given frame to detect faces and apply lip color modification."""
    img = cv2.resize(image, (0, 0), None, 1, 1)
    img_original = img.copy()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector(img_gray)
    print(f"Number of faces detected: {len(faces)}")

    for face in faces:
        landmarks = predictor(img_gray, face)
        landmark_points = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(68)])

        img_lips = apply_mask(img, landmark_points[48:61])
        img_color_lips = np.zeros_like(img_lips)

        b, g, r = get_trackbar_values()
        img_color_lips[:] = (b, g, r)

        img_color_lips = cv2.bitwise_and(img_lips, img_color_lips)
        img_color_lips = cv2.GaussianBlur(img_color_lips, (7, 7), 10)
        img_color_lips = cv2.addWeighted(img_original, 1, img_color_lips, 0.8, 0)

        cv2.imshow("BGR", img_color_lips)
        cv2.imshow("Lips", img_lips)
        cv2.imshow("Original Image with Landmarks", img_original)
        print(landmark_points)

def main():
    initialize_trackbar()
    while True:
        if USE_WEBCAM:
            success, img = cap.read()
            if not success:
                continue
        else:
            img = cv2.imread(IMAGE_PATH)
        process_frame(img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
