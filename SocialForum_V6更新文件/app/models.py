from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    posts = db.relationship('Article', backref = 'author', lazy = 'dynamic')
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

class Check(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), index = True,unique = True)
    check = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<Check %r>' % (self.email)
        
class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title=db.Column(db.String(140))
    body = db.Column(db.String)
    type_a = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Article %r>' % (self.body)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username=db.Column(db.String(64))
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

    def __repr__(self):
        return '<Comment %r>' % (self.body)
