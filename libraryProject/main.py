from flask import Flask, render_template, request, redirect, url_for
from helper import AddBook
from flask_bootstrap import Bootstrap
import sqlite3

db = sqlite3.connect("mybooks.db",check_same_thread=False)
cursor = db.cursor()
#cursor.execute("CREATE TABLE books(id INT PRIMARY KEY, title VARCHAR(30), auther VARCHAR(30), rating FLOAT)")

#db=sqlite3.connect("books.db")
#cursor=db.cursor()
#cursor.execute("DROP TABLE books")
#cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title VARCHAR(250) NOT NULL , auther VARCHAR(250), rating FLOAT NOT NULL)")





app = Flask(__name__)
app.config['SECRET_KEY']= "12345678"
Bootstrap(app)



all_books=[]


@app.route('/')
def home():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    title = request.args.get("book")
    print(title)
    cursor.execute("DELETE FROM books\
                   WHERE books.title = :title", {"title":title})
    db.commit()

    print(title)
    return render_template("index.html", books=books)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddBook()
    if form.validate_on_submit():
        all_books.append(form.data)
        title = all_books[0]['book_name']
        auther = all_books[0]['book_auther']
        rating = all_books[0]['rating']

        cursor.execute("INSERT INTO books(title, auther, rating) VALUES(?,?,?)", (title,auther,rating))
        db.commit()
        return redirect(url_for("home"))

    return render_template("add.html", form=form)
@app.route("/rating", methods=["POST","GET"])
def change_rating():



    if request.method=="POST":
      book_title = request.form["book"]
      new_rating= request.form["rate"]
      cursor.execute("UPDATE books\
                     SET rating= :rating\
                     where title= :title", {"rating": new_rating, "title": book_title})
      db.commit()


      return redirect(url_for("home"))
    book = request.args.get("book_title") # you have to capture the keyword from url_for before doing a post request and if you want it agian you habe to add it again as a hidden input
    return  render_template("rating.html", book_name=book)

if __name__ == "__main__":
    app.run(debug=True)

