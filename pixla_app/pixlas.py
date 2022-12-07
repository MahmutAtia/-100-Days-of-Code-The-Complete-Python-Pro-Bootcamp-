import requests
import datetime as td
now = td.datetime.now()

dic = {
    "token": "nnwqp9e8jm43p9q8jmq",
    "username":"mamo",
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}
id = "jdi943"
post_param = {
    "id":"jdi943",
    "name": "Studing",
    "unit": "hours",
    "type":"float",
    "color": "ichou",

}
headers = {
    "X-USER-TOKEN": "nnwqp9e8jm43p9q8jmq"
}
# post = requests.post(url="https://pixe.la/v1/users/mamo/graphs",
#                      headers=headers, json= post_param
#                      )
date = str(now.date()).replace("-", "")
print(date)
pixle_param= {
    "date": f"{20220530}",
    "quantity": "10",
}
pixl = requests.post(url="https://pixe.la/v1/users/mamo/graphs/jdi943",
           headers=headers, json= pixle_param
                      )
print(pixl.text)


pixle_param= {
    "quantity": "1",
}
pixle = requests.put(url=f"https://pixe.la/v1/users/mamo/graphs/{id}/{date}",
           headers=headers, json= pixle_param
                      )
print(pixle.text)