from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from Blog.database import *

class RegForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=4, max=25, message="username must be between 4 and 25 characters")])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    image = FileField("avatar(optional)", validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Images only!')])

class LogForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField("remember me")

class UpdateProfile(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=4, max=25, message="username must be between 4 and 25 characters")])
    email = StringField("email", validators=[DataRequired(), Email()])
    image = FileField("new avatar", validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Images only!')])

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    image = FileField("image(optional)", validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Images only!')])