from flask import Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, url_for, flash, redirect, request
from app.users.forms import Register, Login
from app import db,bcrypt

from app.models import User

users = Blueprint('users', __name__)

@users.route('/register', methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = Register()
    if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
      user=User(username=form.username.data,email=form.email.data,password=hashed_password)
      db.session.add(user)
      db.session.commit()
      flash('Your Account Has been Created! You are now able to log in','success')
      return redirect(url_for('users.login'))

    return render_template('register.html', title='Register', form=form)


@users.route('/login', methods=['POST', 'GET'])

def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Welcome {user.username.title()} !! ', 'success')
            # args is a dict
            # get returns none if the next key does not exist
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', title='Login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
