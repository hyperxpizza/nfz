from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CovidForm(FlaskForm):
    name = StringField('Imię',validators=[DataRequired()])
    surname = StringField('Nazwisko', validators=[DataRequired()])
    pesel = StringField('Pesel', validators=[DataRequired()])
    email = StringField('E-mail',validators=[DataRequired()])
    temperature = StringField('Temperatura ciała',validators=[DataRequired()])
    objawy = StringField('Objawy',validators=[DataRequired()])
    submit = SubmitField('Wyślij!')
