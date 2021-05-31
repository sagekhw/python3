
import json

with open('server_info.json', mode='rt', encoding='utf-8') as json_file:
    json_data = json.load(json_file)


class FlaskConfig():
    JWT_SECRET_KEY = json_data['production']['SERVER']['JWT_SECRET_KEY']
    JWT_ALGORITHM = json_data['production']['SERVER']['JWT_ALGORITHM']
    JWT_ACCESS_TOKEN_EXPIRES = json_data['production']['SERVER']['JWT_ACCESS_TOKEN_EXPIRES']
    HOST = json_data['production']['SERVER']['HOST']
    PORT = json_data['production']['SERVER']['PORT']


class FlaskMailConfig():
    MAIL_SERVER = json_data['production']['FLASKMAIL']['MAIL_SERVER']
    MAIL_PORT = json_data['production']['FLASKMAIL']['MAIL_PORT']
    MAIL_USERNAME = json_data['production']['FLASKMAIL']['MAIL_USERNAME']
    MAIL_PASSWORD = json_data['production']['FLASKMAIL']['MAIL_PASSWORD']
    MAIL_USE_TLS = json_data['production']['FLASKMAIL']['MAIL_USE_TLS']
    MAIL_USE_SSL = json_data['production']['FLASKMAIL']['MAIL_USE_SSL']