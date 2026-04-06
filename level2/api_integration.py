from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

def main():
    city = input("Enter a city: ")
    data = api_integration(city)
    print(data)


def api_integration(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "min": data["main"]["temp_min"],
            "max": data["main"]["temp_max"],
            "pressure": data["main"]["pressure"],
            "rise": data["sys"]["sunrise"],
            "set": data["sys"]["sunset"],
            "timezone": data["timezone"]
        }
    else:
        return f"Error Ocurred: Can fetch {city}'s data."

    return f"{'City':<8} | {city:<6}\n{'Temperature':<8} | {weather_data["temperature"]:<6}"


if __name__ == "__main__":
    main()
