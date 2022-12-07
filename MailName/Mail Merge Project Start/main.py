#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# 1- open names  2- make list of names

with open("./input/Names/invited_names.txt" , mode = "r") as f :
    names = f.read()
list_names = names.split("\n")
print(list_names)

#1- open emails 2- find [name]

with open("./input/Letters/starting_letter.txt", mode= "r") as f1:
    letter = f1.read()


#1-save the new letters

for i in list_names:
    new_letter = letter.replace("[name]", i)
    with open(f"./Output/ReadyToSend/{i}_letter.txt" , "w") as f3 :
        f3.write(new_letter)


