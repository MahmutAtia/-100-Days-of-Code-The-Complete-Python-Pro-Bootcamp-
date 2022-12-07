from flask import Flask, render_template
import random
import datetime
from helper import *

app= Flask(__name__)



@app.route("/")
def run():
    randomnum= random.randint(1,199)
    year = datetime.datetime.now().date()

    return render_template("index.html", num=randomnum,date =year)
@app.route("/<string:name>")
def geuss(name):
    age , gender = predict(name)
    return render_template("geuss.html", name= name, age =age , gender=gender)

@app.route("/blog")
def blog():
    post = posts()
    return render_template("blog.html",post=post)




if __name__=="__main__":
    app.run(debug=True)
