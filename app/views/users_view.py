from flask import Blueprint,request,json,jsonify
from app.validation import Validator
from app.controller.users_controller import User


Auth_blueprint = Blueprint("Auth_blueprint", __name__)

register = Validator()
user_db = User()


@Auth_blueprint.route('/auth/register', methods = ["POST"])

def register_user():
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

   
    
