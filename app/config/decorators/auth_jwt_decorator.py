from flask import *
from functools import wraps
from flask_jwt_extended import ( verify_jwt_in_request, jwt_required,  get_jwt_identity, get_jwt)
from app.config.ReplacementConfig import *

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["authority"] == 'admin' and claims["role"] == 'owner':
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admins only!"), 403

        return decorator

    return wrapper

def seller_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["authority"] == STR.SELLER and claims["role"] == STR.OWNER:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Sellers only!"), 403

        return decorator

    return wrapper

def staff_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["authority"] == STR.SELLER and claims["role"] == STR.STAFF:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Staffs only!"), 403

        return decorator

    return wrapper


def customer_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["authority"] == STR.CUSTOMER and claims["role"] == STR.OWNER :
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Customers only!"), 403

        return decorator

    return wrapper