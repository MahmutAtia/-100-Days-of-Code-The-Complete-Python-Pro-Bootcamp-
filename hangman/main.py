from replit import clear
import random
from hangman.hangman_helper import *
from constants import *

print(logo)
print("start the game")
print(" guess the word which has the same number of letters '_'")

word = random.choice(word_list)
space = []
lives = 6
for i in word:
    space += "_"
end = False
while not end :
    plist(space)


    inp = input("enter a letter")
    clear()
    for i in range(len(word)):
        if inp == word[i]:
            space[i] = word[i]

    if inp not in word:
        lives -= 1


        if lives == 0:
            end = True
            print("You lose.")
            print("the word is  :"+word)

    if "_" not in space:
        end =True
        print("you win")
        w = plist(space)
        print(f"the word is {w} ")
    print(stages[lives])
