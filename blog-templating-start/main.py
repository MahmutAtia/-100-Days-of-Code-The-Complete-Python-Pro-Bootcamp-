from flask import Flask, render_template
from post import posts


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts= posts)

@app.route("/post/<int:id>")
def get_post(id):

    return render_template("post.html", posts= posts, id=id)
if __name__ == "__main__":
    app.run(debug=True)
