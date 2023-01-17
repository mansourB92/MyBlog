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
    posts= Post.query.all()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        posts=posts
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    RForm = RegForm()
    ch_user = User.query.filter_by(user_name=RForm.username.data).first()
    ch_email = User.query.filter_by(email=RForm.email.data).first()
    if RForm.validate_on_submit() and not(ch_user) and not(ch_email):
        pw_hash = bcrypt.generate_password_hash(RForm.password.data).decode('utf-8')
        user = User(user_name=RForm.username.data, pass_word=pw_hash, email=RForm.email.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Welcome {RForm.username.data}, Your registered successfully", "success")
        login_user(user)
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

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    posts= Post.query.filter_by(user_id=current_user.id)
    form = UpdateProfile()
    ch_user = ""
    ch_email = ""
    if current_user.user_name != form.username.data:
        ch_user = User.query.filter_by(user_name=form.username.data).first()
    if current_user.email != form.email.data:
        ch_email = User.query.filter_by(email=form.email.data).first()
    if form.validate_on_submit() and not(ch_user) and not(ch_email):
        current_user.user_name = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account update successfully", "success")
        return redirect(url_for('profile'))
    elif request.method == "POST":
        flash("This Username or Email already exists", "warning")
    elif request.method == "GET":
        form.username.data = current_user.user_name
        form.email.data = current_user.email
    return render_template(
        'profile.html',
        title='Profile',
        form = form,
        posts=posts
        )

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post created successfully", "success")
        return redirect(url_for('home'))
    return render_template(
        'create_post.html',
        title='Create new post',
        form = form
        )

@app.route('/post/<post_id>/delete')
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash(f"{post.title} is deleted", "info")
    return redirect(url_for('profile'))