from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import TextAreaField
from wtforms.validators import InputRequired

## FORMS
    
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class ArticleForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    content = TextAreaField("content")

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old_Password", validators=[InputRequired()])
    new_password = PasswordField("New_Password", validators=[InputRequired()])