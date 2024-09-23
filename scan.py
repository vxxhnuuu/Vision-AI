import os
import cv2
import face_recognition
import numpy as np
import time
from tts_stt import speak_text

def recognize_face():
    folder_name = "faces"
    if not os.path.exists(folder_name):
        speak_text("Error: 'faces' directory not found.")
        print("Vision AI : Error: 'faces' directory not found.")
        return None

    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        speak_text("Error: Camera not found or cannot be opened.")
        print("Vision AI : Error: Camera not found or cannot be opened.")
        return None

    known_face_encodings, known_face_names = load_known_faces(folder_name)
    if not known_face_encodings:
        speak_text("No known faces found")
        print("Vision AI : No known faces found")
        video_capture.release()
        cv2.destroyAllWindows()
        return None

    recognized_name = 'Unknown'
    unknown_start_time = None  # To track the time when an unknown face is first detected

    while True:
        ret, frame = video_capture.read()
        if not ret:
            speak_text("Failed to grab frame.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            
            if face_distances[best_match_index] < 0.4:  # Threshold for matching
                recognized_name = known_face_names[best_match_index]
                
                # Draw a rectangle around the face and put the name on the frame
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, recognized_name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
                unknown_start_time = None  # Reset unknown timer when a known face is found
                break  # Exit after first match, or remove this to continue checking
            else:
                if unknown_start_time is None:
                    unknown_start_time = time.time()  # Record time when the unknown face is first detected
                elif time.time() - unknown_start_time > 5:
                    recognized_name = "Unknown"
                    break

        # Display the result
        cv2.imshow('Video', frame)

        if recognized_name != 'Unknown' or (unknown_start_time and time.time() - unknown_start_time > 5):
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return recognized_name

def load_known_faces(folder_name):
    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(folder_name):
        if filename.lower().endswith(('.jpg', '.png')):
            image_path = os.path.join(folder_name, filename)
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)

            if face_encodings:
                encoding = face_encodings[0]
                name = os.path.splitext(filename)[0]
                known_face_encodings.append(encoding)
                known_face_names.append(name)
                print(f"Vision AI : Loaded face for: {name}")  # Debugging information

    return known_face_encodings, known_face_names
