"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db = SQLAlchemy()
SECRET_KEY = "asd"
#SQLALCHEMY_ECHO = True
bcrypt = Bcrypt(app)
app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Blog_DB.db"
db.init_app(app)

import Blog.views
