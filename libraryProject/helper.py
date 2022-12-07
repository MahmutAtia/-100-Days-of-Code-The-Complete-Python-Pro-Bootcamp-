from flask_wtf import FlaskForm
from wtforms import StringField,SelectField, SubmitField
from wtforms.validators import  DataRequired

class AddBook(FlaskForm):
    book_name= StringField("Book Name", validators=[DataRequired()])
    book_auther = StringField("Book Auther")
    rating = SelectField("Rating",choices=range(6) , validators=[DataRequired()] )
    submit = SubmitField("Add a new book")



