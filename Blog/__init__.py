"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'Blog/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
db = SQLAlchemy()
SECRET_KEY = "asd"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#SQLALCHEMY_ECHO = True
bcrypt = Bcrypt(app)
app.secret_key = SECRET_KEY
DATABASE = 'sqlite:///Blog_DB.db'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'Log'
login_manager.login_message = 'Please login first'
login_manager.login_message_category = 'info'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

import Blog.views
