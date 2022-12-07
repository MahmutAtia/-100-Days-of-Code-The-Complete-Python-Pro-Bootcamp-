import requests
def predict(name):
    response_age= requests.get(url=f"https://api.agify.io?name={name}")
    response_gender=requests.get(url=f"https://api.genderize.io?name={name}")
    return response_age.json()["age"],response_gender.json()["gender"]

def posts():
    return requests.get(" https://api.npoint.io/c790b4d5cab58020d391").json()


