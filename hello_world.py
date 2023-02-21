from flask import Flask, render_template

#importing an object of class Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    
    return render_template('hello.html')

