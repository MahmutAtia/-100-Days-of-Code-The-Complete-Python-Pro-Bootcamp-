import random

from flask import Flask
app = Flask(__name__)



selected_num = 0
@app.route("/")
def higher_lower():
    global selected_num
    selected_num = random.randint(0,9)
    print(selected_num)
    return "<h1><b><em>Guess a number between 0 and 9</em></b></h1>"\
           "hr"\
           "<img style{display: block;} src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:num>")
def guess(num):
    if int(num) == selected_num:
        return "<h1 style='color:red; font-size:30px;' ><b><em>You found it</em></b></h1>"\
               "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"

    elif  int(num) < selected_num:
        return "<h1><b><em>too high,please try agian</em></b></h1>"             \
               "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
                

    elif int(num) > selected_num:
        return "<h1><b><em>too low,please try agian</em></b></h1>"\
               "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"



if __name__ == "__main__":
    app.run(debug=True)