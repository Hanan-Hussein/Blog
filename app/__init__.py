from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from flask_bootstrap import Bootstrap5
from app.config import config_options

db = SQLAlchemy()
bcrypt = Bcrypt()
mail=Mail()
bootstrap = Bootstrap5()
login_manager = LoginManager()
login_manager.login_view = ''

login_manager.login_message_category = 'info'

login_manager = LoginManager()

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config_options[config_name])
    db.init_app(app)
    
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    from app.users.routes import users
    from app.main.routes import main
    from app.posts.routes import posts


    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)


    return app

