import requests

API_Key = "4907d8ee413a95e945f504b0a9ef3b70"
url = f"https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={API_Key}"
# b = requests.get(url)
# a=b.json()

b= {'coord': {'lon': -0.1257, 'lat': 51.5085}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 279, 'feels_like': 276.29, 'temp_min': 278.46, 'temp_max': 279.82, 'pressure': 1028, 'humidity': 74, 'sea_level': 1028, 'grnd_level': 1024}, 'visibility': 10000, 'wind': {'speed': 3.6, 'deg': 60}, 'clouds': {'all': 100}, 'dt': 1767012722, 'sys': {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1766995571, 'sunset': 1767023920}, 'timezone': 0, 'id': 2643743, 'name': 'London', 'cod': 200}
print(b['main']['temp'])

