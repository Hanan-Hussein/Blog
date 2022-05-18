class Config:
  """
  This are the configurations for the application
  """
  # SQLALCHEMY_TRACK_MODIFICATIONS=True
  SQLALCHEMY_DATABASE_URI='sqlite:///site.db'

  SECRET_KEY ='bc84445981640e5a26fadc7a406f9ff0'
  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 465
  MAIL_USERNAME = 'apollolibrary99@gmail.com'
  MAIL_PASSWORD =  'Library@99'

  MAIL_USE_TLS = False
  MAIL_USE_SSL = True
class ProdConfig(Config):
  """
  This are the configurations for the production environment
  Args:
  Config : The main configuration
  """


class DevConfig(Config):
    """
    This are the configurations for the development environment
    Args:
        Config : The main configuration
    """
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
