import requests
import simplejson as json
from flask import *
from app.config.ReplacementConfig import *
from app.config.AppConfig import *
import urllib


class smsService:
    def __init__(self):
        pass

    def rebuild_requestParam_onemsg(self,param):
        d=dict()
        receiver = list()
        destination = list()
        d= param

        for x in d.keys():
            receiver.append(x)
            temp = x+"|"+d[x]
            destination.append(temp)

        receivers = ",".join(receiver)
        destinations = ",".join(destination)
        return receivers,destinations

    def sms_common(self,url,data):
        try:
            result = dict()
            #     headersParam = {
            #         "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
            #     }
            response = requests.post(url, data=data)
        except Exception as e:
            resCode = 0
            # print(e)
        else:
            resCode = 200
            result = response.json()
        finally:
            result['code'] = resCode
            return result
            
    ############################## SMS ##############################
    def send_oneMsg_toManyReceiver(self,sms_data):
        try:
            result = dict()
            send_url = 'https://apis.aligo.in/send/'
            receivers,destinations = self.rebuild_requestParam_onemsg(sms_data['receiver'])
            sms_data['receiver'] = receivers
            sms_data['destination'] = destinations
            send_response = requests.post(send_url, data=sms_data)
        except Exception as e:
            resCode = 0
            result["error"] = "Exception!!"
        else:
            resCode = 200
            result = send_response.json()
        finally:
            result['code'] = resCode
            return result
        

    def sendList(self,sms_data):
        url = 'https://apis.aligo.in/list/'
        return self.sms_common(url= url,data= sms_data)
        
    ############################## KAKAO TALK ##############################
    def kakaoTalk_getToken(self,kakaoTalk_data):
        url = 'https://kakaoapi.aligo.in/akv10/token/create/30/s/'
        # token/create/토큰 유효시간/{y(년)/m(월)/d(일)/h(시)/i(분)/s(초)}/
        return self.sms_common(url= url,data= kakaoTalk_data)
    
    def kakaoTalkChannel_auth(self,kakaoTalk_data):
        url = 'https://kakaoapi.aligo.in/akv10/profile/auth/'
        return self.sms_common(url= url,data= kakaoTalk_data)
            
    def kakaoTalk_channel_categorylist(self,kakaoTalk_data):
        url = 'https://kakaoapi.aligo.in/akv10/category/' 
        return self.sms_common(url= url,data= kakaoTalk_data)

    def kakaoTalk_channel_registerList(self,kakaoTalk_data):
        url = 'https://kakaoapi.aligo.in/akv10/profile/list/ ' 
        return self.sms_common(url= url,data= kakaoTalk_data)

    def kakaoTalk_template_list(self,kakaoTalk_data):
        url = 'https://kakaoapi.aligo.in/akv10/template/list/ ' 
        return self.sms_common(url= url,data= kakaoTalk_data)
    
    def kakaoTalk_alimtalk_send(self,kakaoTalk_data):
        url = 'https://kakaoapi.aligo.in/akv10/alimtalk/send/ '
        return self.sms_common(url= url,data= kakaoTalk_data)
           


