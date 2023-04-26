from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from commitee import committee_members

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route('/', methods = ["GET","POST"])
def index():
    return render_template("index.html")

@app.route('/club', methods = ["GET","POST"])
def club():
    return render_template("club.html", committee_members=committee_members)