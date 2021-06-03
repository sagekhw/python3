
import smtplib
# 이메일 메시지에 다양한 형식을 중첩하여 담기 위한 객체
from email.mime.multipart import MIMEMultipart
# 위의 모든 객체들을 생성할 수 있는 기본 객체
# MIMEBase(_maintype, _subtype)
# MIMEBase(<메인 타입>, <서브 타입>)
from email.mime.base import MIMEBase
# 이메일 메시지를 이진 데이터로 바꿔주는 인코더
from email import encoders
# 텍스트 형식
from email.mime.text import MIMEText
# 이미지 형식
from email.mime.image import MIMEImage
# 오디오 형식
from email.mime.audio import MIMEAudio

from app.config.ReplacementConfig import *
from app.config.AppConfig import *



class mailService:
    def __init__(self):
        pass

    def send(self):
        pass
        
    def send_email(self,smtp_info, msg):
        try:
            with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
                # TLS 보안 연결
                server.starttls() 
                # 로그인
                server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])
                # 로그인 된 서버에 이메일 전송
                response = server.sendmail(msg['from'], msg['to'], msg.as_string().encode('utf-8')) # 메시지를 보낼때는 .as_string() 메소드를 사용해서 문자열로 바꿔줍니다.
        except Exception as e:
            pass
        else:
            pass
        finally:
            return response

    def send_text(self,email_data):
        try:
            result = dict()
            smtp_info = dict({"smtp_server" : FlaskMailConfig.GMAIL_SERVER, # SMTP 서버 주소
                  "smtp_user_id" : FlaskMailConfig.GMAIL_USERNAME, 
                  "smtp_user_pw" : FlaskMailConfig.GMAIL_PASSWORD, 
                  "smtp_port" : FlaskMailConfig.GMAIL_PORT}) # SMTP 서버 포트

            # 메일 객체 생성 : 메시지 내용에는 한글이 들어가기 때문에 한글을 지원하는 문자 체계인 UTF-8을 명시해줍니다.
            msg = MIMEText(_text = email_data['content'], _charset = "utf-8") # 메일 내용

            msg['Subject'] = email_data['title']     # 메일 제목
            msg['From'] = email_data['sender']       # 송신자
            msg['To'] = email_data['receiver']       # 수신자

            response = self.send_email(smtp_info, msg)
            # 이메일을 성공적으로 보내면 결과는 {}
            if not response:
                resCode = 200
                print('이메일을 성공적으로 보냈습니다.')
            else:
                resCode = 0
                print(response)
                
        except Exception as e:
            resCode = 0
        else:
            resCode = 200
        finally:
            result['code'] = resCode
            return result

"""
def send(self):
        # 세션생성
        s = smtplib.SMTP(FlaskMailConfig.GMAIL_SERVER, FlaskMailConfig.GMAIL_PORT)
         # TLS 보안 연결
        s.starttls()
        s.login(FlaskMailConfig.GMAIL_USERNAME, FlaskMailConfig.GMAIL_PASSWORD)

        # 제목, 본문 작성
        msg = MIMEMultipart()
        msg[STR.SUBJECT] = '제목'
        msg.attach(MIMEText('본문', 'plain'))

        # 파일첨부 (파일 미첨부시 생략가능)
        attachment = open('temp.txt', 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        filename = 'temp.txt'
        part.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(part)
        toAddr= ["sagekhw@gmail.com","sagekhw@naver.com"]
        # 메일 전송
        # s.sendmail("sagekhw5@gmail.com", "sagekhw@naver.com", msg.as_string())
        response = s.sendmail("sagekhw5@gmail.com", toAddr, msg.as_string())
        s.quit()

        # 이메일을 성공적으로 보내면 결과는 {}
        if not response:
            print('이메일을 성공적으로 보냈습니다.')
        else:
            print(response)
"""