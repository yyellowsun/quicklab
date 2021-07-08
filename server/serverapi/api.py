#restfull 请求和响应对应的api
from flask import Blueprint, jsonify, request
from flask.wrappers import Response
from .models import db,User,Work
from sqlalchemy import desc

api = Blueprint('api', __name__)

@api.route('/hello/<string:name>/')
def say_hello(name):
    response = { 'msg': "hello {}".format(name)}
    return jsonify(response)

#对用户的查询和增加
@api.route('/users/', methods=('GET','POST') )
def users():
    if request.method == 'GET':
        users=User.query.all()
        return jsonify({'users': [user.to_dict() for user in users]})
    elif request.method == 'POST':
        pass
        ###可能会存在问题，没有测试过
        #data=request.get_json()
        #last=User.query.order_by(desc(User.id)).first()
        #user=User(username=data['username'],password=data['password'],identity=data['identity'],work=[],id=last.to_dict()['id']+1)
        #db.session.add(user)
        #db.session.commit()
        #return jsonify(user.to_dict(),201)

@api.route('/users/<int:id>', methods=('GET','PUT'))
def user(id):
    if request.method == 'GET':
        user=User.query.get(id)
        return jsonify({'user': [user.to_dict()]})
    elif request.method == 'PUT':
        #没有写对用户的作品的增加
        pass

@api.route('/users/test')
def test():
    user=User.query.order_by(desc(User.id)).first()
    return jsonify({'user': [user.to_dict()]})

#对作品的查询和增加
@api.route('/works/')
def works():
    works=Work.query.all()
    return jsonify({'works':[work.to_dict() for work in works]})
#对作品的更改
@api.route('/works/<int:id>')
def work(id):
    work=Work.query.get(id)
    return jsonify({'work': [work.to_dict()]}) 
#对作品的更改