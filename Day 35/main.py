from twilio.rest import Client
import requests


def weather():
    api = ""
    account_sid = ""
    auth_token = ""
    # city = "Indore"

    lat = 22.1716912
    lon = 76.0724656

    parameters = {
        "lat": lat,
        "lon": lon,
        "appid": api,
        "cnt": 4
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    weather = response.json()

    will_rain = False
    for hour_data in weather["list"]:
        condition = hour_data["weather"][0]["id"]
        if int(condition) < 700:
            will_rain = True

    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to="",
            from_="",
            body="It's going to rain today. Bring an umbrella! ☔")


weather()
