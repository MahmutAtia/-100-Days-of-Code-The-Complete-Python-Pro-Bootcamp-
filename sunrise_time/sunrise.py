import requests
import datetime as dt
import smtplib as smtp

'''---------------------to get when it is dark ---------------------------------------'''
params = {"lat": 39.933365 , "lng":32.859741, "formatted":0}
response = requests.get(url = "https://api.sunrise-sunset.org/json", params= params)
sunrise= response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]

hour_rise ,minute_rise = int( sunrise.split("T")[1] .split(":")[0]) +3 ,sunrise.split("T")[1] .split(":")[1]
hour_set ,minute_set = int( sunset.split("T")[1] .split(":")[0]) +3 ,sunset.split("T")[1] .split(":")[1]

now  = dt.datetime.now()


'''------------------------------- to get the loc of iss___________________________'''
iss_respose= requests.get(url= "http://api.open-notify.org/iss-now.json")
lng = iss_respose.json()["iss_position"]["longitude"]
lat = iss_respose.json()["iss_position"]["latitude"]


#"___________________________________________ Ankara lag and lat___________________________"
lng_ankara=32.859741
lat_ankara=39.933365


'''---------------------------- sending email__________________'''
if (lng_ankara,lat_ankara) == (lng,lat):
    pas = "0201502015"
    email = "manomamo100@gmail.com"
    with  smtp.SMTP("smtp.gmail.com") as new_connection:
        new_connection.starttls()
        new_connection.login(user= email, password= pas)
        new_connection.sendmail(from_addr= email , to_addrs= email , msg= f"Subject: iam here \n\n good morrning {lng , lat}")






print(now.hour,now.minute)