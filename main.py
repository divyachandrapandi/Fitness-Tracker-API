import requests
from datetime import datetime



API_KEY = your api key
APP_ID = your app id
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
user_input = input("What exercise did you completed successfully: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": user_input,
    "gender": "female",
    "weight_kg": "74",
    "height_cm": "164",
}

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=headers)
data = response.json()

# TOdo sheety
today = datetime.now()
sheety_username = "divya55"
sheety_password = "passhatj"
sheety_endpoint = "sheety_endpoint"
sheety_bearer_token = "sheety Token"
# Bearer authentication
headers = {
    "Authorization": sheety_bearer_token
}

for n in range(len(data["exercises"])):
    workouts = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": (data["exercises"][n]["name"]).title(),
            "duration": data["exercises"][n]["duration_min"],
            "calories": data["exercises"][n]["nf_calories"],

        }

    }
    # Basic authentication
    # response = requests.post(url=sheety_endpoint, json=workouts, auth =(USERNAME, PASSWORD))
    sheety_res = requests.post(url=sheety_endpoint, json=workouts, headers=headers)
    print(sheety_res.status_code)
