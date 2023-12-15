import smtplib
import requests
from datetime import datetime
import time

MY_LAT = 22.178200
MY_LON = 76.074097
MY_EMAIL = "minetrio25@gmail.com"
MY_PASSWORD = "zeabquanjkxgmekh"


def can_iss_be_seen():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LON-5 <= iss_longitude <= MY_LON+5:
        return True


def night():
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LON,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if can_iss_be_seen() and night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="Siddharthjainj25@gmail.com",
            msg="Subject: ISS Update\n\nIss is above you in the sky."
        )
