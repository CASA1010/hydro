from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from flask_login import UserMixin
from flask_bootstrap import Bootstrap
from enum import Enum

class MsgCat(Enum):
    OK = "success"
    ERR = "danger"
    WARN = "warning"
    INFO = "info"

app = Flask(__name__, template_folder='../templates', static_folder ='../static') #Verbindung HTML - CSS Teil 1

#Initialisierung Flask-Login-extension
login = LoginManager(app)

#Konfiguration der Datenbank
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.db')
db = SQLAlchemy(app)

#Konfiguration von Flask-Bootstrap
bootstrap = Bootstrap(app)

#Konfigurstion der Datei-Ablage
app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'uploads')
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
    #foto = db.Column(db.BLOB, nullable=True)
    will_sonne = db.Column(db.String(40), nullable=True)
    gefahr = db.Column(db.String(40), nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#über diese Funktion kann sich Flask-Login mittels id den aktuellen User besorgen
@login.user_loader
def load_user(id):
    return User.query.get(int(id))