from flask import Flask
from test import *
import random
app = Flask(__name__)


@app.route('/')
@make_bold
def hello_world():
    return '<b>Hellorglöe mlöher</b>'




if __name__ == "__main__":
    app.run(debug= True)
