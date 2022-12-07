from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

cafe=Cafe()
@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/all", methods=["get"])
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    cafes = db.session.query(Cafe).all()

    cafes2= Cafe.query.all()
    return  jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route("/search")
def get_location():
    if request.method == "GET":
        loc = request.args.get("loc")
        cafes_by_loc = Cafe.query.filter_by(location=loc)
        if cafes_by_loc:
            return jsonify(cafes= [cafe.to_dict() for cafe in cafes_by_loc])
        else:
             return jsonify(erros= {"notfound": "no data"})
## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>")
def patch_new_price(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffe_price= "5euro"
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    else:
        return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP DELETE - Delete Record
@app.route("/report-closed/<id>" , methods=["GET","DELETE"])
def delet(id):
    api_key = request.args.get("api-key")
    if api_key== "mamo":
        cafe = db.session.query(Cafe).get(id)
        if cafe:
            db.session.delete(cafe)
            print(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully added the new cafe."})
        else:
            return jsonify(notfound={"ERROR": "Successfully added the new cafe."})
    else:
        return jsonify(notallowed={"ERROR": "Successfully added the new cafe."})


if __name__ == '__main__':
    app.run(debug=True)
