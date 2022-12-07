from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    canvas.itemconfig(timer_text,text= count)
    win.after(1000, count_down, count-1)
    print(count)

# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("pomdoro app")
win.config(padx=100 ,pady= 50, bg= YELLOW)





image = PhotoImage(file= "./tomato.png" )
canvas = Canvas(width=220,height=299,bg= YELLOW )
canvas.create_image(112,183,image= image)
timer_text = canvas.create_text(112,190, text="00.00", fill= "white", font=( "Courier", 35, "bold"))
canvas.pack(side= "top")
count_down(20)
'''#row1
work_break = Label(text= "start", width= 60, height= 30 )
work_break.grid(row=1,column=2)'''
'''#row3
start = Button(text= "Start")
start.grid(row =3,column=1)

reset = Button(text= "Reset")
reset.grid(row =3 , column=3)
'''









win.mainloop()