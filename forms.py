
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class NewRestaurantForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    address = StringField('Address',validators=[DataRequired()])
    submit = SubmitField('Add')


class ReviewForm(FlaskForm):
    review = StringField('Review', validators=[DataRequired()])
    rating = StringField('Rating (Out of 10)', validators=[DataRequired()])
    submit = SubmitField('Submit')