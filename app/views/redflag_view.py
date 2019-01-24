from flask import Blueprint,request,json,jsonify
from app.controller.users_controller import User
from app.utilities.auth import AuthHelper
from app.controller.redflag_contoller import Redflag
from app.validation import Validator
import datetime



redflag_blueprint = Blueprint("redflag_blueprint", __name__)

validate_input = Validator()
redflag_db = Redflag()
required = AuthHelper()

"""Endpoint for the index page"""

@redflag_blueprint.route('/')
def index():
    response = {
        "status":200,
        "message":"Welcome to I-Reporter"

    }
    return jsonify(response)

@redflag_blueprint.route('/redflags', methods = ["POST"])
@required.token_required
def create_redflag(current_user):

    """Endpoint for creating a redflag"""
    

    request_data = request.get_json(force=True)
    status = 'pending'
    createdOn = datetime.date.today().strftime('%Y-%m-%d')
    location = request_data['location']
    image = request_data['image']
    video = request_data['video']
    comment = request_data['comment']

    
    
    if not (validate_input.validate_digits_input(location)):
        return jsonify({"message": "location Field should contain an integer"}), 400
   
    if not (validate_input.validate_string_input(comment)):
        return jsonify({"message": "comment Field should contain strings"}), 400

    if not (validate_input.validate_string_input(image)):
        return jsonify({"message": "image Field should contain strings"}), 400
    
    if not (validate_input.validate_string_input(video)):
        return jsonify({"message": "video Field should contain strings"}), 400
    
    
    
    
    redflag = redflag_db.create_redflag(status, location,image,video,comment)
    redflagId = redflag_db.get_single_redflag(redflag['redflag_id'])
    
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is  False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
   

    return jsonify({'status':201,
                    'data':[{'id':redflag['redflag_id'],'message':'Redflag record created'}]
    }),201


@redflag_blueprint.route('/redflags/<int:redflag_id>/status', methods = ['PATCH'])
@required.token_required
def update_status(current_user,redflag_id):
    
    """Endpoint for updating redflag status"""

    request_data = request.get_json()

    status = request_data['status']
   
    if not (validate_input.validate_string_input(status)):
        return jsonify({"message": "status Field should contain a string"}), 400

    redflug = redflag_db.patch_redflag_status(status,redflag_id)
    print(str(redflug)+"******")
    redflagId = redflag_db.get_single_redflag(redflug['redflag_id'])
    
   
    
    if not redflug:
        return jsonify({
            'status':400,
            'data':[{'message': 'Redflag record with that id doesnot exist'}]
        }),400
    
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is not False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
    return jsonify({"status": 200,
                    "data":[{'id':redflug['redflag_id'], 'message':'Updated redflag record status'}]
                    }), 200


@redflag_blueprint.route('/redflags', methods = ["GET"])
@required.token_required
def get_redflags(current_user):

    """Endpoint for fetching all redflags"""

   
    redflags = redflag_db.get_all_redflags()
    if not redflags:
        return jsonify({
            'status':400,
            'message':'Redflag with that id doesnot exist'
        }),400

    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is  False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401

    return jsonify({
        'status':200,
        'data': redflags
    }),200

@redflag_blueprint.route('/redflags/<int:redflag_id>', methods = ["GET"])
@required.token_required
def get_single_redflag(current_user,redflag_id):

    """Endpoint for fetching a specific redflag"""
    
    
    redflag = redflag_db.get_single_redflag(redflag_id)

    if not redflag:
        return jsonify({
            'status':400,
            'data':[{'message':'Redflag with that id doesnot exist'}]
        }),400
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is  False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401

    return jsonify({
        'status':200,
        'data': redflag
        }),200

@redflag_blueprint.route('/redflags/<int:redflag_id>', methods = ["DELETE"])
@required.token_required
def delete_redflag(current_user,redflag_id):
    
    """Endpoint for deleting redflag"""
    
    
    flag = redflag_db.get_single_redflag(redflag_id)
    redflagId = redflag_db.get_single_redflag(redflag_id)

    if not  flag:
        return jsonify({
            'status':400,
            'data':[{'message': 'Redflag with that id is not found'}]
        }),400

    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is  False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401

    redflag_db.delete_redflag(redflag_id)
    return jsonify({
       'status':200,
       'data':[{'id':redflag_id,'message': 'Redflag record has been deleted'}]
    }),200



