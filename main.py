import time
from tts_stt import listen_command, speak_text  # Import functions from tts_stt.py
from ai_text import generate_response  # Import generate_response from ai.py
from time_util import get_current_time  # Import your custom time utility
from camera import capture_image  # Import the capture_image function from camera.py
from add import add_face
from scan import recognize_face
from ai_image import generate_image_response
from sound import play_sound
import os

# Main execution inside a loop
if __name__ == "__main__":
    try:
        # Greet the user when the program starts
        print(f"Vision AI : Hi. I am Vision AI")
        speak_text("Hi. I am Vision AI")
        print(f"Vision AI : How can I help you?")
        speak_text("How can I help you?")
        
        while True:
            # Prompt the user for voice input
            #play_sound()
            text_prompt = listen_command()
            print(f"User : {text_prompt}")

            if text_prompt:
                # Generate a response based on the voice input
                response = generate_response(text_prompt)
                print(f"Gemeni Response: {response}")
                    
                # Handle specific commands based on the response
                if response.lower() == "close":
                    print(f"Vision AI : Closing Vision AI. Goodbye!")
                    speak_text("Closing Vision AI. Goodbye!")
                    break  # Exit the loop and end the program
                
                elif response.lower() == "lens":
                    # Capture an image and generate a response based on the image
                    print(f"Vision AI : Smart lens active.")
                    speak_text("Smart lens active.")
                    while True:
                        print(f"Smart Lens : How can i help you")
                        speak_text("How can i help you")
                        #play_sound()
                        image_prompt = listen_command()
                        print(f"User : {image_prompt}")
                        if image_prompt == "close":
                            print(f"Smart Lens : Closing smart lens")
                            speak_text("Closing smart lens")
                            break
                        image_path = capture_image()
                        response_image = generate_image_response(image_prompt , image_path)
                        print(f"Smart Lens : {response_image}")
                        speak_text(f"{response_image}")

                
                elif response.lower() == "time":
                    # Respond with the current time
                    current_time = get_current_time()
                    print(f"Vision AI : The current time is {current_time}")
                    speak_text(f"The current time is {current_time}")
                
                elif response.lower() == "add":
                    # Add a new face to the database
                    add_face()
                
                elif response.lower() == "scan":
                    # Scan and recognize a face
                    response_text = "Scanning person..."
                    print(f"Vision AI : {response_text}")
                    speak_text(response_text)
                    name = recognize_face()
                    if name == "Unknown":
                        print(f"Vision AI : Face not recognized. Please add the face.")
                        speak_text(f"Face not recognized. Please add the face.")
                    else:
                        response_text = f"You are speaking to {name}."
                        print(f"Vision AI : {response_text}")
                        speak_text(response_text)
                else:
                    # Speak the generated response for any other query
                    print(f"Vision AI : {response}")
                    speak_text(f"{response}")
            else:
                print(f"Vision AI : I did not capture any input. Please try again.")
                speak_text("I did not capture any input. Please try again.")

    except Exception as e:
        speak_text("An error occurred.")
        print(f"Error: {e}")
