import pandas as pd

#TODO 1. Create a dictionary in this format:
df = pd.read_csv("./nato_phonetic_alphabet.csv")
dic= {}
for (index , row) in df.iterrows():
    dic[row.letter] = row.code


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def run():
    user_input = input("write a word")
    try:
        list = [dic[letter.upper()] for letter in user_input]
    except:
        print(" sorry , you have to enter a word")
        run()
    else:
        print(list)

run()

