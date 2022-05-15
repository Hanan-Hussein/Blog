from datetime import datetime
from flask_login import UserMixin

from . import db,login_manager

@login_manager.user_loader
def login_manager(user_id):
  return User.query.get(int(user_id))

class User(db.Model,UserMixin):
  """
  """
  id=db.Column(db.Integer,primary_key=True)
  username=db.Column(db.String,nullable=False,unique=True)
  email=db.Column(db.String,nullable=False,unique=True)
  password=db.Column(db.String,nullable=False)
  profile=db.Column(db.String,nullable=False)
  post = db.relationship('Posts', backref='author', lazy=True)

  def __repr__(self):
      return f"id: {self.id} , username: {self.username} , email: {self.email} "

class Posts(db.Model):
  """
  """
  id=db.Column(db.Integer,primary_key=True)
  title=db.Column(db.String,nullable=False)
  content=db.Column(db.String,nullable=False)
  blog_image=db.Column(db.String,nullable=False)
  comments= db.Column(db.String, default='')
  date_created = db.Column(db.Date, nullable=False, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  
  def __repr__(self):
      return f"id: {self.id} , title: {self.title}"