from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class OrderForm(FlaskForm):
    """Contact form."""
    cheeseMaggie = StringField('Cheese Maggie', [
        DataRequired()])
    plainMaggie = StringField('Plain Maggie', [
        DataRequired()])
    masalaDosa = TextField('Masala Dosa', [
        DataRequired()])

    submit = SubmitField('Submit')
