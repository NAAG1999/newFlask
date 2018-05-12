from flask import Flask, render_template

app = Flask(__name__)

#Routing/mapping : whenever user goes to home page, return's output is shown
@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)



if __name__ == "__main__":
    app.run() #kickoff webserver : starts the app

