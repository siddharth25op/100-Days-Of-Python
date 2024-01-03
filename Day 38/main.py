import requests
from datetime import datetime

APP_ID = "56b61045"
API_KEY = "032865d08c89b01aa5d1052482e4b63a"

BASE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Enter Query:")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": 60,
    "height_cm": 180,
    "age": 20
}

response = requests.post(BASE_URL, json=parameters, headers=header)
result = response.json()
print(result)
sheet_url = "https://api.sheety.co/7abc170df37ecd30d14a5d446cbeea46/data/sheet1"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_url, json=sheet_inputs)

    print(sheet_response.text)
