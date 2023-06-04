from flask import Flask, render_template, request

app = Flask(__name__, static_folder=".", static_url_path="")


@app.route("/")
def home():
    thing = request.args.get("thing")
    height = request.args.get("height")
    color = request.args.get("color")
    return render_template("home.html", thing=thing, height=height, color=color)


app.run(port=5000, debug=True)
