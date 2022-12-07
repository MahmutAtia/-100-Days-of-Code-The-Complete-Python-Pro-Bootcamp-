import  requests
from twilio.rest import Client
import os
import twilio.rest


lat = 40.552750
lon = 34.959419

def will_rain(in_next_hours : int, lat :int,lon:int,msg, from_num , to_num) -> str:
    key = "cd3e6953e2b734b193a9eddaf428b200"
    param = {"lat": lat, "lon": lon, "appid": key, "exclude": "current,minutely,daily,alerts"}
    response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=param)
    dic = response.json()
    rain = False
    for i in dic["hourly"][0:in_next_hours]:
        w_id = i["weather"][0]["id"]
        if w_id < 700:
            rain = True
    if rain == True :
        send_massage(msg, from_num , to_num)

def send_massage(msg , from_num , to_num):

    account_sid = "ACa43ce72e300e26dc1b8cc0b5b3d5aaec"
    auth_token = "77d78a91761c9cad74ecb18b9b126cc5"
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=msg,
        from_=from_num,
        to=to_num
    )

    print(message.sid)
will_rain(5,lat,lon, "it is rainig", "+19785408307", "+905050782635")
