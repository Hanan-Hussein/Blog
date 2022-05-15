from flask import Flask
from app.config import config_options
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

db = SQLAlchemy()
bootstrap = Bootstrap5()
login_manager = LoginManager()
login_manager.login_view = ''

login_manager.login_message_category = 'info'

login_manager = LoginManager()
def create_app(config_name):
  app=Flask(__name__)

  app.config.from_object(config_options[config_name])
  login_manager.init_app(app)
  db.init_app(app)
  bootstrap.init_app(app)
  
  #import blueprints
  from app.main.routes import main

  #register blueprint
  app.register_blueprint(main)

  return app

