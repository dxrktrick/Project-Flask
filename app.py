from flask import Flask, render_template

#Application
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("/access.html")

#xdd
