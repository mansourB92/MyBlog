from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from Blog.database import *

class RegForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=4, max=25, message="username must be between 4 and 25 characters")])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])


class LogForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField("remember me")

class UpdateProfile(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=4, max=25, message="username must be between 4 and 25 characters")])
    email = StringField("email", validators=[DataRequired(), Email()])

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])