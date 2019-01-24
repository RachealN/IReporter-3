from flask import Blueprint,request,json,jsonify
from app.validation import Validator
from app.controller.users_controller import User
from app.utilities.auth import AuthHelper


Auth_blueprint = Blueprint("Auth_blueprint", __name__)

validate_input = Validator()
user_db = User()
token = AuthHelper()




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
    
    

    validate_email = Validator().validate_email(email)
    validate_firstname = Validator().validate_string_input(firstname)
    validate_lastname= Validator().validate_string_input(lastname)
    validate_password = Validator().validate_password(password)
    validate_phonenumber = Validator().validate_digits_input(phonenumber)

    if not validate_email or not validate_lastname or not validate_password \
    or not validate_phonenumber or not validate_firstname:
        return jsonify({'message':'some fields are missing or incorrect'}),400

    

    
    if not validate_input.validate_email(email):
        return jsonify({'message':'You have an invalid email or the email is missing'}),400

    if not validate_input.validate_password(password):
        return jsonify({'message':'You have an invalid password or password is missing'}),400


    
    if user_db.check_user_by_email(email):
        return jsonify({'message':'Email already exists'}),400

    user_db.register_user(request_data['firstname'],request_data['lastname'],request_data['email'],request_data['password'],request_data['phonenumber'],request_data['username'])
    return jsonify({
        'status':201,
        'message':'user created successfully',
        'data':user_db.check_user_by_email(email)
        }),201

    


@Auth_blueprint.route('/auth/login', methods = ["POST"])
def login_user():

    """Handle POST request for this Endpoint. Url ---> /api/vi/authcd/login"""

    request_data = request.get_json(force=True)
    if len(request_data.keys()) != 2:
        return jsonify({"message": "some fields are missing"}), 401
    email = request_data['email']
    password = request_data['password']
    
    if not validate_input.validate_email(email):
        return jsonify({"message": "You entered an invalid email or email is missing"}), 401

    if not validate_input.validate_password(password):
        return jsonify({"message": "You entered an invalid password "}), 401


    check_user = user_db.check_user_by_email(email)
    if check_user:
        payload = token.encode_auth_token(check_user)
        return jsonify({
            'status':200,
            'message': 'login successful',
            'token': payload[0],
            'user':check_user}), 200

    return jsonify({"message": "You are not a system user"}), 401


@Auth_blueprint.route('/auth/users', methods = ["GET"])
def get_all_users():
    users = user_db.get_users()
    if not users:
        return jsonify({
            'status':400,
            'message':'user with that id doesnot exist'
        }),400


    return jsonify({
        'status':200,
        'data': users
    }),200

@Auth_blueprint.route('/auth/users/<int:user_id>', methods = ["GET"])
def get_user(user_id):
    user = user_db.get_user_by_userid(user_id)
    if not user:
        return jsonify({
            'status':400,
            'data':[{'message':'user with that id doesnot exist'}]
        }),400
    return jsonify({
        'status':200,
        'data': user
        }),200

@Auth_blueprint.route('/auth/users/<int:user_id>', methods = ["DELETE"])
def Delete_user(user_id):
    
    userId = user_db.get_user_by_userid(user_id)
    
    
    if not  userId:
        return jsonify({
            'status':400,
            'data':[{'message': 'user with that id is not found'}]
        }),400
    user_db.delete_user(user_id)
    return jsonify({
       'status':200,
       'data':[{'id':user_id,'message': 'user deleted succesfully'}]
    }),200

@Auth_blueprint.route('/auth/users/<int:user_id>', methods = ["PUT"])
def update_user(user_id):
    
    userId = user_db.get_user_by_userid(user_id)

    if not userId:
        return jsonify({
            'status':400,
            'data':[{'message':'user with that id doesnot exist'}]
        }),400
    user_db.update_user(user_id)
    return jsonify({
        'status':201,
       'data':[{'message':'user updated succesfully'}]

    })


    
    