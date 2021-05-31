from app.config.sql_db.db import *
from app.config.decorators.mariadb_decorator import *


class read:
    def __init__(self):
        pass
    
    def findByAll(self,entity):
        return _select_all(entity)

    
    def findBySQL(self,query):
        return _select_common(query)
  

def _select_all(table):
    query="SELECT * FROM "+table
    return _select_common(query)

def _select_common(query):
    if not query:
        return None
    else:
        return init_db_query(query)
        

        
    