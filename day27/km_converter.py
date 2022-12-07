from tkinter import *


window = Tk()
window.title("convert mile to km")
window.config(padx= 10 , pady= 10)
#window.minsize(height= 100 , width= 220)

#func
def click():
    miles = float(my_entry.get())
    print(miles)
    km = miles * 1.60934
    my_lable2.config(text= f"{km}")





#frist column
my_lable = Label(text= "is equal to")
my_lable.grid(column=1,row=2)

#second column
my_entry = Entry(text="0", width= 7)
my_entry.grid(column=2 , row= 1)

my_lable2 = Label(text="0")
my_lable2.grid(column=2 , row= 2)

my_button = Button(text="click", command= click )
my_button.grid(column=2, row=3)

#third column
my_lable3 = Label(text="miles")
my_lable3.grid(column=3 , row= 1)

my_lable4 = Label(text="KM")
my_lable4.grid(column=3 , row= 2)













window.mainloop()
