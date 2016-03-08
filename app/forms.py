from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(Form):
    login = StringField('login1', validators=[DataRequired(), Email()])
    password = PasswordField('password1', validators=[DataRequired()])
    remember_me = BooleanField('remember_me1', default=False)
    submit = SubmitField('Log in')