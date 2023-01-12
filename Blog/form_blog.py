from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from Blog.database import *

class RegForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=4, max=25, message="username must be between 4 and 25 characters")])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])

    def validate_username(self, username):
        user = User.query.filter_by(user_name=username.data).first()
        if user:
            raise ValidationError('This username already exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email already exists')

class LogForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField("remember me")