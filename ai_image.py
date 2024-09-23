# ai.py
import PIL.Image
import google.generativeai as genai  # Assuming you have the genai library for Gemini API
import html

# Set your API key (replace with your actual API key)
API_KEY = "AIzaSyAihtq0kFBTVnepqQ3MKfoC2ZpcWcGBgU8"

# Custom prompt to guide the response generation
CUSTOM_PROMPT = (
    "Please respond with only the necessary output based on the user query. "
    "For all other queries, respond with only the direct output of the query without any additional explanation. "
    "If any question is asked, give a brief answer. "
    "If the query is related to the given image, give a response related to the image. "
    "If the query is to read the page of a book read it"
    "If the query is to summarize the content of the page give summary"
    "This is the user's query:"
)

# Function to configure the Gemini API with your API key
def configure_api():
    if not API_KEY:
        raise ValueError("API key is not set.")
    genai.configure(api_key=API_KEY)

# Generate a response from the Gemini API
def generate_image_response(text_prompt, image_path):
    # Configure API
    configure_api()

    # Combine the custom prompt with the user's text input
    prompt_full = f"{CUSTOM_PROMPT} {text_prompt}"
    
    try:
        # Load the image using PIL
        image = PIL.Image.open(image_path)

        # Initialize the model (replace 'gemini-1.5-pro' with your actual model identifier)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Send the combined text prompt and image to the model
        response = model.generate_content([prompt_full, image])
        
        if response:
            # Decode HTML entities and clean up any extra symbols in the response
            decoded_response = html.unescape(response.text)
            cleaned_response = decoded_response.replace('*', '').replace('**', '')
            return cleaned_response.strip()  # Ensure no leading or trailing whitespace
        
        return "No response generated."
    
    except Exception as e:
        return f"Error: {str(e)}"
