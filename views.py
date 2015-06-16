# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect,url_for,session,request,g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app,db,login_manager
from models import User,Post
from forms import LoginForm,RegisterForm
from hashlib import md5

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
        title = 'Home')

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
    	    username=form.data['username']
    	    psdmd5=md5(form.data['password'])
	    password=psdmd5.hexdigest()
	    remember_me = form.data['remember_me']
	    user=User.query.filter_by(username=username,password=password).first()
	    if user:
    		login_user(user, remember = remember_me)
		flash("signin successful")
		return redirect(request.args.get('next') or url_for('index'))
	    else:
		flash('用户名或密码错误')
		return render_template('login.html', title = 'Sign In',form = form)
        return render_template('login.html', title = 'Sign In',form = form)
    return render_template('login.html', title = 'Sign In',form = form)

@app.route('/signout')
@login_required
def signout():
    logout_user()
    flash('signout successful')
    return redirect('/index')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method == 'POST':
    	if form.validate_on_submit():
            psdmd5 = md5(form.data['password'])
   	    password = psdmd5.hexdigest()
    	    u = User(username=form.data['username'], email=form.data['email'], password=password)
    	try:
	    db.session.add(u)
	    db.session.commit()
	    flash('signup successful')
    	except Exception, e:
	    flash('signup failed')
	    return render_template('signup.html', form=form)
	return redirect(url_for('login'))
    else:
        return render_template('signup.html', form=form)
