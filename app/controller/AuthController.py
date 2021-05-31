from flask import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity,get_jwt,get_jti)
from app.config.decorators.auth_jwt_decorator import *
from app.entities.user import *
from app.services.userService import *
from app.config.ReplacementConfig import *
import bcrypt
import datetime


auth = Blueprint('AuthController', __name__, url_prefix='/auth')

userService = userService()


@auth.route("/register", methods=["POST"])
def register():
    req = request.get_json()
    newUser = user_init(req)
    # print(newUser.toJSON)
    return userService.user_register(newUser)

@auth.route("/findAll", methods=["POST"])
def findAll():
    return userService.read_all()

@auth.route('/login', methods=['POST'])
def login():
	# input_data = request.get_json()
    user_email = request.json.get('email')	
    user_password = request.json.get('password')
    user_status = ReplacementConfig.IN
    return userService.login_check(user_email,user_password,user_status)

@auth.route('/logout', methods=['POST'])
@jwt_required() #jwt check
def logout():
	
	user_email = request.json.get('email')
	user_status = ReplacementConfig.OUT
	return userService.logout(user_email,user_status)


@auth.route("/protected", methods=["GET"])
@jwt_required() #jwt check좋
def protected():
    # Access the identity of the current user with get_jwt_identity
    # current_user = get_jwt_identity()
    # claims = get_jwt()
    # print("current_user : ",current_user)
    # print(claims['authority'])
    # print(claims['role'])
    return "hello"
    # return jsonify(logged_in_as=current_user), 200



@auth.route("/admin", methods=["GET"])
@jwt_required()    # jwt check
@admin_required()  # authority : admin check
def admin_test():
    current_user = get_jwt_identity()    
    return jsonify(logged_in_as=current_user), 200



@auth.route("/user", methods=["GET"])
@jwt_required()    # jwt check
@customer_required()   # authority : customer check
def user_test():
    current_user = get_jwt_identity()  
    return jsonify(logged_in_as=current_user), 200
	