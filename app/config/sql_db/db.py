import pymysql
import json

with open('server_info.json', mode='rt', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    #print(json_data)
    
    
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
    
"""
def init_db_query(query):
    try: 
        db_connect = db_init()
        cur = db_connect.cursor(pymysql.cursors.DictCursor)
        cur.execute(query)
        rv = cur.fetchall()
    except Exception as e:
        print(e)
         # 오류가 발생하면 롤백
        db_connect.rollback()
    else:
        pass
    finally:
        cur.close()
        db_connect.close()
        return rv

def init_db_commit_query(query):
    try: 
        db_connect = db_init()
        cur = db_connect.cursor(pymysql.cursors.DictCursor)
        cur.execute(query)
        rv = cur.fetchall()     
    except Exception as e:
        print(e)
         # 오류가 발생하면 롤백
        
        db_connect.rollback()
    else:
        db_connect.commit()
        
    finally:
        cur.close()
        db_connect.close()
        return rv
"""