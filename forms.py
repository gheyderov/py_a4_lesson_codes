from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    company = StringField('company', validators=[DataRequired()])
    message = TextAreaField('message', validators=[DataRequired()])
    subscribe = BooleanField('subscribe')
