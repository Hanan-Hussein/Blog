from flask import Flask
from app.config import config_options
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
login_manager.login_view = ''

login_manager.login_message_category = 'info'

login_manager = LoginManager()
def create_app(config_name):
  app=Flask(__name__)

  app.config.from_object(config_options[config_name])
  login_manager.init_app(app)
  return app

