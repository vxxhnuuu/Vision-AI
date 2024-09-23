import google.generativeai as genai  # Assuming this is the correct library for interacting with Gemini API
import html

# Set your API key
API_KEY = "AIzaSyAihtq0kFBTVnepqQ3MKfoC2ZpcWcGBgU8"

CUSTOM_PROMPT = (
    "Please respond with only the necessary output based on the user query. "
    "For predefined commands, respond with the corresponding response code as defined:\n"
    "close = close\n"
    "add a face = add\n"
    "scan a face = scan\n"
    "time = time\n"
    "open smart lens = lens\n"
    "For all other queries, respond with only the direct output of the query without any additional explanation. "
    "If any questions is asked give brief answer."
    "If any error is encountered return error. Dont explain the error"
    "This is the user's query:"
)

# Configure the Gemini API
def configure_api():
    if not API_KEY:
        raise ValueError("API key is not set.")
    genai.configure(api_key=API_KEY)

# Generate a response from the Gemini API
def generate_response(prompt):
    configure_api()  # Ensure the API is configured before making a request
    prompt_full = f"{CUSTOM_PROMPT} {prompt}"
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Replace with your actual model identifier
        response = model.generate_content(prompt_full)
        if response:
            decoded_response = html.unescape(response.text)  # Decode HTML entities if any
            cleaned_response = decoded_response.replace('*', '').replace('**', '')
            return cleaned_response.strip()  # Ensure no leading or trailing whitespace
        return "No response generated."
    except Exception as e:
        return f"Error: {str(e)}"