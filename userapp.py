from flask import Flask,render_template

user = Flask(__name__)

@user.route('/')
def login():
    return render_template("login.html")

@user.route('/')
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    user.run()
