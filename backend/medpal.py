from open import send_message
# chat_functions.py

def adaptive_truncate(message, token_limit):
    tokens = message["content"].split()
    truncated_tokens = []
    total_tokens = 0
    for token in tokens:
        total_tokens += len(token.split())
        if total_tokens <= token_limit:
            truncated_tokens.append(token)
        else:
            break
    message["content"] = " ".join(truncated_tokens)
    return message

def custom_chat_gpt(enter_your_question):
    token_limit = 4000
    messages = [{"role": "system", "content": "You are a doctor"}]

    user_input_tokens = enter_your_question.split()
    current_message = {"role": "user", "content": ""}
    current_token_count = len("You are a doctor".split())

    for token in user_input_tokens:
        token_tokens = len(token.split())
        if current_token_count + token_tokens <= token_limit:
            current_message["content"] += token + " "
            current_token_count += token_tokens
        else:
            current_message = adaptive_truncate(current_message, token_limit)
            reply = send_message(messages + [current_message])
            messages.append({"role": "user", "content": " ".join(current_message["content"].split())})
            messages[-1]["content"] = reply
            current_message = {"role": "user", "content": token + " "}
            current_token_count = token_tokens

    current_message = adaptive_truncate(current_message, token_limit)
    reply = send_message(messages + [current_message])
    messages.append({"role": "user", "content": " ".join(current_message["content"].split())})
    messages[-1]["content"] = reply

    return reply

def patient_chat(patient_input):
    # Process patient input, handle queries, etc.
    messages = [{"role": "user", "content": patient_input}]

    # Use a prompt to ask for symptoms
    prompt = "Please describe your symptoms, and I will do my best to assist you."
    messages.append({"role": "system", "content": prompt})

    # Send the messages to the chatbot
    response = send_message(messages)

    # Extract the relevant information from the response
    # In a real-world scenario, you would use more advanced natural language processing techniques
    # and consult healthcare professionals or databases for accurate information.

    # For simplicity, let's assume the chatbot provides drug names in square brackets
    drug_candidates = [word.strip('[]') for word in response.split() if word.startswith('[') and word.endswith(']')]
    
    # If drug candidates are found, return the first one; otherwise, provide a general response
    return f"The suggested drug for your symptoms is: {drug_candidates[0]}" if drug_candidates else "I recommend consulting with a healthcare professional for personalized advice."
