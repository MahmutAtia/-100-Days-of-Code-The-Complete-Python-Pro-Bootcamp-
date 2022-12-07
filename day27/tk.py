from tkinter import *

window = Tk()
window.title("app")
window.minsize(200 ,200)

#lable
my_lable = Label(text="welcome")
my_lable.grid(column=1 ,row=1)
#entry
my_entry = Entry(width= 10)
my_entry.insert(END, "i love you")
my_entry.grid(column=2,row=2)

#text
my_text = Text(height= 2, width= 10)
my_text.insert(END , "my list")
my_text.grid(column=3 ,row=1)
#button
def show():
    my_lable.config(text=f"{my_entry.get()}")

def add():
    my_text.insert(END , "A")
#spinbox
#my_spinbox = Spinbox(from_= 0 , to= 10 , command= add)
#my_spinbox.pack()

my_button = Button(text="click me", command= show)
my_button.grid(column=4 ,row=4)













window.mainloop()