from tkinter import *
from  tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    l = [random.choice(letters) for _ in range(random.randint(6,8))]
    n = [random.choice(numbers) for _ in range(random.randint(1,3))]
    s = [random.choice(symbols) for _ in range(random.randint(1,3))]
    password_list= l+n+s
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    passinput.insert(0 , password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    try:
        with open("password manger.json", "r") as f :
            louded_data = json.load(f)
            try:
                louded_dic = louded_data[webinput.get()]
            except KeyError:
                messagebox.showinfo(title="wrong input", message="there is no such website in your list")

    except FileNotFoundError:
        messagebox.showinfo(title= "wrong input" , message= "there is no such website in your list")
    else:
        messagebox.showinfo(title= webinput.get() , message= f"your email is {louded_dic['email']}"
                                                             f"your password is {louded_dic['pass']}")

def add():

    web =webinput.get()
    email=emailinput.get()
    passw= passinput.get()
    dic = {web: {"email": email,
                 "pass" : passw}}
    if len(web) == 0 or len(passw) == 0 :
        info = messagebox.showinfo(title=web, message=f"you have empty fields ")
    else:
        is_ok = messagebox.askokcancel(title= web, message= f"do you want to save password : {passw} to {web}")
        if is_ok:
            try:
                with open("password manger.json", "r") as f:
                    data = json.load(f)
                    data.update(dic)
            except:
                with open("password manger.json", "w") as f:
                   json.dump(dic,f)
            else:
                with open ("password manger.json", "w") as f:
                    json.dump(data,f)

            webinput.delete(0, 'end')
            emailinput.delete(0, 'end')
            passinput.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")


window.config(pady=50, padx=50)
img = PhotoImage(file= "logo.png")
canvas = Canvas(height= 200, width= 200)
canvas.create_image(100,100,image= img)
canvas.grid(row= 0, column= 1)
lweb = Label(text= "Website: ")
lweb.grid(row=1, column=0 )
webinput = Entry( width= 36)
bsearch = Button(text= "Search", command= search)
bsearch.grid(row=1, column=3)

webinput.grid(row= 1, column=1 , columnspan=2)

lemail = Label(text= "Email: ")
lemail.grid(row=2, column=0 )
emailinput = Entry( width= 36)
emailinput.insert(END, "mahmod02015@gmail.com")
emailinput.grid(row= 2, column=1 , columnspan=2)


lpass= Label(text= "Password: ")
lpass.grid(row=3, column=0 )
passinput = Entry( width= 17)
passinput.grid(row= 3, column=1 )
bpass = Button(text= "Generate Password", width=15, command=generate_pass )
bpass.grid(row=3, column=2)



badd=Button(text= "Add",width= 36, command= add )
badd.grid(row=4, column=1, columnspan=2)


window.mainloop()