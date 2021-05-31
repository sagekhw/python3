from app.config.sql_db.orm.crud import *
from app.repositories.userRepository import *
from app.entities.user import *
from flask import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity,get_jwt,get_jti)
from app.config.nosql_db.mongodbConfig import *
import bcrypt
from datetime import datetime
import simplejson as json

repo = userRepository()

class userService:
    def __init__(self):
        pass

    ### about Repository
    def read_all(self):
        try:
            temp = repo.findByAll()
            
        except Exception as e:
            print(e)
            return "False"
        else:
            if(not temp):
                return "nothing"
            else:
                return jsonify(
                        code = 200,
                        result = temp
                        )
        finally:
            pass
        
 
    def readByEmail(self,email):
        try:
            temp = repo.findByEmail(email)
        except Exception as e:
            print(e)
            return "False"
        else:
            if(not temp):
                return "nothing"
            else:
                res = temp
                return res
        finally:
            pass
    
    def findByEmailWithoutPasswrodAndUnregistered(self,email):
        try:
            temp = repo.findByEmailWithoutPasswrodAndUnregistered(email)
        except Exception as e:
            print(e)
            return "False"
        else:
            if(not temp):
                return "nothing"
            else:
                res = temp
                return res
        finally:
            pass

    def findByEmailAndAuthorityAndRole(self,user):

        if ((user.authority == 'customer' and user.role == 'owner')
            or (user.authority == 'seller' and user.role == 'owner')
            or (user.authority == 'seller' and user.role == 'staff')
            or (user.authority == 'admin' and user.role == 'owner')
            ):
            try:
                print(user.email,user.athority,user.role)
                temp = repo.findByEmailAndAuthorityAndRole(user)
                
            except Exception as e:
                print(e)
                return "False"
            else:
                if(not temp):
                    return "nothing"
                else:
                    return jsonify(
                        code = 200,
                        result = temp
                        )
            finally:
                pass
        else:
        	return jsonify(
                code = 5101,
        		result = "Unknown properties"
        		)
        
    def readByEmailandPassword(self,email,password):
        try:
            temp = repo.findByEmail_Password(email,password)
        except Exception as e:
            print(e)
            return "False"
        else:
                res = temp
                return res
        finally:
            pass
    def encrypted_password(self,pw):
        tmp = bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt())
        password = tmp.decode("utf-8")
        return password

    def status_update_sql(self,emailParam,statusParam):
        try:
            temp = repo.update_statusByEmail(email=emailParam,status=statusParam)
        except Exception as e:
            print(e)
            return False
        else:
            return True
        finally:
            pass
            
    def user_register_sql(self,user):
        try:
            origin_pw = user.password
            user.password = self.encrypted_password(origin_pw)
            print("user.password : ",user.password)
            user.status = 'out'
            user.accumulated_money = 0
            user.registered_at=datetime.now()
            
            temp = repo.save_user_sql(user)
        except Exception as e:
            print(e)
            return False
        else:
            return True
        finally:
            pass

    ### about service logic
    def user_register(self,user):
        """
        user_register > user_register_sql+encrypted_password > userRepository:save_user_sql
        """
        if ((user.authority == STR.CUSTOMER and user.role == STR.OWNER)
            or (user.authority == STR.SELLER and user.role == STR.OWNER)
            or (user.authority == STR.SELLER and user.role == STR.STAFF)
            or (user.authority == STR.ADMIN and user.role == STR.OWNER)
            ):
            result = self.user_register_sql(user)
            if result:
                return jsonify(
                code = 200,
        		result = "success"
        		)
            else:
                return jsonify(
                code = 500,
        		result = "false"
        		)
        else:
        	return jsonify(
                code = 5101,
        		result = "Unknown properties"
        		)

    def login_check(self,user_email,user_password,user_status):
        temp = self.readByEmail(user_email)
        
        if(temp == "nothing" or temp == "False"):
            return jsonify(
                code = 5102,
                result = "This information does not exist."
                )
        else:
            input_authority = temp[0]['authority']
            if(not input_authority):
                return jsonify(
                    code = 5102,
                    result = "false"
                    )
            
            input_role = temp[0]['role']
            if(not input_role):
                return jsonify(
                    code = 5102,
                    result = "false"
                    )
            pw = temp[0]['password']
            if(not bcrypt.checkpw(user_password.encode("utf-8"), pw.encode("utf-8"))):
                return jsonify(
                    code = 5102,
                    result = "false"
                    )
            if(not self.status_update_sql(user_email,user_status)):
                return jsonify(
                    code = 5102,
                    result = "false"
                    )
            #insert_logInOutLog_mongodb(user_email,user_status)
            if(temp == "nothing" or temp == "False"):
                return jsonify(
                    code = 5102,
                    result = "This information does not exist."
                    )
            additional_claims = {"authority": f"{input_authority}","role":f"{input_role}"}
            return jsonify(result = "success",
                # 검증된 경우, access 토큰 반환
                access_token = create_access_token(identity = user_email,
                                                additional_claims=additional_claims
                                                )
            )
    def logout(self,user_email,user_status):
        temp = self.readByEmail(user_email)
        if(temp == "nothing" or temp == "False"):
            return jsonify(
                code = 5102,
                result = "This information does not exist."
                )
        else:         
            if(not self.status_update_sql(user_email,user_status)):
                return jsonify(
                code = 5102,
                result = "This information does not exist."
                )
            else:
                insert_logInOutLog_mongodb(user_email,user_status)
                return jsonify(
                code = 200,
                result = "logout"
                )

    def update(self,p_user):
        try: 
            temp = repo.updateUserSql(p_user)        
        except Exception as e:
            print(e)
            return jsonify(
                code = 500,
        		result = "false"
        		)
        else:
            return jsonify(
                code = 200,
        		result = "success"
        		)
        finally:
            pass
    
    # def update_companyId_ByUserid(self,userId,companyId):
    #     try: 
    #         temp = repo.update_companyId_ByUserid(userId,companyId)        
    #     except Exception as e:
    #         print(e)
    #         return jsonify(
    #             code = 500,
    #     		result = "false"
    #     		)
    #     else:
    #         return jsonify(
    #             code = 200,
    #     		result = "success"
    #     		)
    #     finally:
    #         pass

    # def updateById(self,p_user):
    #     try: 
    #         temp = repo.updateUserSql(p_user)        
    #     except Exception as e:
    #         print(e)
    #         return jsonify(
    #             code = 500,
    #     		result = "false"
    #     		)
    #     else:
    #         return jsonify(
    #             code = 200,
    #     		result = "success"
    #     		)
    #     finally:
    #         pass

    def delete(self,p_user):
        try:            
            temp = repo.deleteUserSql(p_user)       
        except Exception as e:
            print(e)
            return jsonify(
                code = 500,
        		result = "false"
        		)
        else:
            return jsonify(
                code = 200,
        		result = "success"
        		)
        finally:
            pass


# To save login logout history in mongodb ocostore > user_log
def insert_logInOutLog_mongodb(user_email,user_status):
    temp = mongodb.user_log.insert({"email":user_email,"status":user_status,"time":datetime.now()})
    items = mongodb.user_log.find({})
    # for item in items : 
    #     print (item)
    
