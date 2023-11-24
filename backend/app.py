# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from openai import initialize_openai
from medpal import custom_chat_gpt, patient_chat

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
SECRET_TOKEN = os.getenv('OPENAI_API_KEY')
if not SECRET_TOKEN:
    raise ValueError("OPENAI_API_KEY is not set. Please set it in your environment.")

initialize_openai(SECRET_TOKEN)

# API endpoint to receive user input
@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()
        user_input = data['user_input']

        # Call your custom_chat_gpt function
        response = custom_chat_gpt(user_input)

        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)})
    
# API endpoint to receive patient input
@app.route('/chat', methods=['POST'])
def patient_chat_endpoint():
    try:
        data = request.get_json()
        patient_input = data['patient_input']

        # Call your patient_chat function
        response = patient_chat(patient_input)

        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
