# openai_functions.py
import openai

def initialize_openai(api_key):
    openai.api_key = api_key

def send_message(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response["choices"][0]["message"]["content"]
