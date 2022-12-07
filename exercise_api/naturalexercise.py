import requests
import datetime as dt
now = dt.datetime.now()

GENDER = "male"
WEIGHT_KG = "85"
HEIGHT_CM ="183"
AGE = "24"
body = {
    "query": input("tell me what you did"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id":"1c80e273",
"x-app-key":"2c7cdf885d87c58b51c7ad77960b5785"
}

response = requests.post(url=" https://trackapi.nutritionix.com/v2/natural/exercise",
                         json= body
                         , headers=headers)
print(response.json())

dic = response.json()["exercises"][0]



"________________---adding rows ____________________________"

row = requests.post(url="https://api.sheety.co/916958af53b521c9dc948ca92d8542d8/newWorkout/sheet1",
                    json= {"sheet1":{


      "date": now.strftime("%H:%M"),
      "time": now.strftime("%d-%m-%Y"),
      "exercise": dic["name"].title(),
      "duration": dic["duration_min"] ,
      "calories": dic["nf_calories"],

                    }
                           })

print(row.text)