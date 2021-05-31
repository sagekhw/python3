from app.config.sql_db.orm.crud import *
from app.config.sql_db.orm.read import *
from app.config.sql_db.orm.insert import *
from app.config.sql_db.orm.update import *
from app.config.ReplacementConfig import *
from app.entities.user import *
from datetime import *

class userRepository(user):
    def __init__(self):
        pass

    ################################################### SELECT ###################################################
    def findByRealAll(self):
        
        return crud.findByAll(self,USER)

    def findByUnregisteredAll(self):
        query= (
            f"SELECT " + 
            f"{STR.ID},{STR.NAME},{STR.EMAIL},{STR.SUB_EMAIL}" +
            f",{STR.SNS_TYPE},{STR.SNS_ID},{STR.PHONE_NUMBER},{STR.AUTHORITY} " + 
            f",{STR.ROLE},{STR.ACCUMULATED_MONEY},{STR.REGISTERED_AT},{STR.UNREGISTERED_AT} " + 
            f",{STR.UPDATED_AT},{STR.UPDATED_BY} " +
            f"FROM {STR.USER} WHERE {STR.UNREGISTERED_AT} IS NOT NULL"
        )
        return crud.findBySQL(self,query)

    def findByAll(self):
        query= (
            f"SELECT " + 
            f"{STR.ID},{STR.NAME},{STR.EMAIL},{STR.SUB_EMAIL}" +
            f",{STR.SNS_TYPE},{STR.SNS_ID},{STR.PHONE_NUMBER},{STR.AUTHORITY} " + 
            f",{STR.ROLE},{STR.ACCUMULATED_MONEY},{STR.REGISTERED_AT},{STR.UNREGISTERED_AT} " + 
            f",{STR.UPDATED_AT},{STR.UPDATED_BY} " +
            f"FROM {STR.USER} WHERE {STR.UNREGISTERED_AT} IS NULL"
        )
        return crud.findBySQL(self,query)
    
    
    def findByEmailWithoutPasswrodAndUnregistered(self,email):
        query= (
            f"SELECT " + 
            f"{STR.ID},{STR.NAME},{STR.EMAIL},{STR.SUB_EMAIL}" +
            f",{STR.SNS_TYPE},{STR.SNS_ID},{STR.PHONE_NUMBER},{STR.AUTHORITY} " + 
            f",{STR.ROLE},{STR.ACCUMULATED_MONEY},{STR.REGISTERED_AT},{STR.UNREGISTERED_AT} " + 
            f",{STR.UPDATED_AT},{STR.UPDATED_BY} " +
            f"FROM {STR.USER} WHERE {STR.UNREGISTERED_AT} IS NULL AND " +
            f"{STR.EMAIL} = '{email}'"
        )
        return crud.findBySQL(self,query)

    def findByEmail(self,email):
        query = f"SELECT * FROM {STR.USER} where {STR.EMAIL} = '{email}'"
        return crud.findBySQL(self,query)

    def findByEmail_Password(self,email,password):
        query = (
            f"SELECT * FROM {STR.USER} " + 
            f"where {STR.EMAIL} = '{email}' and {STR.PASSWORD} = '{password}'"
            )
        return crud.findBySQL(self,query)

    def findByEmailAndAuthorityAndRole(self,user):
        print(user.email,user.authority,user.role)
        query = (
            f"SELECT {STR.EMAIL},{STR.NAME},{STR.PHONE_NUMBER},{STR.SUB_EMAIL}  FROM {STR.USER} " + 
            f"where {STR.EMAIL} = '{user.email}' and {STR.AUTHORITY} = '{user.authority}' "
            f"and {STR.ROLE} = '{user.role}' "
            )
        print(query)
        return crud.findBySQL(self,query)
    
    def update_statusByEmail(self,email,status):
        query = (
            f"UPDATE {STR.USER} " +
            f"SET  {STR.STATUS} = '{status}' " +
            f"WHERE  {STR.EMAIL} = '{email}' AND {STR.UNREGISTERED_AT} IS NULL " 
            )
        return crud.UpdateBySQL(self,query)

    ################################################### INSERT ###################################################
    def save_user_sql(self,user):
        # tmp_registered_at = registered_at.strftime('%Y-%m-%d %H:%M:%S')
        query = (
            f"INSERT INTO {STR.USER} " +
            f" ({STR.EMAIL},{STR.NAME},{STR.SUB_EMAIL},{ STR.PASSWORD},{STR.SNS_TYPE},{STR.SNS_ID}, " + 
            f" {STR.STATUS},{STR.PHONE_NUMBER},{STR.AUTHORITY},{STR.ROLE}, " +
            f" {STR.ACCUMULATED_MONEY},{STR.REGISTERED_AT}) " +
            f"VALUES ('{user.email}','{user.name}','{user.sub_email}','{user.password}','{user.sns_type}','{user.sns_id}'," +
            f"'{user.status}','{user.phone_number}','{user.authority}','{user.role}'," +
            f"{user.accumulated_money},'{user.registered_at}'" +
            f")"
            )

        return crud.InsertBySQL(self,query)

    ################################################### UPDATE ###################################################
    def updateUserSql(self,user):
        user.updated_at=datetime.now()
        # tmp_updated_at = company.updated_at.strftime(STR.DATEFORMAT_TYPE1)
        query = (
            f"UPDATE {STR.USER} " +
            f"SET {STR.EMAIL} = '{user.email}' " +
            f",{STR.PASSWORD} = '{user.password}' " +
            f",{STR.PHONE_NUMBER} = '{user.phone_number}' " +
            f",{STR.UPDATED_AT} = '{user.updated_at}' " +
            f",{STR.UPDATED_BY} = '{user.updated_by}' " +
            f"WHERE {STR.ID} = {user.id} AND {STR.UNREGISTERED_AT} IS NULL"
            )
        return crud.UpdateBySQL(self,query)

    def update_companyId_ByUserid(self,userId,companyId,option=None):
        query = (
            f"UPDATE {STR.USER} " +
            f"SET  {STR.COMPANYID} = '{companyId}' " +
            f"WHERE  {STR.ID} = '{userId}' AND {STR.UNREGISTERED_AT} IS NULL " 
            )
        
        if(option == ReplacementConfig.INSTANT):
            return crud.UpdateBySQL(self,query)
        else:
            return query
    
    ################################################### DELETE ###################################################
    def deleteUserSql(self,user):
        user.unregistered_at=datetime.now()
        # tmp_updated_at = company.unregistered_at.strftime(STR.DATEFORMAT_TYPE1)
        query = (
            f"UPDATE {STR.USER} " +
            f"SET {STR.UNREGISTERED_AT} = '{user.unregistered_at}' " +
            f"WHERE {STR.ID} = {user.id} "
            )
        print(query)    
        # return "updateCompanySql"
        return crud.UpdateBySQL(self,query)

    ################################################### FUNCTION ###################################################
