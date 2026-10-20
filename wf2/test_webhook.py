import requests


user_message = "Can you tell me about blackholes in 2 lines"

request_message = {"message": user_message}

url = "https://rohan-man.app.n8n.cloud/webhook-test/8d87a61c-e893-476c-9ab5-a00c6e9e183d"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])