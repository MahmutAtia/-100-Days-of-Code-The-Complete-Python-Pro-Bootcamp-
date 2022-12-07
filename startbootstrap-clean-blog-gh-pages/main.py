from flask import Flask, render_template,request
import requests
import smtplib as smt

pas = "0201502015"
email = "manomamo100@gmail.com"
def send(email, pas,name , text ):
    with smt.SMTP("smtp.gmail.com") as new_connection:
        new_connection.starttls()  # for security
        new_connection.login(user="manomamo100@gmail.com", password=pas)
        new_connection.sendmail(from_addr="manomamo100@gmail.com", to_addrs="manomamo100@gmail.com", msg=f"Subject:{name} \n\n {text}")


response = requests.get(url="https://api.npoint.io/fda471bf944972811882").json()
app= Flask(__name__)
@app.route("/")
@app.route(("/<name>"))
def run(name=None, json= response):
    if name != None:
        return render_template(f"{name}.html", name=name , json=json,  msg= "Contact me")
    else:
        return render_template("index.html", name=name, json=json)

@app.route("/post/<int:id>")
def get_post(id,json= response):

    return render_template("post.html", id=id, json=json)
@app.route("/form-entry" , methods=["post"])
def recive():
    email = request.form['email']
    name = request.form['name']
    msg=request.form['msg']
    num= request.form['num']
    text= f" phone number : {num} msg : {msg} , {email}"
    try:
        send(email,pas, name ,text)
        return render_template("contact.html", msg="Successfully sent message")
    except:
        return render_template("contact.html", msg="your message couldn't be sent")


if __name__== "__main__":
    app.run(debug=True)


send("DAGGS", pas, "dsag", "SDAg" ,"sDAF ")
