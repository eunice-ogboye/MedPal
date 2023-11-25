# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS



from medpal import custom_chat_gpt, patient_chat

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes





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

""" if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) """
