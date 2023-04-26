from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

# SET SUBNAV LINK LABELS HERE
index_subnav = ["Welcome", "Beginners", "Useful Links"]
club_subnav = ["Committee"]
records_subnav = ["Barebow","Recurve","Compound","Longbow","AFB"]

@app.route('/', methods = ["GET","POST"])
def index():
    return render_template("index.html", 
                           subnav_bar=index_subnav)

from commitee import committee_members

@app.route('/club', methods = ["GET","POST"])
def club():
    return render_template("club.html", 
                           subnav_bar=club_subnav, committee_members=committee_members)


from static.records.barebow import barebow
from static.records.recurve import recurve
from static.records.compound import compound
from static.records.longbow import longbow
from static.records.afb import afb

bowtypes = {"Barebow" : barebow,
            "Recurve" : recurve,
            "Compound" : compound,
            "Longbow" : longbow,
            "American Flatbow" : afb}

@app.route('/records', methods = ["GET","POST"])    
def records():
    return render_template("records.html",
                           subnav_bar=records_subnav,
                           bowtypes=bowtypes,
                           barebow=barebow,
                           recurve=recurve,
                           compound=compound,
                           longbow=longbow,
                           afb=afb)