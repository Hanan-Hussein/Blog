from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField,RadioField
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from app.models import User
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class Register(FlaskForm):
    """_summary_

    Args:
        Form (_type_): _description_
    """
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password')])

    submit = SubmitField('Signup')

    def validate_username(self, username):
        """
        """
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError(
                "That username is already taken! Please choose another")

    def validate_email(self, email):
        """

        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "That email is already taken! Please choose another")


class Login(FlaskForm):
    """

    Args:
        Form (_type_): _description_
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class Subscribe(FlaskForm):
    """

    Args:
        Form (_type_): _description_
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Subscribe')