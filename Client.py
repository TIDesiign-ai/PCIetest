import requests


url = "http://192.168.1.100:8000/api"

data = {
    "message": "Hello",
    "value": 123
}

response = requests.post(url, json=data)

print(response.json())
