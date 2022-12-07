from flask import Flask,render_template, request


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login" , methods=["post"])
def login():
    email=request.form['email']
    passw= request.form['pass']
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)