"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, url_for, flash
from Blog import app, db, bcrypt
from Blog.database import *
from Blog.form_blog import *

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
    if RForm.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(RForm.password.data).decode('utf-8')
        user = User(user_name=RForm.username.data, pass_word=pw_hash, email=RForm.email.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Welcome {RForm.username.data}, Your registered successfully", "success")
        return redirect(url_for('home'))
    return render_template(
        'Reg.html',
        title='Register',
        form=RForm
    )
