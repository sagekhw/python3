from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import *
from flask_jwt_extended import JWTManager
from flask_mail import Mail, Message

from .controller.SimbaController import *
from .controller.AuthController import *
from .controller.UserController import *
from app.config.AppConfig import *
# from datetime import timedelta
import datetime

app = Flask(__name__)

CORS(app, resources={r'*': {'origins': '*'}})

#### JWT ####
# JWT 매니저 활성화

app.config["JWT_SECRET_KEY"] = FlaskConfig.JWT_SECRET_KEY
app.config['JWT_ALGORITHM'] = FlaskConfig.JWT_ALGORITHM
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=FlaskConfig.JWT_ACCESS_TOKEN_EXPIRES)
jwt = JWTManager(app)
"""
# jwt = JWTManager()
# jwt.init_app(app)
"""

app.config['MAIL_SERVER']= FlaskMailConfig.MAIL_SERVER
app.config['MAIL_PORT'] = FlaskMailConfig.MAIL_PORT
app.config['MAIL_USERNAME'] = FlaskMailConfig.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = FlaskMailConfig.MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = FlaskMailConfig.MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = FlaskMailConfig.MAIL_USE_SSL
mail=Mail(app)

app.register_blueprint(auth)
app.register_blueprint(userC)
app.register_blueprint(simba)


