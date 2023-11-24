import requests
import json

url = "http://127.0.0.1:5000/chat"
data = {"patient_input": "drugs for flu"}

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

print("Response:")
print(response.status_code)
print(response.json())
