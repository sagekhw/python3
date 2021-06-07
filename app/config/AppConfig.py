
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import *
from flask_jwt_extended import JWTManager
from flask_mail import Mail, Message

# from app.controller.SimbaController import *
# from app.controller.AuthController import *
# from app.controller.UserController import *
from app.config.AppConfig import *
import datetime
import json

with open('server_info.json', mode='rt', encoding='utf-8') as json_file:
    json_data = json.load(json_file)



class FlaskConfig():
    JWT_SECRET_KEY = json_data['production']['SERVER']['JWT_SECRET_KEY']
    JWT_ALGORITHM = json_data['production']['SERVER']['JWT_ALGORITHM']
    JWT_ACCESS_TOKEN_EXPIRES = json_data['production']['SERVER']['JWT_ACCESS_TOKEN_EXPIRES']
    HOST = json_data['production']['SERVER']['HOST']
    PORT = json_data['production']['SERVER']['PORT']


class FlaskMailConfig():
    GMAIL_SERVER = json_data['production']['MAIL']['GOOGLE']['SERVER']
    GMAIL_PORT = json_data['production']['MAIL']['GOOGLE']['PORT']
    GMAIL_USERNAME = json_data['production']['MAIL']['GOOGLE']['USERNAME']
    GMAIL_PASSWORD = json_data['production']['MAIL']['GOOGLE']['PASSWORD']
    GMAIL_USE_TLS = json_data['production']['MAIL']['GOOGLE']['USE_TLS']
    GMAIL_USE_SSL = json_data['production']['MAIL']['GOOGLE']['USE_SSL']

class FlaskSMSConfig():
    ALIGO_IDENTIFIER = json_data['production']['SMS']['ALIGO']['IDENTIFIER']
    ALIGO_KEY = json_data['production']['SMS']['ALIGO']['KEY']



class FlaskAppConfig():
    def __init__(self):
        pass


### function
# mail = Mail()
def init_application():
        print('init app')
        app = Flask(__name__)
        # app = FlaskAppConfig.init_app(app)
        CORS(app, resources={r'/*': {'origins': '*'}})

        #### FILE ####
        app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
        # app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 #1MB
        # app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']

        #### JWT ####
        # JWT 매니저 활성화

        app.config["JWT_SECRET_KEY"] = FlaskConfig.JWT_SECRET_KEY
        app.config['JWT_ALGORITHM'] = FlaskConfig.JWT_ALGORITHM
        app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=FlaskConfig.JWT_ACCESS_TOKEN_EXPIRES)
        jwt = JWTManager(app)

        app.config['CORS_HEADERS'] = 'Content-Type'
        """
        # jwt = JWTManager()
        # jwt.init_app(app)
        """

        return app