from flask import Flask
from test import *
app = Flask(__name__)




@app.route('/')
def hello_world():
    return 'Hello fdfs'

@app.route('/<name>')
@make_bold
def hello_name(name):
    return f'hallo{name}'

if __name__ == "__main__":
    app.run(debug= True )