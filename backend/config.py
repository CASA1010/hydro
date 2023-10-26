from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, template_folder='../templates') # Variable app mit Info vom Flask Proyekt

#Konfiguration der Datenbank
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.db')
db = SQLAlchemy(app)

#Konfiguration für CSRF-Protection (Security-feature; wird benötigt, sobald man per Browser Daten im Backend ändern möchte)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

#Definition der Model-Klassen
class Pflanze(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=True)
    wissenschaft_name = db.Column(db.String(40), nullable=True)
    familie = db.Column(db.String(40), nullable=True)
    vegetationszone = db.Column(db.String(40), nullable=True)
    #TODO: foto = db.Column(BLOB), nullable=True) foto = image_attachment('Foto')
    will_sonne = db.Column(db.String(40), nullable=True)
    gefahr = db.Column(db.String(40), nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)