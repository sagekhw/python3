from .insert import insert
from .read import read
from .update import update
from app.config.sql_db.db import *
import pymysql

class crud(insert,read,update):
    def __init__(self):
        pass

    def init_db(self):
        return db_init()
    
    def getCursor(self,db_connect):
        return db_connect.cursor(pymysql.cursors.DictCursor)

    def init_db_query(self,query):
        db_connect = db_init()
        cur = db_connect.cursor(pymysql.cursors.DictCursor)
        cur.execute(query)
        rv = cur.fetchall()
        cur.close()
        db_connect.close()
        return rv

    def _commit_common(query):
        if not query:
            return None
        else:
            return init_db_commit_query(query)
            
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

    