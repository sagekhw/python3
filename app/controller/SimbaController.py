from flask import *
from flask_mail import Mail, Message
from app.config.AppConfig import *
from app.services.mailService import *
from app.services.smsService import *

simba = Blueprint('SimbaController', __name__, url_prefix='/simba')
mailService = mailService()
smsService = smsService()
@simba.route('/a', methods=['GET'])
def a():    
    return {'hello':'a-simba'}



@simba.route("/email", methods=['post', 'get'])
def email_test():
    print(FlaskMailConfig.GMAIL_SERVER)
    return "hello"    
   


@simba.route("/sms", methods=['post', 'get'])
def sms():
    # print(FlaskSMSConfig.ALIGO_IDENTIFIER)
    smsService.send()
    return "hello"


@simba.route("/sms/list", methods=['post', 'get'])
def sendList():
    # print(FlaskSMSConfig.ALIGO_IDENTIFIER)
    smsService.sendList()
    return "hello"

