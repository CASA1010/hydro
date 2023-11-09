from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FloatField, DateField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import date

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
    
    


