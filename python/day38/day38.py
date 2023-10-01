import requests
from datetime import datetime
import os

# Retrival of datetime information
today_date = datetime.today().strftime("%m/%d/%Y")
today_time = datetime.now().strftime("%H:%M:%S")

print (today_date)
# Authentication_keys
APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
BEARER_ID = os.environ["BEARER_ID"]
BEARER = {"Authorization": f"Bearer {BEARER_ID}" }

# query_input = input("What did you do today? Please try your best to quantify the amount of exercise you've done."
#                     "e.g. I ran 3 miles\n")

query_input = "I walked three miles and did skipping for 30 minutes"

request_header = {
                    "x-app-id":APP_ID,
                    "x-app-key":APP_KEY,
                  }

request_body = {
    "query": query_input,
    "gender":"male",
    "weight_kg":65,
    "height_cm":172,
    "age":24
}

connection = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                           headers=request_header,
                           data =request_body,
                           )

result = connection.json()
for i in result["exercises"]:
    exercise_name = i["name"]
    exercise_duration = i["duration_min"]
    exercise_calories = i["nf_calories"]

    data_add_row = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise_name.title(),
            "duration": round(float(exercise_duration)),
            "calories": exercise_calories,
        }
    }

    print(data_add_row)

    requests.post(url="https://api.sheety.co/95af271f4017f5445552c4362bef01b8/pythonWorkout/workouts",
                  headers=BEARER,
                  json=data_add_row)







