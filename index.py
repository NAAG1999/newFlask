from flask import Flask, render_template

app = Flask(__name__)

#Routing/mapping : whenever user goes to home page, return's output is shown
@app.route("/")
#@app.route("/<user>")
#def index(user = None):
#    return render_template("user.html", user=user)

@app.route("/shopping")
def shopping():
    food = ["cheese", "curd", "rice"]
    return render_template("shopping.html", food= food)


if __name__ == "__main__":
    app.run(debug=True) #kickoff webserver : starts the app

