# openai_functions.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()


# Set your OpenAI API key
SECRET_TOKEN = os.getenv('OPENAI_API_KEY')



def send_message(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        api_key = SECRET_TOKEN
    )
    return response["choices"][0]["message"]["content"]
 """   

def send_message(message):
   
    Generates a response to the user's input using the OpenAI GPT-3.5-Turbo model.

    Args:
        user_input (str): The user's input to generate a response to.

    Returns:
        str: The response generated by the GPT-3.5-Turbo model.
    
    prompt = user_input + "\ndoctor chatbot:\n"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.15 # Adjust the token limit as needed
        )
        
        return response.choices[0].message["content"].strip()

    except Exception as e:
        return str(e)
"""
