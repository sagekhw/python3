from flask import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity,get_jwt,get_jti)
from app.config.decorators.auth_jwt_decorator import *
from app.entities.user import *
from app.services.userService import *
from app.config.ReplacementConfig import *
import bcrypt
from datetime import *


userC = Blueprint('UserController', __name__, url_prefix='/user')

userService = userService()


@userC.route("/findAll", methods=["POST"])
def findAll():
    return userService.read_all()

@userC.route("/findByStaffEmail", methods=["POST"])
def findByStaffEmail():
    req = request.get_json()
    findUser = user(
                    email=req[STR.EMAIL]
                    ,authority=STR.SELEER
                    ,role=STR.STAFF
                    )
    return userService.findByEmailAndAuthorityAndRole(findUser)

@userC.route("/update", methods=["POST"])
# @jwt_required()    
# @seller_required()  
def update_user():
    # current_user = get_jwt_identity()
    req = request.get_json()
    newUser = user_update_init(req)
    newUser.id = req[STR.ID]
    print(newUser.email)
    # userService.updated_by = current_user
    return userService.update(newUser)

@userC.route("/delete", methods=["POST"])
# @jwt_required()    
# @seller_required()  
def delete_user():
    # current_user = get_jwt_identity()
    req = request.get_json()
    newUser = user(id=req[STR.ID])
    # newCompany.updated_by = current_user
    return userService.delete(newUser)