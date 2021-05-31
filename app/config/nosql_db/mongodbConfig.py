import pymongo
import json

with open('server_info.json', mode='rt', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

conns = []
"""
def init_mongodb_db(user,password,host,port,db_name):
    dbconn = pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:{port}")
    db = dbconn.get_database(db_name)
    conns.append(db)
    return conns.pop()



mongodb = init_mongodb_db(
                        user=json_data['production']['DATABASES']['MONGODB']['USER']
                        ,password=json_data['production']['DATABASES']['MONGODB']['PASSWORD']
                        ,host=json_data['production']['DATABASES']['MONGODB']['HOST']
                        ,port=json_data['production']['DATABASES']['MONGODB']['PORT']
                        ,db_name=json_data['production']['DATABASES']['MONGODB']['NAME']
                        )
"""