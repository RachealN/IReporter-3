from flask import Blueprint,request,json,jsonify
from app.validation import Validator
from app.controller.users_controller import User
from app.utilities.auth import AuthHelper


Auth_blueprint = Blueprint("Auth_blueprint", __name__)

register = Validator()
user_db = User()
token = AuthHelper()
login = Validator()



@Auth_blueprint.route('/auth/register', methods = ["POST"])
def register_user():

    """Handle POST request for this Endpoint. Url ---> /api/v1/auth/register"""

    request_data = request.get_json()

    firstname = request_data['firstname']
    lastname = request_data['lastname']
    email = request_data['email']
    password = request_data['password']
    phonenumber = request_data['phonenumber']
    username = request_data['username']
    isAdmin = True
    

    
    if not register.validate_email(email):
        return jsonify({'message':'You have an invalid email or the email is missing'}),400

    if not register.validate_password(password):
        return jsonify({'message':'You have an invalid password or password is missing'}),400


    
    if user_db.check_user_by_email(email):
        return jsonify({'message':'Email already exists'}),400

    user_db.register_user(request_data['firstname'],request_data['lastname'],request_data['email'],request_data['password'],request_data['phonenumber'],request_data['username'])
    user_db.check_user_by_email(email)
    return jsonify({'message':'user created successfully'}),201



@Auth_blueprint.route('/auth/login', methods = ["POST"])
def login_user():

    """Handle POST request for this Endpoint. Url ---> /api/vi/auth/login"""

    request_data = request.get_json(force=True)
    if len(request_data.keys()) != 2:
        return jsonify({"message": "some fields are missing"}), 401
    email = request_data['email']
    password = request_data['password']
    
    if not login.validate_email(email):
        return jsonify({"message": "You entered an invalid email or email is missing"}), 401

    if not login.validate_password(password):
        return jsonify({"message": "You entered an invalid password or password should be atleast 8 characters long"}), 401


    check_user = user_db.check_user_by_email(email)
    if check_user:
        payload = token.encode_auth_token(check_user)
        return jsonify({
            'message': 'login successful',
            'auth_token': payload}), 200

    return jsonify({"message": "You are not a system user"}), 401