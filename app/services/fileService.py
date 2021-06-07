import requests
import simplejson as json
from flask import *
from app.config.ReplacementConfig import *
from app.config.AppConfig import *
import urllib


class fileService:
    def __init__(self):
        pass


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    
           


