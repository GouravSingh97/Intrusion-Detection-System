import requests
import logging
logging.basicConfig(filename="logs/geo.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
def get_geolocation(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        return f"{data.get(city, )}, {data.get(country, )}"
    except Exception as e:
        logging.error(f"Geolocation error for IP {ip}: {str(e)}")
        return "Unknown"
