from constants import *

def plist(list) :
    x=""
    for i in list:
        x+=i
    print(x)
    return (x)


def check(word, space, stages):
    lives = 6
    end = False
    inp = input("enter a letter")


    for i in range(len(word)) :
        if inp == word[i]:
            space[i] = word[i]

    if inp not in word :
        lives -= 1
        print(f"you have {lives}")
        if lives == 0:
            end = True






