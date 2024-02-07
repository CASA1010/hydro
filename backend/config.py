from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from enum import Enum

class MsgCat(Enum):
    OK = "success"
    ERR = "danger"
    WARN = "warning"
    INFO = "info"

app = Flask(__name__, static_folder = '../static', template_folder='../templates') # Variable app mit Info vom Flask Proyekt

#Konfiguration der Datenbank
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #app nicht bei jeder Änderung an der DB informieren
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Konfiguration von Flask-Login
login = LoginManager(app)
login.login_view = 'login'
login.login_message = "Bitte melden Sie sich an, um diese Seite aufzurufen"
login.login_message_category = MsgCat.ERR.value

#Konfiguration von Flask-Bootstrap
bootstrap = Bootstrap(app)

#Konfiguration der Datei-Ablage
app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024 #max. 8 MByte

#Konfiguration für CSRF-Protection (Security-feature; wird benötigt, sobald man per Browser Daten im Backend ändern möchte)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)
csrf.init_app(app)