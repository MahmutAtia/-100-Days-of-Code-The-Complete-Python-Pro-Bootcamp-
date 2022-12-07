import sqlite3

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

''' make sure there is no copy paste ',' any where and encode()'''



conn = sqlite3.connect("data.db",check_same_thread=False)
c=conn.cursor()


class edit_form(FlaskForm):
    rating= StringField("your rating out of 10", validators=[DataRequired()])
    review= StringField("your rewiew", validators=[DataRequired()])
    submit= SubmitField("Edit Movie")
class add_form(FlaskForm):
    title= StringField("Movie Title", validators=[DataRequired()])
    review= StringField("your rewiew", validators=[DataRequired()])
    submit= SubmitField("Edit Movie")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

@app.route("/", methods=["POST","GET"])
def home():
    '''All Movies'''
    c.execute('''SELECT * FROM films''')
    conn.commit()
    films = c.fetchall()
    '''Delete a movie'''
    if request.method=="GET":
        id =request.args.get("id")
        print(id)
        c.execute('''DELETE FROM films WHERE films.id =:id''', {"id":id})
        conn.commit()

    return render_template("index.html", films=films)


@app.route("/edit", methods=["POST","GET"])
def edit():
    form = edit_form()
    id =request.args.get("id")
    if form.validate_on_submit():
        c.execute(''' UPDATE films\
                     SET rating= :rating\
                     where id= :id''', {"rating": request.form.rating, "id": id})
        c.execute(''' UPDATE films\
                                 SET review= :review\
                                 where id= :id''', {"rating": request.form.review, "id": id})
        conn.commit()
        return redirect("home")

    return render_template("edit.html", form =form)


@app.route("/add", methods=["post", "get"])
def add():
    form = add_form()
    return render_template("add.html", form=form)
if __name__ == '__main__':
    app.run(debug=True)





















#c.execute("CREATE TABLE films (id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(30), year INT, description VARCHAR(250), rating FLOAT,ranking INT,review VARCHAR(250), img_url VARCHAR(250))"

title="Phon Booth".encode()
year="2002".encode()
description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.".encode()
rating=7.3
ranking=10
review="My favourite character was the caller.".encode()
img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg".encode()
id=2
#c.execute('''INSERT INTO films (title,year,description ,rating ,ranking,review,img_url) VALUES("Phone Booth",
#2002,"Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#7.3,10,"My favourite character was the caller.","https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")''')
#c.execute('''INSERT INTO films (title,year,description ,rating ,ranking,review,img_url) VALUES(:title,:year,:description ,:rating ,:ranking,:review,:img_url)''',
#          {"title":title, "year":year, "description":description,"rating" :rating,"ranking": ranking,"review": review,"img_url": img_url})
#conn.commit()

#c.execute('''INSERT INTO films (title,year,description ,rating ,ranking,review,img_url) VALUES(?,?,?,?,?,?,?)''',(title,year,description ,rating ,ranking,review,img_url))
#conn.commit()
