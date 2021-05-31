from app.config.sql_db.orm.crud import crud
from app.config.sql_db.orm.read import *
from app.config.ReplacementConfig import *

class user(crud):
    
    def __init__(self
                ,id=None
                # ,name=None
                ,email=None
                ,sub_email=None
                ,name=None
                ,password=None
                ,sns_type=None
                ,sns_id=None
                ,status=None
                ,phone_number=None
                ,authority=None
                ,role=None
                ,accumulated_money=None
                ,connect_time=None
                ,registered_at=None
                ,unregistered_at=None
                ,updated_at=None
                ,updated_by=None
                ):
        self.table_name = self.__class__.__name__
        self.id = id
        self.name = name
        self.email = email
        self.sub_email = sub_email
        self.name = name
        self.password = password
        self.sns_type = sns_type
        self.sns_id = sns_id
        self.status = status
        self.phone_number = phone_number
        self.authority = authority
        self.role = role
        self.accumulated_money = accumulated_money
        self.connect_time = connect_time
        self.registered_at = registered_at
        self.unregistered_at = unregistered_at
        self.updated_at = updated_at
        self.updated_by = updated_by
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

def user_init(req):
    return user(
                email=req[STR.EMAIL]
                ,password=req[STR.PASSWORD]
                ,sub_email=req[STR.SUB_EMAIL]
                ,name=req[STR.NAME]
                ,sns_type=req[STR.SNS_TYPE]
                ,sns_id=req[STR.SNS_ID]
                # ,status=req[STR.STATUS]
                ,phone_number=req[STR.PHONE_NUMBER]
                ,authority=req[STR.AUTHORITY]
                ,role=req[STR.ROLE]
                # ,accumulated_money=req[STR.ACCUMULATED_MONEY]
                # ,registered_at=req[STR.REGISTERED_AT]
                # ,unregistered_at=req[STR.UNREGISTERED_AT]
                # ,updated_at=req[STR.UPDATED_AT]
                # ,updated_by=req[STR.UPDATED_BY]
                )

def user_update_init(req):
    return user(
                email=req[STR.EMAIL]
                ,password=req[STR.PASSWORD]
                # ,status=req[STR.STATUS]
                ,phone_number=req[STR.PHONE_NUMBER]
                ,authority=req[STR.AUTHORITY]
                ,role=req[STR.ROLE]
                )

def response_user(userObj):
    return user(
                email=userObj.email
                ,name=userObj.name
                ,phone_number=userObj.phone_number
                ,sub_email=userObj.sub_email
                )
