from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/files'

login_manager= LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return User.query.get(int(user_id))

db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":

        new_row = User(email=request.form.get("email"), password= generate_password_hash(password=request.form.get("password"),
                                                                                         salt_length=8), name=request.form.get("name"))
        print(request.form.get("email"))
        print(User.query.all())
        db.session.add(new_row)
        db.session.commit()


        return render_template("secrets.html" , name=request.form.get("name") )
    return render_template("register.html")


@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        mail= request.form.get("email")
        user = User.query.filter_by(email=mail).first()
        if user:
            if check_password_hash(user.password,request.form.get("password")):
                login_user(user) #you have to use it to login
                return redirect(url_for("secrets", name=user.name))

            else:
                flash("there is no such password")
        else:
            flash("there is no such email")

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    print(current_user)
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download/<filename>')
def download():
    return send_from_directory(directory='', path='static/files/cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
