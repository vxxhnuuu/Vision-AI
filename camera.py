# camera.py
import cv2
from tts_stt import speak_text  # Assuming you're using the tts_stt.py for speaking text

def capture_image(image_path="captured_image.jpg"):
    """Capture an image using the webcam and save it to a file."""
    # Initialize the camera (0 is the default camera)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        speak_text("Error: Could not open the camera.")
        return None

    # Read a single frame from the camera
    ret, frame = cap.read()
    
    if ret:
        # Save the captured image to the specified path
        cv2.imwrite(image_path, frame)
    else:
        speak_text("Error: Could not capture the image.")
        image_path = None

    # Release the camera
    cap.release()

    return image_path
