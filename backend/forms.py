from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FloatField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import date

#Definition des GUI-Eingabeformulars für neue / zu ändernde Pflanzen
class PflanzeForm(FlaskForm):
    name = TextAreaField('Name', 
                         validators = [DataRequired(),         
                         Length(min=1, max=40)])
    wissenschaft_name = TextAreaField('Wissenschaftl. Name', 
                         validators = [DataRequired(),         
                         Length(min=1, max=40)])
    familie = TextAreaField('Familie', 
                         validators = [DataRequired(),         
                         Length(min=1, max=40)])
    vegetationszone = TextAreaField('Vegetationszone', 
                         validators = [DataRequired(),         
                         Length(min=1, max=40)])
    will_sonne = TextAreaField('Heller Standort?', 
                         validators = [DataRequired(),         
                         Length(min=1, max=40)])
    gefahr = TextAreaField('Gefahr', 
                         validators = [DataRequired(),         
                         Length(min=1, max=40)])
    submit = SubmitField('Submit')

