from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField,RadioField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
    """
    Args:
        FlaskForm (_type_): _description_
    """
    title=StringField('Title', validators=[DataRequired()])
    description=TextAreaField('Description', validators=[DataRequired(),Length(min=2, max=300)])
    content=TextAreaField('Content', validators=[DataRequired(),Length(min=2)])
    blog_image= FileField('Post Image', validators=[FileAllowed(['jpg','png','svg','jpeg','gif'])])
    category=RadioField('Category', choices = [('Food','Food'),('Technology','Technology'),('Fashion','Fashion'),('Travel','Travel')])

    submit = SubmitField('Create Post')
    

    
class CommentsForm(FlaskForm):
    content=TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Add')
