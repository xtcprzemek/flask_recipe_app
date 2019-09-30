from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    username = StringField('User name', validators=[DataRequired(), Length(min=3, max=40)])
    password = StringField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm_password = StringField('Confirm password', validators=[DataRequired(), EqualTo('password')])

