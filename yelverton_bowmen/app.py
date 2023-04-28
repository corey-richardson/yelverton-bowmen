from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# source bin/activate
# flask --debug run

# CLUB PAGE
from commitee import committee_members

# RECORDS ROOM PAGE
from static.records.barebow import barebow
from static.records.recurve import recurve
from static.records.compound import compound
from static.records.longbow import longbow
from static.records.afb import afb
bowtypes = {"Barebow" : barebow,
            "Recurve" : recurve,
            "Compound" : compound,
            "Longbow" : longbow,
            "American Flatbow" : afb }

# GALLERY PAGE
from os import scandir, path
directory = 'static/gallery'

# FLASK APP SETUP
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

# SET SUBNAV LINK LABELS HERE
index_subnav = ["Welcome", "Beginners", "Useful Links"]
club_subnav = ["Committee"]
records_subnav = ["Club Records", "Rounds and Classifications", "252 Scheme", "Frostbite Postal", "Portsmouth Postal"]

# INDEX PAGE
@app.route('/', methods = ["GET","POST"])
def index():
    return render_template("index.html", 
                           subnav_bar=index_subnav)

# CLUB PAGE
@app.route('/club', methods = ["GET","POST"])
def club():
    return render_template("club.html", 
                           subnav_bar=club_subnav, committee_members=committee_members)

# RECORDS ROOM PAGE
@app.route('/records', methods = ["GET","POST"])    
def records():
    return render_template("records.html",
                           subnav_bar=records_subnav)
    
# bowtypes=bowtypes,
# barebow=barebow,
# recurve=recurve,
# compound=compound,
# longbow=longbow,
# afb=afb

@app.route('/records/<bowtype>')
def bowtype_record(bowtype):
    match bowtype:
        case "afb":
            bowtype=afb
        case "barebow":
            bowtype=barebow
        case "compound":
            bowtype=compound
        case "longbow":
            bowtype=longbow
        case "recurve":
            bowtype=recurve
        case _:
            bowtype=barebow
    return render_template("bowtype_record.html",
                           # subnav_bar = ["AFB", "Barebow", "Compound", "Longbow", "Recurve"],
                           bowtype=bowtype)


    
@app.route('/gallery', methods = ["GET","POST"]) 
def gallery():
    return render_template("gallery.html",
                           directory=directory,
                           scandir=scandir)