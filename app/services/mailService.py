
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



class mailService:
    def __init__(self):
        pass

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

