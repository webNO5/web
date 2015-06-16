# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import TextField,StringField,PasswordField,BooleanField
from wtforms.validators import DataRequired,ValidationError
from models import User
from hashlib import md5

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    conform = PasswordField('conform', validators=[DataRequired()])

    def validate_username(self, field):
        username = field.data.strip()
        if len(username) < 5 or len(username) > 20:
            raise ValidationError('username must be 5-20 letters')
        else:
        #验证是否注册
            u = User.query.filter_by(username=username).first()
            if u:
	        raise ValidationError('The username already exists')

    def validate_email(self, field):
        email = field.data.strip()
        email = User.query.filter_by(email=email).first()
        if email:
	    raise ValidationError('The email already exists')


    def validate_password(self, field):
        password = field.data.strip()
        if len(password) < 6:
	    raise ValidationError('password must be 6 letter at least')

    def validate_conform(self, field):
        conform = field.data.strip()
        if self.data['password'] != conform:
	    raise ValidationError('the password and conform are different')
    
