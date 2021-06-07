from flask import *
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message
from app.config.AppConfig import *
from app.services.mailService import *
from app.services.smsService import *
from app.services.fileService import *
from werkzeug.utils import secure_filename
import os

fileC = Blueprint('FileController', __name__, url_prefix='/file')
mailService = mailService()
smsService = smsService()
fileService = fileService()
FPATH = "/home/data/"
# FPATH = "~/oco/"


@fileC.route('/a', methods=['GET'])
def a():    
    return {'hello':'a-simba'}

@fileC.route('/fileList', methods=['POST'])
def list_file():
    fileList = dict()
    files = os.listdir(FPATH)
    i=0
    for x in files:
        path = FPATH+"/"+x
        
        fileList["'"+i+"'"] = path
        i=i+1
        
    # path = FPATH
    return fileList

#파일 업로드 처리
@fileC.route('/fileUpload', methods=['POST'])
@cross_origin()
def upload_file():
    f = request.files['files']
	#저장할 경로 + 파일명
    f.save(FPATH + secure_filename(f.filename))
    files = os.listdir(FPATH)
    return {'hello':f'{files}'}
    # return {'hello':'a-simba'}


#파일 download 처리
@fileC.route('/fileDownload', methods=['POST'])
def download_file():
    req = request.get_json()
    sw=0
    files = os.listdir(FPATH)
    for x in files:
        if(x==req['file']):
            sw=1
    path = FPATH
    return send_file(path + req['file'],
				attachment_filename = req['file'],
				as_attachment=True)