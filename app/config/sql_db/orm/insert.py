from app.config.sql_db.db import *
from app.config.sql_db.orm.crud import *


class insert:
    def __init__(self):
        pass

    def InsertBySQL(self,query):
        return _insert_common(query)

def _insert_common(query):
    if not query:
        return None
    else:
        return init_db_commit_query(query)
        