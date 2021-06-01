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



@simba.route("/kakao/token", methods=['post', 'get'])
def token():
    # print(FlaskSMSConfig.ALIGO_IDENTIFIER)
    basic_send_url = 'https://kakaoapi.aligo.in/akv10/token/create/30/s/' # 요청을 던지는 URL, 현재는 토큰생성
    # token/create/토큰 유효시간/{y(년)/m(월)/d(일)/h(시)/i(분)/s(초)}/

    # ================================================================== 토큰 생성 필수 key값
    # API key, userid
    # API키, 알리고 사이트 아이디

    sms_data={'apikey': 'ygymi2qceedlx4gg23yotngatxeyh8s6', #api key
            'userid': 'otheon', # 알리고 사이트 아이디
    }

    create_token_response = requests.post(basic_send_url, data=sms_data)


    print(create_token_response.json())
    return "hello"
