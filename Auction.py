import os
dic = {}
app = "yes"
while app == "yes":
    name = input("enter your name")
    price = int(input("enter your price"))
    dic[name] = price
    app= input("enter yes or no")
    os.system("CLS")
ma = max(dic.values())
winner = list(dic)[list(dic.values()).index(ma)]
print("the winner is "+winner + " with "+str(ma) +"$")
