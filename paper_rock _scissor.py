import os
import random


app = "yes"

rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  '''

paper = '''
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
  '''

scissors = '''
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  '''
user = 0
pc = 0
while app == "yes":
      os.system("CLS")
      pl = input(" 0 for Paper , 1 for  Scissors or 2 for Rock")
      inp = int(pl)
      player = [paper, scissors, rock][inp]

      rand = random.choice([paper, scissors, rock])
      print(player)
      print(rand)

      if player == rand:
            result = ("play again")
      if player == rock and rand == scissors:
            result = ("you win ")
      if player == rock and rand == paper:
            result =("you lose ")
      if player == scissors and rand == rock:
            result =("you lose ")
      if player == scissors and rand == paper:
            result =("you win ")
      if player == paper and rand == rock:
            result =("you win ")

      if player == paper and rand == scissors:
            result =("you lose ")
      print(result)
      if result == "you lose ":
            pc = pc +1

      if result == "you win ":
            user = user +1

      print(f"result Pc {pc} : user {user}")
      user_input = input("y or n")
      if user_input == "n":
            app = "no"
