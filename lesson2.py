from flask import Flask

app = Flask(__name__)

#Routing/mapping : whenever user goes to home page, return's output is shown
@app.route('/')
def index():
    return "This is the homepage"

@app.route('/profile')
def profile():
    return "<h2>Hey There, Welcome</h2>"

@app.route('/profile/ABC')
def any():
    return "<h2>Hey There, Welcome Again</h2>"

@app.route('/post/<username>')
def post(username):
    return "<h2>Hey There %s</h2>" % username

@app.route('/post/<int:post_id>')
def post_1(post_id):
    return "<h2>Hey There id no %s</h2>" % post_id

if __name__ == "__main__":
    app.run(debug=True) #kickoff webserver : starts the app

