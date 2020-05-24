from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField
# from flask.ext.wtf import validators, ValidationError
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class OrderForm(FlaskForm):
    """Contact form."""
    cheeseMaggie = IntegerField('Cheese Maggie', [NumberRange(
        min=0, message="please enter only positive values!")])
    plainMaggie = IntegerField('Plain Maggie', [NumberRange(
        min=0, message="please enter only positive values!")])
    masalaDosa = IntegerField('Masala Dosa', [NumberRange(
        min=0, message="please enter only positive values!")])

    submit = SubmitField('Submit')
