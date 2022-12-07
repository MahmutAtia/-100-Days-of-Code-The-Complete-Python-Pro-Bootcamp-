easy = 10
hard =5

def diff():
    hard_easy = input("chose hard or easy")
    if hard_easy == "hard":
         return hard
    if hard_easy == "easy":
        return easy
    else:
        print("please write hard or easy")


def check(user_input , answer , turns):
    if user_input > answer :
        print("too high")
        turns -=1
        print(f"you only have {turns} attempts")
        return turns
    if user_input < answer:
        print("too low")
        turns -= 1
        print(f"you only have {turns} attempts")
        return turns

    else:
        print("congratulation you won the number is {}".format(answer))


