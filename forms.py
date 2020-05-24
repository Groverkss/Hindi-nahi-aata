from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField
# from flask.ext.wtf import validators, ValidationError
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class OrderForm(FlaskForm):
    """Contact form."""
    cheeseMaggie = IntegerField('Cheese Maggie', [ Optional(), NumberRange(min=1,max=None,message="please enter only positive values!")])
    plainMaggie = IntegerField('Plain Maggie', [ Optional(), NumberRange(min=1,max=None,message="please enter only positive values!")] )
    masalaDosa = IntegerField('Masala Dosa', [ Optional(), NumberRange(min=1,max=None,message="please enter only positive values!")] )

    submit = SubmitField('Submit')
