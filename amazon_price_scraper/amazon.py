import requests
from bs4 import BeautifulSoup
import smtplib as stm

def get_price(url ,check):
    header = {
        "Accept-Language":"tr,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"
    }
    response = requests.get(url= url, headers= header)
    soup =  BeautifulSoup(response.text, "lxml")
    price = soup.find_all("span", class_= "a-offscreen")
    p_text = price[0].text
    p_int =float(p_text.split("$")[1])
    if p_int <= check:
        email(p_int)


def email(price):
    with stm.SMTP("smtp.gmail.com") as connection:
        pas = "0201502015"
        email = "manomamo100@gmail.com"
        connection.starttls()
        connection.login( user= email , password= pas)
        connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:Happy Birth Day \n\n {price}")

get_price("https://www.amazon.com/dp/B09KXY67M2/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B09KXY67M2&pd_rd_w=uXRrL&content-id=amzn1.sym.3be1c5b9-5b41-4830-a902-fa8556c19eb5&pf_rd_p=3be1c5b9-5b41-4830-a902-fa8556c19eb5&pf_rd_r=RN879QRZ31YV007AC603&pd_rd_wg=O7b5Q&pd_rd_r=fd714e27-eddb-4868-bb00-e6a9469e7c93&s=industrial&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSzZaRjVLTFZPUjk0JmVuY3J5cHRlZElkPUEwMjA0ODAzMTNTNzdCRU9HRjgyOCZlbmNyeXB0ZWRBZElkPUExMDM1NDM5MjNZS0wzVUFJWEFFViZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
          10)