import requests
url = "https://api.openweathermap.org/data/3.0/weather?lat=45.8116&lon=15.9425&appid=APIKEY"

response = requests.get(url)
print(response.json())