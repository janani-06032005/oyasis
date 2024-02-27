import requests
import geopy.geocoders

api_key = open("../api_key.txt", "r").read()


def main():
    city_name = input("City: ")

    geolocator = geopy.geocoders.Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city_name)
    lati = location.latitude
    longi = location.longitude

    weather_response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lati}&lon={longi}&appid={api_key}"
    ).json()

    print("Weather:", weather_response["weather"][0]["main"])
    print(
        "Temperature: {} Celcius".format(
            round(weather_response["main"]["temp"] - 273.15, 2)
        )
    )
    print("Humidity: {} %".format(weather_response["main"]["humidity"]))
    print("Wind Speed: {} meter/sec".format(weather_response["wind"]["speed"]))
    
    return


main()