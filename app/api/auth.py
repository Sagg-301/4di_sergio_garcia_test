# Import flask dependencies
from flask import Blueprint, request
from ..common.Exceptions import *
from .validators import *
from ..common.Exceptions import ValidationException
from ..logic.Commands import *
from flask_login import current_user, login_required, logout_user, login_user
import traceback
import json

from ..logic.Commands import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth = Blueprint('auth', __name__, url_prefix='/auth/')


@ auth.route('/login', methods=['POST'])
def login():
    try:
        data = json.loads(request.data)

        validator = LoginValidator(data)
        validator.validate()

        command = LoginCommand(data)
        user = command.execute()

        login_user(user)

        return {"status": 1, "message": "User logged in successfully", "data": {"user": user.serialize()}}, 200
    except ValidationException as ex:
        return {"status": 0, "message": ex.message}, 422
    except InvalidCredentialsException as ex:
        traceback.print_exc()
        return {"status": 0, "message": ex.message}, 403
    except Exception as ex:
        traceback.print_exc()
        return {"status": 0, "message": "There was an internal error"}, 500
    
@ auth.route('/who-am-i', methods=['GET'])
@ login_required
def who_am_i():
    try:
        return {"status": 1, "data": current_user.serialize()}, 200
    except Exception as ex:
        traceback.print_exc()
        return {"status": 0, "message": "There was an internal error"}, 500


@ auth.route('/logout', methods=['POST'])
@ login_required
def logout():
    try:
        logout_user()
        return {"status": 1, "message": "Logged out successfully"}, 200
    except Exception as ex:
        traceback.print_exc()
        return {"status": 0, "message": "There was an internal error"}, 500
