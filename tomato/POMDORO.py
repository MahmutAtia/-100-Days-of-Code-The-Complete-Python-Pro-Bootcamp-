import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- count down ------------------------------- #

def reset_timer():
    win.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    rania_POMDORO.config(text="Timer")
    #check_marks.config(text="")
    global reps
    reps = 0
def count_down(count):
    global timer
    mins = int(count / 60)
    sec = count % 60
    if sec <= 9:
        sec= f"0{sec}"
    canvas.itemconfig(canvas_text, text=f"{mins}: {sec}")

    if count > 0:
       timer = win.after(1000,count_down ,count-1)

def pause():
        time.sleep(5)


def start_timer():
    global reps
    reps += 1
    if reps == 1:
        count_down(WORK_MIN)
        rania_POMDORO.config(text="Rania's POMDORO" ,font=(FONT_NAME, 35 , "bold" ), bg= YELLOW)
        canvas.itemconfig(canvas_image , image= image)

    elif reps == 2 :
        count_down(SHORT_BREAK_MIN)
    elif reps == 3:
        rania_POMDORO.config(text="work hard canim", font=(FONT_NAME, 35, "bold"), bg=YELLOW)
        canvas.itemconfig(canvas_image, image=image2)
        count_down(WORK_MIN)
    elif reps == 4:
        count_down(SHORT_BREAK_MIN)
    elif reps == 5 :
        count_down(WORK_MIN)
    elif reps == 6:
        count_down(SHORT_BREAK_MIN)
    elif reps == 7:
        count_down(WORK_MIN)
    elif reps == 8:
        count_down(LONG_BREAK_MIN)
        reps = 0
# ----------------------------The APP ------------------------------- #

win = Tk()
win.minsize(height= 400, width= 500)
win.title("POMDORO")
win.config(pady= 50 , padx= 100, bg= YELLOW, highlightthickness= 0)


rania_POMDORO = Label(text="Rania's POMDORO" ,font=(FONT_NAME, 35 , "bold" ), bg= YELLOW)
rania_POMDORO.grid(row=1, column=2)


#Canvas
image = PhotoImage(file= "./tomato.png")
image2 = PhotoImage(file="./png-transparent-orange-nutrient-health-vitamin-c-food-orange.png")
canvas = Canvas(height= 250, width= 250,bg= YELLOW)
canvas_image = canvas.create_image(130,130 , image= image)
canvas_text = canvas.create_text(130, 130 , text="00:00", fill= "white", font= (FONT_NAME, 35 , "bold"))
canvas.grid(row= 2, column= 2)



start = Button(text= "Start", command= start_timer, highlightthickness=0 )
start.grid(row=3, column=1)

reset = Button(text= "Reset", highlightthickness = 1, command= reset_timer)
reset.grid(row=3, column=3)




win.mainloop()
