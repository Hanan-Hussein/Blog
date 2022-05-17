from app.models import User, Posts
from flask import render_template, Blueprint
from flask import render_template, url_for, flash, redirect, request
from sqlalchemy import asc, desc
from ..request import get_random_quote

main = Blueprint('main', __name__)


@main.route('/')
def home():
    # All Posts here
    posts = Posts.query.order_by(desc(Posts.date_created)).limit(3).all()
    headline=Posts.query.filter_by(id=1).first()
    quote =get_random_quote()

    for post in posts:
        image_file= url_for('static',filename='posts/'+post.blog_image)

        post.blog_image= image_file
    headline_image= headline.blog_image

    return render_template('index.html',posts=posts,headline_image=headline_image,headline=headline,quote=quote)
