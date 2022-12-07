# try to write what do you want before starting
import random
import os
''' constants or global variables section '''
#             turns = None
#1- chose a random number from 1-100
#      answer = random.randint(1,100)
#2- set difficulty helper func
from v2_helper import diff

#3- let user input num
#      user = int(input("please guess a number between 1 and 100"))
#4- check the number func and 5- reduce attempt number
from v2_helper import check



#6- if wrong , rebeat




''' orgnization of the code '''

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    turns = diff()
    print("you have {} attempts".format(turns))
    user = 0
    while answer != user :
        user = int(input("please guess a number between 1 and 100"))
        turns = check(user , answer , turns)
        if turns == 0 :
            print("you lose")
            print("the correct number is {}".format(answer))
            break
        if answer != user and turns != 0 :
            print("try again")
        os.system("CLS")
game()