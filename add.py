import os
import cv2
from tts_stt import listen_command, speak_text  # Import necessary functions
from sound import play_sound

def add_face():
    folder_name = "faces"
    os.makedirs(folder_name, exist_ok=True)  # Create directory if it doesn't exist

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        speak_text("Error: Could not open camera.")
        return

    speak_text("Capturing face, please wait.")
    print("Vision AI : Capturing face, please wait.")
    cv2.waitKey(1000)

    ret, frame = cap.read()
    if not ret:
        speak_text("Error: Failed to capture image.")
        print("Vision AI : Error: Failed to capture image.")
        cap.release()
        cv2.destroyAllWindows()
        return

    name = ""
    while not name:  # Keep asking for the name until it is captured
        speak_text("Please say the name for the captured face.")
        print("Vision AI : Please say the name for the captured face.")
        #play_sound()
        name = listen_command()
        
        if not name:
            speak_text("Sorry, I did not catch that. Please try again.")
            print("Vision AI : Sorry, I did not catch that. Please try again.")

    # Save the face image with the provided name
    file_path = os.path.join(folder_name, f"{name}.jpg")

    if os.path.exists(file_path):
        speak_text("Person already exists.")
        print("Vision AI : Person already exists.")
    else:
        cv2.imwrite(file_path, frame)
        speak_text(f"Face of {name} saved successfully.")
        print(f"Vision AI : Face of {name} saved successfully.")

    cap.release()
    cv2.destroyAllWindows()
