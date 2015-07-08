#coding=utf-8
from flask import render_template, flash, redirect,url_for,session,request,g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app,db,login_manager
from models import User,Article,Comment,Check
from forms import LoginForm,RegisterForm,ArticleForm,CommentForm,CheckForm
from hashlib import md5
import datetime,time
import newsspider,mail,checkcode

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
def index():
    art={}
    art['art1']=Article.query.filter_by(type_a=1).all()
    art['art2']=Article.query.filter_by(type_a=2).all()
    art['art3']=Article.query.filter_by(type_a=3).all()
    art['art4']=Article.query.filter_by(type_a=4).all()
    art['art5']=Article.query.filter_by(type_a=5).all()
    art['art6']=Article.query.filter_by(type_a=6).all()
    article={
        'article1':[],
        'article2':[],
        'article3':[],
        'article4':[],
        'article5':[],
        'article6':[],
    }
    newlist=[]
    news=newsspider.new()
    try:
        newlist=news.run()
    except Exception,e:
        try:
            newlist=news.run()
        except Exception,x:
            pass
    newlist=newlist[0:10]
    for a in art['art1']:
        username=User.query.filter_by(id=a.user_id).first().username
        article['article1'].append({'art':a,'url':'/article/'+str(a.id),'user':username})
    article['article1']=article['article1'][-5:]
    article['article1']=article['article1'][::-1]
    for a in art['art2']:
        username=User.query.filter_by(id=a.user_id).first().username
        article['article2'].append({'art':a,'url':'/article/'+str(a.id),'user':username})
    article['article2']=article['article2'][-5:]
    article['article2']=article['article2'][::-1]
    for a in art['art3']:
        username=User.query.filter_by(id=a.user_id).first().username
        article['article3'].append({'art':a,'url':'/article/'+str(a.id),'user':username})
    article['article3']=article['article3'][-5:]
    article['article3']=article['article3'][::-1]
    for a in art['art4']:
        username=User.query.filter_by(id=a.user_id).first().username
        article['article4'].append({'art':a,'url':'/article/'+str(a.id),'user':username})
    article['article4']=article['article4'][-5:]
    article['article4']=article['article4'][::-1]
    for a in art['art5']:
        username=User.query.filter_by(id=a.user_id).first().username
        article['article5'].append({'art':a,'url':'/article/'+str(a.id),'user':username})
    article['article5']=article['article5'][-5:]
    article['article5']=article['article5'][::-1]
    for a in art['art6']:
        username=User.query.filter_by(id=a.user_id).first().username
        article['article6'].append({'art':a,'url':'/article/'+str(a.id),'user':username})
    article['article6']=article['article6'][-5:]
    article['article6']=article['article6'][::-1]
    return render_template('index.html',
        title = 'Home',article=article,news=newlist)

@app.route('/admin')
@login_required
def admin():
    if g.user.role==1:
        art={}
        art['art1']=Article.query.filter_by(type_a=1).all()
        art['art2']=Article.query.filter_by(type_a=2).all()
        art['art3']=Article.query.filter_by(type_a=3).all()
        art['art4']=Article.query.filter_by(type_a=4).all()
        art['art5']=Article.query.filter_by(type_a=5).all()
        art['art6']=Article.query.filter_by(type_a=6).all()
        article={
            'article1':[],
            'article2':[],
            'article3':[],
            'article4':[],
            'article5':[],
            'article6':[],
        }
        for a in art['art1']:
            username=User.query.filter_by(id=a.user_id).first().username
            article['article1'].append({'art':a,'url':'/article/'+str(a.id),'delurl':'/deletearticle/'+str(a.id),'user':username})
        article['article1']=article['article1'][::-1]
        for a in art['art2']:
            username=User.query.filter_by(id=a.user_id).first().username
            article['article2'].append({'art':a,'url':'/article/'+str(a.id),'delurl':'/deletearticle/'+str(a.id),'user':username})
        article['article2']=article['article2'][::-1]
        for a in art['art3']:
            username=User.query.filter_by(id=a.user_id).first().username
            article['article3'].append({'art':a,'url':'/article/'+str(a.id),'delurl':'/deletearticle/'+str(a.id),'user':username})
        article['article3']=article['article3'][::-1]
        for a in art['art4']:
            username=User.query.filter_by(id=a.user_id).first().username
            article['article4'].append({'art':a,'url':'/article/'+str(a.id),'delurl':'/deletearticle/'+str(a.id),'user':username})
        article['article4']=article['article4'][::-1]
        for a in art['art5']:
            username=User.query.filter_by(id=a.user_id).first().username
            article['article5'].append({'art':a,'url':'/article/'+str(a.id),'delurl':'/deletearticle/'+str(a.id),'user':username})
        article['article5']=article['article5'][::-1]
        for a in art['art6']:
            username=User.query.filter_by(id=a.user_id).first().username
            article['article6'].append({'art':a,'url':'/article/'+str(a.id),'delurl':'/deletearticle/'+str(a.id),'user':username})
        article['article6']=article['article6'][::-1]
        return render_template('admin.html',title = 'admin',article=article)
    return redirect('/index')

@app.route('/allarticles/<int:t>')
def allarticles(t):
    #art=Article.query.all()
    art=Article.query.filter_by(type_a=t).all()
    article=[]
    for a in art:
        username=User.query.filter_by(id=a.user_id).first().username
        article.append({'art':a,'url':'/article/'+str(a.id),'user':username})
    article=article[::-1]
    return render_template('allarticles.html',
        title = 'allarticles',article=article,type_a=t)

@app.route('/news')
def news():
    newlist=[]
    news=newsspider.new()
    try:
        newlist=news.run()
    except Exception,e:
        try:
            newlist=news.run()
        except Exception,x:
            pass
    return render_template('news.html',
        title = 'news',news=newlist)

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
                if user.role==1:
                    login_user(user, remember = remember_me)
                    return redirect('/admin')
    		login_user(user, remember = remember_me)
		flash(u"登录成功！")
		return redirect(request.args.get('next') or url_for('index'))
	    else:
		flash(u'用户名或密码错误')
		return render_template('login.html', title = 'Sign In',form = form)
        return render_template('login.html', title = 'Sign In',form = form)
    return render_template('login.html', title = 'Sign In',form = form)

@app.route('/check', methods = ['GET', 'POST'])
def check():
    form = CheckForm()
    state=0
    if request.method == 'POST':
        if form.validate_on_submit():
    	    email=form.data['email']
    	    e=User.query.filter_by(email=email).first()
	    if e:
                flash(u'该邮箱已被注册')
                return render_template('check.html', title = 'check',form = form)
    	    check=checkcode.check_code()
    	    #mail.signupmail(email,check)
	    c = Check(email=email, check=check,timestamp=datetime.datetime.fromtimestamp(time.time()+10*60))
            try:
                db.session.add(c)
                db.session.commit()
                state=1
                mail.signupmail(email,check)
                flash(u'验证码已发送至'+email+u'，请注意查收邮件！')
                return render_template('check.html', title = 'check',form = form,state=state)
            except Exception, e:
                state=2
                flash(u'未知错误！')
                return render_template('check.html', title = 'check',form = form,state=state)
    return render_template('check.html', title = 'check',form = form,state=state)

@app.route('/signout')
@login_required
def signout():
    logout_user()
    flash(u'已退出')
    return redirect('/index')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    cresult=0
    if request.method == 'POST':
    	if form.validate_on_submit():
            psdmd5 = md5(form.data['password'])
   	    password = psdmd5.hexdigest()
   	    email=form.data['email']
   	    check=form.data['check']
   	    username=form.data['username']
   	    now=datetime.datetime.fromtimestamp(time.time())
   	    checks=Check.query.filter_by(email=email).all()
   	    for c in checks:
                if c.check==check and c.timestamp>now:
                    cresult=1
                    break
            if cresult==0:
                flash(u'验证码错误')
                return redirect(url_for('signup'))
    	    u=User(username=username,email=email,password=password)
            try:
                db.session.add(u)
                db.session.commit()
                flash(u'注册成功')
                mail.finishmail(email,username)
                ccheck=Check.query.filter_by(email=email).all()
                for ch in ccheck:
                    db.session.delete(ch)
                db.session.commit()
                return redirect(url_for('login'))
            except Exception, e:
                flash(u'注册失败')
                return render_template('signup.html',title = 'sign up', form=form)
    else:
        return render_template('signup.html',title = 'sign up', form=form)

@app.route('/newarticle/<int:c>', methods = ['GET', 'POST'])
@login_required
def newarticle(c):
    form = ArticleForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title=form.data['title']
    	    body = form.data['body']
    	    body=body.replace('\n','<br>&nbsp;&nbsp;&nbsp;&nbsp;')
    	    type_a=c
	    a=Article(title=title,body=body,type_a=type_a,timestamp=datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S"),author=g.user)
	    try:
	        db.session.add(a)
	        db.session.commit()
	        flash(u'发帖完成')
	        return redirect(url_for('myarticle'))
	    except Exception, e:
	        flash(u'发帖失败')
            return render_template('newarticle.html', title = 'newarticle',form = form)
    return render_template('newarticle.html', title = 'newarticle',form = form)

@app.route('/myarticle',methods = ['GET', 'POST'])
@login_required
def myarticle():
    art=Article.query.filter_by(user_id=g.user.id).all()
    article=[]
    for a in art:
        article.append({'art':a,'url':'/article/'+str(a.id)})
    article=article[::-1]
    return render_template('myarticle.html', title = 'myarticle',article=article)

@app.route('/deletearticle/<int:d>')
@login_required
def deletearticle(d):
    if Article.query.filter_by(id=d).first().user_id!=g.user.id and g.user.role!=1:
        return redirect('/')
    try:
        com=Comment.query.filter_by(article_id=d).all()
        for c in com:
            db.session.delete(c)
            db.session.commit()
        art=Article.query.filter_by(id=d).first()
        db.session.delete(art)
        db.session.commit()
        flash(u'已删除')
    except Exception,e:
        flash(u'操作失败')
    if g.user.role==1:
        return redirect('/admin')
    return redirect('/myarticle')

@app.route('/article/<int:a>',methods = ['GET', 'POST'])
@login_required
def article(a):
    form = CommentForm()
    article=Article.query.filter_by(id=a).first()
    identification={}
    identification['id']=0
    if article.user_id==g.user.id:
        identification['id']=1
        identification['delurl']='/deletearticle/'+str(a)
        identification['updturl']='/updatearticle/'+str(a)
    if request.method == 'POST':
        if form.validate_on_submit():
    	    body = form.data['body']
    	    username=User.query.filter_by(id=g.user.id).first().username
	    c=Comment(username=username,body=body,timestamp=datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S"),article_id=a)
	    try:
	        db.session.add(c)
	        db.session.commit()
	        flash(u'评论成功')
	    except Exception, e:
	        flash(u'操作失败')
	    comment=Comment.query.filter_by(article_id=a).all()
	    return render_template('article.html', title = 'article',form=form,article=article,comment=comment,identification=identification)
    comment=Comment.query.filter_by(article_id=a).all()
    return render_template('article.html', title = 'article',form=form,article=article,comment=comment,identification=identification)
