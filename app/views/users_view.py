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
    isAdmin = True
    

    
    if not validate_input.validate_email(email):
        return jsonify({'message':'You have an invalid email or the email is missing'}),400

    if not validate_input.validate_password(password):
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
    
    if not validate_input.validate_email(email):
        return jsonify({"message": "You entered an invalid email or email is missing"}), 401

    if not validate_input.validate_password(password):
        return jsonify({"message": "You entered an invalid password or password should be atleast 8 characters long"}), 401


    check_user = user_db.check_user_by_email(email)
    if check_user:
        payload = token.encode_auth_token(check_user)
        return jsonify({
            'message': 'login successful',
            'auth_token': payload}), 200

    return jsonify({"message": "You are not a system user"}), 401


@Auth_blueprint.route('/auth/users', methods = ["GET"])
@token.token_required
def get_all_users(current_user):
    current_user=current_user.get('sub')
    print(current_user)
    # if current_user.get('isAdmin') is  'False':
    #     return jsonify({
    #         'message':'You  cannot perform this function'
    #     }),401
    return jsonify({
        'users': user_db.get_users()
    }),200

@Auth_blueprint.route('/auth/users/<int:user_id>', methods = ["GET"])
def get_user(user_id):
   return jsonify({
        'user': user_db.get_user_by_userid(user_id)
    })

@Auth_blueprint.route('/auth/users/<int:user_id>', methods = ["DELETE"])
def Delete_user(user_id):
    return jsonify({
       'user':user_db.delete_user(user_id),
       'message': 'user deleted succesfully'
    })

@Auth_blueprint.route('/auth/users/<int:user_id>', methods = ["PUT"])
def update_user(user_id):
    return jsonify({
       'user':user_db.update_user(user_id),
       'message':'user updated succesfully' 

    })
    