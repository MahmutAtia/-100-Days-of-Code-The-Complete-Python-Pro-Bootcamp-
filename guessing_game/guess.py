import random



num =random.randint(0,100)
attempt = None
app = 10

while app > 0:
    chosen = int(input("geuss a number"))
    if chosen- num > 20 :
        print("too high")
    if chosen -num < -20 :
        print("too low")
    if chosen - num > 10:
        print("high")
    if chosen - num < -10:
        print("low")
    if chosen - num > 5:
        print(" slightly high")
    if chosen - num < -5:
        print("slightly low")

    if app <= 9:
     if abs(chosen - num) < abs(attempt-num):
        print("you did better than last time")
    else:
        print("try better geuss")
    attempt = chosen
    if chosen == num :
        print("well done")
    app -= 1