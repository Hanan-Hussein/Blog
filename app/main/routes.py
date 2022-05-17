from app.models import User, Posts
from flask import render_template, Blueprint
from flask import render_template, url_for, flash, redirect, request

main = Blueprint('main', __name__)


@main.route('/')
def home():
    # All Posts here
    posts = Posts.query.all()
    for post in posts:
        image_file= url_for('static',filename='profiles/'+post.blog_image)

    return render_template('index.html',posts=posts,image_file=image_file)
