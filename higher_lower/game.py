import random
from data import *
import os
# 1- take two elemant from the list randomly
# 2- compare as output
# 3- take input
# 4- score and continu or break



old_chosen = []
score = 0
high = random.choice(data) # i did these because i want he elemant with higher followers to be up every time
while True :
    ''' i want chose every elemant one time and begine with  the elemant with higher followers '''

    os.system("CLS")


    up = high
    down = random.choice(data)
    while down in old_chosen:
        down = random.choice(data)
        if old_chosen == data:
            break

    if old_chosen == data:
        print("you are the best player")
        print(f"your score is {score} ")
        break



    old_chosen.append(down)



    print(logo)
    print(f"up : {up['name']}, a {up['description']}, from {up['country']}")
    print(vs)
    print(f"down : {down['name']}, a {down['description']}, from {down['country']}\n")
    print("what do you think who has more followers? up or down\n\n")
    user = input("a for up ,b down")




    if user == "a" and up["follower_count"] > down["follower_count"]:
        score += 1
        print(f"your score is {score}")
        high = up
    elif user == "b" and down["follower_count"] > up["follower_count"]:
        score += 1
        print(f"your score is {score}")
        high = down

    else:
        print(f"you lost , your score : {score}")
        break
