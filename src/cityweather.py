import re
import sys
import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv("API_KEY")

if __name__ == "__main__": 
    print("Enter City")
    city = input()
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # temperature in Celsius
    }
    response = requests.get(url, params)
    data = response.json()
    # print(response.status_code)
    if response.status_code != 200:
        print(f"Error Code {response.status_code}, Enter a Valid City")
    else:
        print(f"temperature: {data['main']['temp']} degrees Celsius")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")
