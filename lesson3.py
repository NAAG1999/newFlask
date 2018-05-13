from flask import Flask, request

app = Flask(__name__)

#Routing/mapping : whenever user goes to home page, return's output is shown
@app.route('/')
def index():
    return "Method used : %s" %request.method

@app.route('/bacon',methods=['GET', 'POST'])
def bacon():
    return "Method used : %s" %request.method

#to use POST method



if __name__ == "__main__":
    app.run(debug=True) #kickoff webserver : starts the app
