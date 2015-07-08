# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import TextAreaField,StringField,PasswordField,BooleanField
from wtforms.validators import DataRequired,ValidationError
from models import User,Article, Comment,Check
from hashlib import md5

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class CheckForm(Form):
    email = EmailField('email', validators=[DataRequired()])

    def validate_email(self, field):
        email = field.data.strip()
        email = User.query.filter_by(email=email).first()
        if email:
	    raise ValidationError(u'邮箱已存在')

class RegisterForm(Form):
    username = StringField('username', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    conform = PasswordField('conform', validators=[DataRequired()])
    check = StringField('check', validators=[DataRequired()]) 

    def validate_email(self, field):
        email = field.data.strip()
        email = User.query.filter_by(email=email).first()
        if email:
	    raise ValidationError(u'邮箱已存在')

    def validate_username(self, field):
        username = field.data.strip()
        if len(username) < 5 or len(username) > 20:
            raise ValidationError(u'用户名为5-20个字符')
        else:
        #验证是否注册
            u = User.query.filter_by(username=username).first()
            if u:
	        raise ValidationError(u'用户名已注册')

    def validate_password(self, field):
        password = field.data.strip()
        if len(password) < 6:
	    raise ValidationError(u'密码不能少于六个字符')

    def validate_conform(self, field):
        conform = field.data.strip()
        if self.data['password'] != conform:
	    raise ValidationError(u'两次输入密码不一致')

class ArticleForm(Form):
    title = StringField('title', validators=[DataRequired()])
    body = TextAreaField('body', validators=[DataRequired()])

    def validate_title(self, field):
        title = field.data.strip()
        if len(title) < 1:
	    raise ValidationError(u'不能为空')

    def validate_body(self, field):
        body = field.data.strip()
        if len(body) < 1:
	    raise ValidationError(u'不能发空贴')

class CommentForm(Form):
    body = TextAreaField('body', validators=[DataRequired()])

    def validate_body(self, field):
        body = field.data.strip()
        if len(body) < 1:
	    raise ValidationError(u'不能为空')
    
