import requests
import datetime as dt
from sinchsms import SinchSMS
import time


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
key = "2HE60GKT2YE65O16."
param= {"function": "TIME_SERIES_DAILY",
        "symbol":STOCK,
        "apikey":key
        }

'''-----sms______________'''


def sendSMS(msg):
    # enter all the details
    # get app_key and app_secret by registering
    # a app on sinchSMS
    number = '+447520650996'
    app_key = '25e62cde029a46a6b7d3a372d1810239'
    app_secret = '36e6e53730b74032b2015531ca226ba9'

    # enter the message to be sent
    message = msg

    client = SinchSMS(app_key, app_secret)
    print("Sending '%s' to %s" % (message, number))

    response = client.send_message(number, message)
    message_id = response['messageId']
    response = client.check_status(message_id)

    # keep trying unless the status returned is Successful
    while response['status'] != 'Successful':
        print(response['status'])
        time.sleep(1)
        response = client.check_status(message_id)

    print(response['status'])


'''-----------------------------news------------------------------'''

def get_news(diff):
    api = "1a35559447804076a51cebebafaf4001"
    response_news = requests.get(url=f"https://newsapi.org/v2/everything?q=tesla&from={date_yester}&sortBy=publishedAt&apiKey={api}")
    news =  response_news.json()["articles"][:3]
    i=0
    titls= []
    for new in news:
        i+=1
        titls.append(f"{i}- "+new['title'])
    return (f"{STOCK}: 🔺{diff}%\n{titls[0]}\n{titls[1]}\n{titls[2]}\n")
'''_________________________________________ diff between today and yesterday________________'''
now = dt.datetime.now()
date = now.date()
date_today = f"{date.year}-0{date.month}-{date.day-4}"
date_yester = f"{date.year}-0{date.month}-{date.day-5}"
response = requests.get(url="https://www.alphavantage.co/query", params=param)
stock_today = response.json()["Time Series (Daily)"][f"{date_today}"]["4. close"]
stock_yester = response.json()["Time Series (Daily)"][f"{date_yester}"]["4. close"]
print(stock_yester,stock_today)
diff = abs(float(stock_today)/float(stock_today) - float(stock_yester)/float(stock_today))

if diff*100 > 5 :
    msg = get_news(diff*100)
    print(msg)




## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.







## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

