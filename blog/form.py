from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, validators, TextAreaField
from author.form import RegisterForm
from blog.models import Category
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class SetupForm(RegisterForm):
    name = StringField('Blog name', [
        validators.Required(),
        validators.Length(min=4, max=80)
        ])
        
def categories():
    return Category.query
        
class PostForm(Form):
    image = FileField('Image', validators=[
        FileAllowed(['jpg', 'png'], "Images only!")
        ])
    title = StringField('Title', [
        validators.Required(),
        validators.Length(min=1, max=80)
        ])
    body = TextAreaField('Content', validators=[validators.Required()])
    category = QuerySelectField('Category', query_factory=categories, allow_blank=True)
    new_category = StringField('New Category')
    
class CommentForm(Form):
    text = TextAreaField('Comment', validators=[validators.Required()])
    