from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
#proposer 和Inspector
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    identity = db.Column(db.String(64))
    works = db.relationship('Work', backref="survey", lazy=False)

    def to_dict(self):
        return dict(id=self.id,
                    username=self.username,
                    password=self.password,
                    identity=self.identity,
                    works=[work.to_dict() for work in self.works])

    def __init__(self,id,un,pw,ity):
        self.id = id
        self.username = un
        self.password = pw
        self.identity = ity

#作品表
class Work(db.Model):
    __tablename__ = 'works'
#基本信息
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=True)
    theme = db.Column(db.String(64), nullable=True)
    commit_time = db.Column(db.DateTime, nullable=True,default=datetime.now)
    commit_user = db.Column(db.String(64), db.ForeignKey('users.username'))
    status = db.Column(db.String(64), nullable=True)
#详细信息
    photo_url = db.Column(db.String(64),  nullable=True)
    photo_time = db.Column(db.DateTime, nullable=True,default=datetime.now)
    describeinfo = db.Column(db.String(64),  nullable=True)
    copyrightnum = db.Column(db.Integer, unique=True, nullable=True)
    opinion = db.Column(db.String(64), nullable=True)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            theme=self.theme,
            commit_time=self.commit_time.strftime('%Y-%m-%d %H:%M:%S'),
            commit_user=self.commit_user,
            status=self.status,
            photo_url=self.photo_url,
            photo_time=self.photo_time.strftime('%Y-%m-%d %H:%M:%S'),
            describeinfo=self.describeinfo,
            copyrightnum=self.copyrightnum,
            opinion=self.opinion
        
        )
