##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as td
import random
import smtplib as smt
import pandas as pd

now = td.datetime.now()
month = now.month
day = now.day

'''____________________________________reading letters and modify_________________________________________________'''
num = random.randint(1,3)
with open(f"letter_templates/letter_{num}.txt", "r") as f:
    text = f.read()
'''----------------------------------------------------'''
info = pd.read_csv("birthdays.csv")
dic = {(row.day, row.month): row for index , row in info.iterrows()}



'''_________________________________sending email_______________________________'''
if (day,month) in dic:
    print("yes")
    text = text.replace("[NAME]",dic[(day,month)]["name"] )
    pas = "0201502015"
    email = "manomamo100@gmail.com"
    with smt.SMTP("smtp.gmail.com") as new_connection:
        new_connection.starttls()  # for security
        new_connection.login(user=email, password=pas)
        new_connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:Happy Birth Day \n\n {text}")








