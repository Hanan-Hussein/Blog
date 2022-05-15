from app.models import User, Posts
from flask import render_template, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def home():
    # All Posts here
    # posts = Posts.query.all()

    return render_template('index.html')
