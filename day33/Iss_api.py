import requests

response =requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_longitude=data["iss_position"]["longitude"]
iss_latitude=data["iss_position"]["latitude"]

print(iss_latitude,iss_longitude)