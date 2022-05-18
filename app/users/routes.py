from flask import Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, url_for, flash, redirect, request
from app.users.forms import Register, Login,Subscribe,UpdateAccountForm
from app import db,bcrypt,mail
from flask_mail import  Message
from app.models import Posts, User, Subscribers
from app.users.utils import save_picture

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

@users.route('/subscribe', methods=['POST', 'GET'])
def subscribe():
    form=Subscribe()
    if form.validate_on_submit():
        sub=Subscribers(email=form.email.data)
        
        db.session.add(sub)
        db.session.commit()
        msg=Message("WELCOME",sender="apollolibrary99@gmail.com",recipients=[sub.email])
        msg.body = "Welcome to H&J's Blog you Have Subscribed News Letter we will loop you on all newly updates"
        mail.send(msg)
     
        flash('Your  Has Joined H&J Blog Subscription  ','success')
        return redirect(url_for('main.home'))


    return render_template('subscribe.html',form=form)

@users.route('/account',methods=['POST', 'GET'])
@login_required
def account():
    """
    """
    post= Posts.query.filter_by(user_id=current_user.id)
    form=UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture=save_picture(form.picture.data)
            current_user.profile=picture
             
        current_user.username=form.username.data
        current_user.email=form.email.data

        db.session.commit()
        flash('Your Account Has been updated!','success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':

        form.username.data=current_user.username
        form.email.data=current_user.email
    
    image_file= url_for('static',filename='profiles/'+current_user.image_file)
    return render_template('account.html', title='Account',image_file=image_file,form=form,post=post )
