
from flask import Flask
from flask_cors import CORS
from app.controller.NoticeController import *
from app.controller.AuthController import *
from app.controller.UserController import *
from app.controller.FileController import *
from app.config.AppConfig import *

app = init_application()
app.register_blueprint(auth)
app.register_blueprint(userC)
app.register_blueprint(notice)
app.register_blueprint(fileC)
# CORS(app, resources={r'*': {'origins': '*'}})

server_port = FlaskConfig.PORT
app.run(host="0.0.0.0", port=server_port)

