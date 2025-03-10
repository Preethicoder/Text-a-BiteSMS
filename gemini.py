
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
APP_KEY = os.getenv("APP_KEY")

def get_nutrition(text, display=False):
    """
    Retrieves nutrition information for a given food item or list of items using the Gemini API.

    Args:
        text: The food item or list of food items.
        display: If True, provides a summary of total calories and macronutrients.
                 If False, provides detailed nutrition information for each item.

    Returns:
        The nutrition information as a string, or None if an error occurs.
    """
    try:
        genai.configure(api_key=APP_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")

        if display:
            refined_query = (
                f"Calculate the approximate total calories and macronutrient composition for: {text}. "
                "Provide a general estimate. "
                "Format: Total calories: [value] kcal, Protein: [value] g, Carbs: [value] g, Fats: [value] g"
            )
        else:
            refined_query = (
                f"Provide the calorie and macronutrient composition for: {text}. "
                "If no quantity is given, provide average values. "
                "Format: [Food Name]: Calories: [value] kcal, Protein: [value] g, Carbs: [value] g, Fats: [value] g"
            )

        response = model.generate_content(refined_query)
        return response.text

    except Exception as e:
        print(f"Error: {e}")
        return None










