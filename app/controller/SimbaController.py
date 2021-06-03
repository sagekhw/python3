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

@simba.route('/test', methods=['POST'])
def test():
    req = request.get_json()
    
    return smsService.send_oneMsg_toManyReceiver(req)


@simba.route("/email", methods=['post', 'get'])
def email_test():
    print(FlaskMailConfig.GMAIL_SERVER)
    return "hello"    
   


@simba.route("/sms/send/onemsg", methods=['post', 'get'])
def sms():
    req = request.get_json()
    """
    {
        "key":"essential",
        "user_id":"essential",
        "sender":"essential",
        "receiver":{
            "01012345678":"yaro",
            "01012345678":"simba"},
        "destination":"selection",
        "msg_type":"essential",
        "msg":"%고객명%님! 안녕하세요. sagekhw test",
        "title":"selection",
        "rdate":"selection",
        "rtime":"selection"  
    }
    """
    return smsService.send_oneMsg_toManyReceiver(req)


@simba.route("/sms/list", methods=['post', 'get'])
def sendList():
    req = request.get_json()
    """
    {
        "key": "essential", 
        "user_id": "essential",
        "page":"selection (default 1) integer",
        "page_size":"selection (default 30) 30~500 integer",
        "start_date":"selection (default recently) YYYYMMDD",
        "limit_day":"selection integer"
    }
    """
    return smsService.sendList(req)

@simba.route("/kakaoTalk/token", methods=['post', 'get'])
def getToken():
    req = request.get_json()
    """
    {
        "apikey": "essential", 
        "userid": "essential"
    }
    """
    return smsService.kakaoTalk_getToken(req)

@simba.route("/kakaoTalk/authChannel", methods=['post', 'get'])
def authChannel():
    req = request.get_json()
    """
    {
    "apikey": "essential", 
    "userid": "essential",
    "token": "essential",
    "plusid": "essential",
    "phonenumber": "essential"
    }
    """
    return smsService.kakaoTalkChannel_auth(req)

@simba.route("/kakaoTalk/channel/categorylist", methods=['post', 'get'])
def kakaoTalk_channel_categorylist():
    req = request.get_json()
    """
    {
        "apikey": "essential", 
        "userid": "essential",
        "token": "essential"
    }
    """
    return smsService.kakaoTalk_channel_categorylist(req)

@simba.route("/kakaoTalk/channel/list", methods=['post', 'get'])
def kakaoTalk_channel_registerList():
    req = request.get_json()
    """
    {
        "apikey": "essential", 
        "userid": "essential",
        "token": "essential"
    }
    """
    return smsService.kakaoTalk_channel_registerList(req)

@simba.route("/kakaoTalk/template/list", methods=['post', 'get'])
def kakaoTalk_template_list():
    req = request.get_json()
    """
    {
        "apikey": "essential", 
        "userid": "essential",
        "token": "essential",
        "senderkey":"essential",
        "tpl_code":"selection"
    }
    """
    return smsService.kakaoTalk_template_list(req)


@simba.route("/kakaoTalk/alimtalk/send", methods=['post', 'get'])
def kakaoTalk_alimtalk_send():
    req = request.get_json()
    """
    "apikey": "essential",
    "button_1":{
        "button":[
        {
            "linkMo": "http://www.sagekhw.com/",
            "linkPc": "http://www.sagekhw.com/",
            "linkType": "WL",
            "linkTypeName": "웹링크",
            "name": "자세히 보기"
        }
        ]
    },
    "failover": "Y",
    "fmessage_1": "essential",
    "fsubject_1": "대체문자 제목",
    "message_1": "essential",
    "receiver_1": "essential",
    "sender": "essential",
    "senderkey": "essential",
    "subject_1": "essential",
    "token": "essential",
    "tpl_code": "essential",
    "userid": "essential"
    }
    """
    req['button_1'] = json.dumps(req['button_1']) # button의 타입은 JSON 이어야 합니다.

    return smsService.kakaoTalk_alimtalk_send(req)

 