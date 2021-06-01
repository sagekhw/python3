import requests
import json
from app.config.ReplacementConfig import *
from app.config.AppConfig import *


class smsService:
    def __init__(self):
        pass

    def send(self):
        send_url = 'https://apis.aligo.in/send/' # 요청을 던지는 URL, 현재는 문자보내기

        # ================================================================== 문자 보낼 때 필수 key값
        # API key, userid, sender, receiver, msg
        # API키, 알리고 사이트 아이디, 발신번호, 수신번호, 문자내용

        sms_data={'key': FlaskSMSConfig.ALIGO_KEY, #api key
                'user_id': FlaskSMSConfig.ALIGO_IDENTIFIER, # 알리고 사이트 아이디
                'sender': '070-4350-0558', # 발신번호
                'receiver': '01046682003', # 수신번호 (,활용하여 1000명까지 추가 가능)
                'msg': 'sagekhw test', #문자 내용 
                'msg_type' : 'SMS', #메세지 타입 (SMS, LMS)
                'title' : 'title', #메세지 제목 (장문에 적용)
                'destination' : '01000000000|홍길동', # %고객명% 치환용 입력
                #'rdate' : '예약날짜',
                #'rtime' : '예약시간',
                #'testmode_yn' : '' #테스트모드 적용 여부 Y/N
        }
        send_response = requests.post(send_url, data=sms_data)
        print (send_response.json())

    def sendList(self):
        list_url ='https://apis.aligo.in/list/'

        # ================================================================== 문자 보낼 때 필수 key값
        # API key, userid, sender, receiver, msg
        # API키, 알리고 사이트 아이디, 발신번호, 수신번호, 문자내용
        """
        list_data={
            'key': FlaskSMSConfig.ALIGO_KEY, #api key
            'user_id': FlaskSMSConfig.ALIGO_IDENTIFIER, # 알리고 사이트 아이디
            'testmode_yn' : 'N'
        }
        headersParam = {
            "Content-Type":"application/json"
        }
        print("list_data : ",type(json.dumps(list_data)),list_data)
        """
        list_data={
            "key": "ygymi2qceedlx4gg23yotngatxeyh8s6", #api key
            "user_id": "otheon", # 알리고 사이트 아이디
            "testmode_yn" : "N"
        }
        # list_response = requests.post(list_url,headers=headersParam, data=json.dumps(list_data))
        list_response = requests.post("https://apis.aligo.in/list/",headers='"Content-Type":"application/json"', data=list_data)
        print(list_response.json())