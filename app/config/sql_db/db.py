import pymysql
import json

with open('server_info.json', mode='rt', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

    
    
conns = []
default_cursor = pymysql.cursors.DictCursor
def db_init():
    dbconn = pymysql.connect(
        host=json_data['production']['DATABASES']['MARIADB']['HOST']        ,
        port=json_data['production']['DATABASES']['MARIADB']['PORT']        , 
        user=json_data['production']['DATABASES']['MARIADB']['USER']        , 
        passwd=json_data['production']['DATABASES']['MARIADB']['PASSWORD']  , 
        db=json_data['production']['DATABASES']['MARIADB']['NAME']          ,
        charset='utf8'                                                      ,
        cursorclass=pymysql.cursors.DictCursor                              ,
        autocommit=False
    )

    conns.append(dbconn)

    return conns.pop()
    
