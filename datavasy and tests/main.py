from flask import request
from flask import Flask
from markupsafe import escape
from flask import url_for, redirect, url_for
from flask import render_template


app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_get()
    else:
        return login_get()

@app.route('/login')
def login_get():
    return render_template("login.html")


@app.route('/login')
def login_post():
    person = request.args.get['username']
    return render_template('profile.html', person=person)

@app.route('/profile')
def profile():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=15000)