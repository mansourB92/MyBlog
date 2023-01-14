"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, url_for, flash, request
from Blog import app, db, bcrypt, login_manager
from Blog.database import *
from Blog.form_blog import *
from flask_login import login_user, current_user, logout_user, login_required

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/Reg', methods=['GET', 'POST'])
def Reg():
    """Renders the about page."""
    RForm = RegForm()
    ch_user = User.query.filter_by(user_name=RForm.username.data).first()
    ch_email = User.query.filter_by(email=RForm.email.data).first()
    if RForm.validate_on_submit() and not(ch_user) and not(ch_email):
        pw_hash = bcrypt.generate_password_hash(RForm.password.data).decode('utf-8')
        user = User(user_name=RForm.username.data, pass_word=pw_hash, email=RForm.email.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Welcome {RForm.username.data}, Your registered successfully", "success")
        return redirect(url_for('home'))
    elif request.method == "POST":
        flash("This Username or Email already exists", "warning")
    return render_template(
        'Reg.html',
        title='Register',
        form=RForm
    )
@app.route('/Log', methods=['GET', 'POST'])
def Log():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    Lform = LogForm()
    if Lform.validate_on_submit():
        user = User.query.filter_by(user_name=Lform.username.data).first()
        if user and bcrypt.check_password_hash(user.pass_word, Lform.password.data):
            login_user(user, remember=Lform.remember.data)
            flash(f"Welcome {Lform.username.data}, Your login successfully", "success")
            return redirect(url_for('home'))
        else:
            flash("Email or Password is wrong", "danger")
    return render_template(
        'Log.html',
        title='Login',
        form=Lform
    )

@app.route('/Logout')
@login_required
def Logout():
    logout_user()
    flash("You logout successfully", "success")
    return redirect(url_for('home'))