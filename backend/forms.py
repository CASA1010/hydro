from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from models import User
from sqlalchemy import and_, not_
from config import db
from flask_login import current_user


#Formulare für Benutzer
#-Registrierung
class RegistrationForm(FlaskForm):
    username = StringField('Benutzername',
                            validators=[DataRequired(message="Bitte vergeben Sie Ihren gewünschten Benutzernamen.")])
    email = StringField('EMail-Adresse',
                        validators=[DataRequired(message="Bitte geben Sie eine EMail-Adresse an, unter der wir Sie erreichen können."),
                                    Email(message="Bitte geben Sie eine gültige EMail-Adresse ein.")])
    password = PasswordField('Passwort',
                            validators=[DataRequired(message="Bitte geben Sie Ihr Passwort ein.")])
    password2 = PasswordField('Passwort-Wiederholung',
                            validators=[DataRequired(message="Bitte geben Sie das gewünschte Passwort erneut ein."),
                            EqualTo(fieldname='password', message="Passwort und Passwort-Wiederholung sind nicht gleich.")])

    register = SubmitField('Registrieren')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Dieser Benutzername ist bereits vergeben.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Diese EMail-Adresse ist bereits vergeben.")

#-Passwort ändern
class PasswordChangeForm(FlaskForm):
    password = PasswordField('Aktuelles Passwort',
                            validators=[DataRequired(message="Bitte geben Sie Ihr aktuelles Passwort ein.")])
    password_new = PasswordField('Neues Passwort',
                            validators=[DataRequired(message="Bitte geben Sie Ihr neues Passwort ein.")])
    password_new2 = PasswordField('Passwort-Wiederholung',
                            validators=[DataRequired(message="Bitte geben Sie das gewünschte Passwort erneut ein."),
                            EqualTo(fieldname='password_new', message="Passwort und Passwort-Wiederholung sind nicht gleich.")])

    passwort_aendern = SubmitField('Neues Passwort vergeben')

    def validate_password(self, password):
        if not current_user.check_password(password.data):
            raise ValidationError("aktuelles Passwort inkorrekt.")

#-Login
class LoginForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired(message="Bitte geben Sie Ihren Benutzernamen ein.")])
    password = PasswordField('Passwort', validators=[DataRequired(message="Bitte geben Sie Ihr Passwort ein.")])
    remember_me = BooleanField('Angemeldet bleiben')

    login = SubmitField('Anmelden')

#-Sonstige (für Admin-Bereich, User-Details)
class UserForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired(message="Bitte geben Sie Ihren Benutzernamen ein.")])
    email = StringField('EMail-Adresse', validators=[DataRequired(message="Bitte geben Sie Ihre EMail-Adresse ein."),
                                                     Email(message="Bitte geben Sie eine gültige EMail-Adresse ein.")])

    aendern = SubmitField('Benutzername/ EMail ändern')
    abbrechen = SubmitField('Abbrechen')

    def validate_username(self, username):
        user = db.session.query(User).filter(and_(User.username == username.data, User.id != current_user.id)).first()
        if user is not None:
            raise ValidationError("Dieser Benutzername ist bereits vergeben.")

    def validate_email(self, email):
        #user = User.query.filter_by(email=email.data).first()
        user = db.session.query(User).filter(and_(User.email == email.data, User.id != current_user.id)).first()
        if user is not None:
            raise ValidationError("Diese EMail-Adresse ist bereits vergeben.")

#Formular für Pflanzen
class PflanzeForm(FlaskForm):
    name = StringField('Name', 
                        validators = [DataRequired(message="Der Name der Pflanze muss angegeben werden."),         
                                    Length(min=0, max=40, message="Der Name darf maximal 40 Zeichen lang sein")])
    wissenschaft_name = StringField('Wissenschaftl. Name',      
                        validators = [Length(min=0, max=40, message="Der Wissenschaftl. Name darf maximal 40 Zeichen lang sein")])
    familie = StringField('Familie',       
                        validators = [Length(min=0, max=40, message="Die Familie darf maximal 40 Zeichen lang sein")])
    bild = FileField('Bild')
                    #validators= [DataRequired(message="Es muss ein Bild der Pflanze hochgeladen sein.")])
    vegetationszone = StringField('Vegetationszone',        
                                validators = [Length(min=0, max=40, message="Die Vegetationszone darf maximal 40 Zeichen lang sein")])
    will_sonne = StringField('Heller Standort?',      
                            validators = [Length(min=0, max=40, message="Der Standort darf maximal 40 Zeichen lang sein")])
    gefahr = StringField('Gefahr',       
                        validators = [Length(min=0, max=40, message="Die Gefahrenangaben dürfen maximal 40 Zeichen lang sein")])
    
    anlegen = SubmitField('Anlegen')
    aendern = SubmitField('Ändern')
    loeschen = SubmitField('Löschen')
    abbrechen = SubmitField('Abbrechen')
    bild_hochladen = SubmitField('Bild hochladen')
    anwenden = SubmitField('Anwenden')