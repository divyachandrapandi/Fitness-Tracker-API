import requests
from datetime import datetime


username = "divyachandrapandi"
API_KEY = "aa689022297f21b8b16fb0309d225741"
APP_ID = "9a7a92a6"
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
sheety_endpoint = "https://api.sheety.co/159c57a4845f54585761b941dcef8bd7/workoutTracking/workouts"
sheety_bearer_token = "Basic ZGl2eWE1NTpwYXNzaGF0ag=="
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
replit = "https://replit.com/@Divya55/Fitnesstracker?v=1#main.py"