import json
import random
import time
from tkinter import *
import pandas as pd



BACKGROUND_COLOR = "#B1DDC6"

'''----------------------------funcs-------------------------------------------------------'''
known_words = []
df = {"Frensh" : [], "English":[] }
data = pd.read_csv("data/french_words.csv")
data_dic = data.to_dict(orient="records")
ran_word = random.choice(data_dic)


def back_card():
    canvas1.itemconfig(word, text=ran_word["English"], fill="white")
    canvas1.itemconfig(lang, text="English", fill="white")
    canvas1.itemconfig(img, image=card_back)
def right():
    global ran_word, flip_timer
    ran_word = random.choice(data_dic)
    known_words.append(ran_word["French"])
    print(known_words)
    canvas1.itemconfig(word, text= ran_word["French"],fill ="black")
    canvas1.itemconfig(lang, text="French", fill="black")
    canvas1.itemconfig(img, image=card_front)

    flip_timer = window.after(10000,func= back_card)





def wrong():
    global ran_word, flip_timer
    flip_timer = window.after_cancel(flip_timer)
    new = {"French" : ran_word["French"] ,"English" :  ran_word["English"] }
    df.append(new)
    print(df)

    ran_word = random.choice(data_dic)

    print(known_words)
    canvas1.itemconfig(word, text=ran_word["French"], fill="black")
    canvas1.itemconfig(lang, text="French", fill="black")
    canvas1.itemconfig(img, image=card_front)

    flip_timer = window.after(10000, func=back_card)






'''_________________________________ UI ______________________________________________________'''
window = Tk()
window.config(bg= BACKGROUND_COLOR, padx= 50, pady=50,width= 900, height= 625 )
window.title("Learn French with flash cards")
flip_timer = window.after(10000, func=back_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas1 = Canvas(width=800, height= 526, bg= BACKGROUND_COLOR, highlightthickness= 0)
img = canvas1.create_image(400,263,image= card_front)
lang = canvas1.create_text(400, 150,text="French", font=("Ariel", 40 ,"italic"), fill= "black")
word = canvas1.create_text(400, 263,text= ran_word["French"], font=("Ariel", 60 ,"bold"), fill= "black" )

canvas1.grid(row= 0, column=0 ,columnspan= 2)

yes = PhotoImage(file= "images/right.png")
byes = Button(image=yes, highlightthickness= 0, command= right)
byes.grid(row= 1, column= 0)


no = PhotoImage(file= "images/wrong.png")
bno= Button(image= no, highlightthickness= 0, command= wrong)
bno.grid(row= 1, column= 1)











window.mainloop()