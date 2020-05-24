from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class OrderForm(FlaskForm):
    """Contact form."""
    Cheese Maggie = StringField('cheeseMaggie', [
        DataRequired()])
    Plain Maggie = StringField('plainMaggie', [
        DataRequired()])
    Masala Dosa = TextField('masalaDosa', [
        DataRequired()])

    submit = SubmitField('Submit')
