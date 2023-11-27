from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FloatField, DateField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from datetime import date
from config import User


#Formular für die Registrierung neuer User
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

#Formular für die Login-Seite
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

#Definition des GUI-Eingabeformulars für neue / zu ändernde Pflanzen todo esto estaba bien
class PflanzeForm(FlaskForm):
#Attribute der Klasse
#-Eingabefelder
    name = TextAreaField('Name', 
                         validators = [DataRequired(),         
                         Length(min=1, max=40)])
    wissenschaft_name = TextAreaField('Wissenschaftl. Name', 
                         validators = [DataRequired(),         
                         Length(min=1, max=40)])
    familie = TextAreaField('Familie', 
                         validators = [DataRequired(),         
                         Length(min=1, max=40)])
    bild = FileField('Bild',
                     validators=[DataRequired()])
    vegetationszone = TextAreaField('Vegetationszone', 
                         validators = [DataRequired(),         
                         Length(min=1, max=40)])
    will_sonne = TextAreaField('Heller Standort?', 
                         validators = [DataRequired(),         
                         Length(min=1, max=40)])
    gefahr = TextAreaField('Gefahr', 
                         validators = [DataRequired(),         
                         Length(min=1, max=40)])

#-Buttons
    anlegen = SubmitField('Anlegen')
    aendern = SubmitField('Ändern')
    loeschen = SubmitField('Löschen')
    abbrechen = SubmitField('Abbrechen')
    bild_hochladen = SubmitField('Bild hochladen')
    
    


