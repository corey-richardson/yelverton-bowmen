from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from commitee import committee_members

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

# SET SUBNAV LINK LABELS HERE
index_subnav = ["Welcome", "Beginners", "Useful Links"]
club_subnav = ["Committee"]

@app.route('/', methods = ["GET","POST"])
def index():
    return render_template("index.html", 
                           subnav_bar=index_subnav)

@app.route('/club', methods = ["GET","POST"])
def club():
    return render_template("club.html", 
                           subnav_bar=club_subnav, committee_members=committee_members)