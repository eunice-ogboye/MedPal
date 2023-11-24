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
