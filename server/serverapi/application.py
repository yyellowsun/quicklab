#创建Flask app实体和注册数据库对象
from flask import Flask
from flask_cors import CORS

def create_app(app_name='SERVER_API'):
    app = Flask(app_name)
    app.config.from_object('serverapi.config.BaseConfig')

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    from serverapi.api import api
    app.register_blueprint(api, url_prefix="/api")
    
    from serverapi.models import db
    db.init_app(app)
    
    return app