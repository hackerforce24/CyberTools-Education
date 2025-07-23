import requests

ip = input("Enter IP: ")
response = requests.get(f"http://ip-api.com/json/{ip}")
data = response.json()
print(data)
