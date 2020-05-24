from flask_wtf import FlaskForm,
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class OrderForm(FlaskForm):
    """Contact form."""
    cheeseMaggie = StringField('cheeseMaggie', [
        DataRequired()])
    plainMaggie = StringField('plainMaggie', [
        DataRequired()])
    masalaDosa = TextField('masalaDosa', [
        DataRequired()])

    submit = SubmitField('Submit')
