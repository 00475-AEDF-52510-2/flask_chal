from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user_list = [
        {"username": "traveler", "name": "Alex"},
        {"username": "photographer", "name": "Sam"},
        {"username": "gourmet", "name": "Chris"}
    ]

    return render_template("index.html", user_list=user_list)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
