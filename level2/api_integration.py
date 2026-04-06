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

    display_data = f"""
{'City':<12} | {weather_data["city"]:<12}|
{'Country':<12} | {weather_data["country"]:<12}|
{'Temperature':<12} | {weather_data["temperature"]:<12}|
{'Pressure':<12} | {weather_data["pressure"]:<12}|
{'Minimun Temp':<12} | {weather_data["min"]:<12}|
{'Maximum Temp':<12} | {weather_data["max"]:<12}|
{'Time Zone':<12} | {weather_data["timezone"]:<12}|
    """

    return display_data


if __name__ == "__main__":
    main()
