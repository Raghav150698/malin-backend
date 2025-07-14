from google.generativeai import client
from google.api_core.exceptions import GoogleAPICallError, NotFound

# Configure your Google API key here (set as env variable recommended)
API_KEY = "YOUR_GOOGLE_API_KEY"

client.configure(api_key=API_KEY)

async def list_available_models():
    """
    Utility async function to list available models.
    Call this once to check which models you can use.
    """
    try:
        models = client.list_models()
        return [model.name for model in models.models]
    except GoogleAPICallError as e:
        return f"Error fetching models: {str(e)}"

async def get_gemini_response(question: str) -> str:
    """
    Generate a response from the Gemini (Google Generative AI) model.
    Replace 'models/text-bison-001' with your valid model name.
    """
    try:
        model = client.get_model("models/text-bison-001")  # Replace with your model after list check

        response = model.generate_content(question)
        return response.text

    except NotFound:
        return "Error: Model not found. Please check the model name and API access."
    except GoogleAPICallError as e:
        return f"API Error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
