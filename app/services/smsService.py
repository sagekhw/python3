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
        try:
            result = dict()
            list_url ='https://apis.aligo.in/list/'
            headersParam = {
                "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
            }
            list_response = requests.post(list_url, headers=headersParam, data=sms_data)
        except Exception as e:
            resCode = 0
            result["error"] = "Exception!!"
        else:
            resCode = 200
            result=list_response.json()
        finally:
            result['code'] = resCode
            return result
 

    ############################## KAKAO TALK ##############################
    def kakaoTalk_getToken(self,kakaoTalk_data):
        try:
            result = dict()
            basic_send_url = 'https://kakaoapi.aligo.in/akv10/token/create/30/s/' # 요청을 던지는 URL, 현재는 토큰생성
            # token/create/토큰 유효시간/{y(년)/m(월)/d(일)/h(시)/i(분)/s(초)}/
            create_token_response = requests.post(basic_send_url, data=kakaoTalk_data)
        except Exception as e:
            resCode = 0
            result["error"] = "Exception!!"
        else:
            resCode = 200
            result = create_token_response.json()
        finally:
            result['code'] = resCode
            return result
    
    def kakaoTalkChannel_auth(self,kakaoTalk_data):
        try:
            result = dict()
            basic_send_url = 'https://kakaoapi.aligo.in/akv10/profile/auth/'
            channel_auth_response = requests.post(basic_send_url, data=kakaoTalk_data)
        except Exception as e:
            # print(e)
            resCode = 0
            result["error"] = "Exception!!"
        else:
            resCode = 200
            result = channel_auth_response.json()
        finally:
            result['code'] = resCode
            return result
            
    def kakaoTalk_channel_categorylist(self,kakaoTalk_data):result = dict()
        except Exception as e:
            resCode = 0
            print(e)
        else:
            resCode = 200
        finally:
            result['code'] = resCode
            return result

    def kakaoTalk_channel_registerList(self,kakaoTalk_data):
        try:
            result = dict()
            basic_send_url = 'https://kakaoapi.aligo.in/akv10/profile/list/ ' 
            category_search_response = requests.post(basic_send_url, data=kakaoTalk_data)
            
        except Exception as e:
            resCode = 0
            print(e)
        else:
            resCode = 200
            result = category_search_response.json()
        finally:
            result['code'] = resCode
            return result

    def kakaoTalk_template_list(self,kakaoTalk_data):
        try:
            result = dict()
            basic_send_url = 'https://kakaoapi.aligo.in/akv10/template/list/ ' 
            category_search_response = requests.post(basic_send_url, data=kakaoTalk_data)
            
        except Exception as e:
            resCode = 0
            print(e)
        else:
            
            result = category_search_response.json()            
        finally:
            result['code'] = resCode
            return result
    
    def kakaoTalk_alimtalk_send(self,kakaoTalk_data):
        try:
            result = dict()
            basic_send_url = 'https://kakaoapi.aligo.in/akv10/alimtalk/send/ ' 
            response = requests.post(basic_send_url, data=kakaoTalk_data)
        except Exception as e:
            resCode = 0
            # print(e)
        else:
            resCode = 200
            result = response.json()
        finally:
            result['code'] = resCode
            return result
           


