import requests
response = requests.get("https://api.agify.io?name=adnan")
data = response.json()
print("Predicted age:", data["age"])
