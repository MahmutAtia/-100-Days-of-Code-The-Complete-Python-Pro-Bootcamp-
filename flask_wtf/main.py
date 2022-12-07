from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, EmailField ,SubmitField, DateField
from wtforms.validators import DataRequired ,Email, Length
from flask_bootstrap import Bootstrap
class MyForm(FlaskForm):
    addres =EmailField("Enter your email", validators=[DataRequired(), Email(message="Enter a valid email"),Length(min=6 , max=30)])
    pas = PasswordField("enter your password", validators=[DataRequired(),Length(min=6 , max=18)])
    bith = DateField("enter your birthday", validators=[])
    submit= SubmitField("submit")

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.secret_key = "mamo"
    return app
app = create_app()

@app.route("/")
def home():
    return render_template('index.html')




@app.route("/login", methods=["POST", "GET"])
def login():
    form = MyForm()

    if form.validate_on_submit():
       if form.addres.data=="admin@email.com" and form.pas.data=="12345678":
            return render_template("success.html")
       else:
        return render_template("denied.html")
    return render_template("login.html",form=form)






if __name__=="__main__":
    app.run(debug=True)