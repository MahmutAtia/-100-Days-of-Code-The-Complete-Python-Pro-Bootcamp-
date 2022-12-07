import requests

response = requests.get(url= "https://opentdb.com/api.php?amount=5&type=boolean")
question_data = response.json()["results"]


