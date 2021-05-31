from app.config.sql_db.db import *
from app.config.sql_db.orm.crud import *


class update:
    def __init__(self):
        pass

    def UpdateBySQL(self,query):
        return _update_common(query)

def _update_common(query):
    if not query:
        return None
    else:
        return init_db_commit_query(query)