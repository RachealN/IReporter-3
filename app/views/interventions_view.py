from flask import Blueprint,request,json,jsonify
from app.controller.interventions_controller import Intervention
from app.controller.users_controller import User
from app.utilities.auth import AuthHelper
from app.validation import Validator
import datetime




intervention_blueprint = Blueprint("intervention_blueprint",__name__)

validate_input = Validator()
intervention_db = Intervention()
required = AuthHelper()



@intervention_blueprint.route('/interventions', methods = ["POST"])
@required.token_required
def create_intervention(current_user):

    """Endpoint creating intervention"""
    
    
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
    
    
    record = intervention_db.create_intervention(status, location,image,video,comment)
    print(record)
    interventionId = intervention_db.get_single_intervention(record['intervention_id'])
    
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is  False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401

    return jsonify({'status':201,
                    'data':[{'id':record['intervention_id'],'message':'intervention record created'}]
    }),201

@intervention_blueprint.route('/interventions/<int:intervention_id>/location', methods = ['PATCH'])
@required.token_required
def patch_location(current_user,intervention_id):

    """Endpoint forupdating location"""

    request_data = request.get_json()

    location = request_data['location']

    if len(request_data.keys()) != 1:
        return jsonify({"message": "Some fields are missing"}), 400

    if not (validate_input.validate_digits_input(location)):
        return jsonify({"message": "location Field should contain an integer"}), 400
        
   
    intervien = intervention_db.update_location(location,intervention_id)
    interventionId = intervention_db.get_single_intervention(intervien['intervention_id'])

    
    if not intervien:
        return jsonify({
            'status':400,
            'data':[{'message': 'intervention record with that id doesnot exist'}]
        }),400
    
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
    return jsonify({"status": 200,
                    "data":[{'id':intervien['intervention_id'], 'message':"Updated intervention record’s location"}]
                    }), 200
    

@intervention_blueprint.route('/interventions/<int:intervention_id>/comment', methods = ['PATCH'])
@required.token_required
def patch_comment(current_user,intervention_id):

    """Endpoint for updating comment"""

    request_data = request.get_json()

    comment = request_data['comment']

    if not (validate_input.validate_string_input(comment)):
        return jsonify({"message": "comment Field should contain a string"}), 400
        
   
    intervien = intervention_db.update_comment(comment,intervention_id)
    interventionId = intervention_db.get_single_intervention(intervien['intervention_id'])

    if not intervien:
        return jsonify({
            'status':400,
            'data':[{'message': 'intervention record with that id doesnot exist'}]
        }),400
    
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is  False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401

    return jsonify({"status": 200,
                    "data":[{'id':intervien['intervention_id'], 'message':"Updated intervention record’s comment"}]
                    }), 200

@intervention_blueprint.route('/interventions/<int:intervention_id>/status', methods = ['PATCH'])
@required.token_required
def update_status(current_user,intervention_id):

    """Endpoint for updating status"""

    request_data = request.get_json()

    status = request_data['status']
   
    if not (validate_input.validate_string_input(status)):
        return jsonify({"message": "status Field should contain a string"}), 400

    if len(request_data.keys()) != 1:
        return jsonify({"message": "Some fields are missing"}), 400

    intervien = intervention_db.update_status(status,intervention_id)
    print(intervien)
    interventionId = intervention_db.get_single_intervention(intervien['intervention_id'])
   
    
    if not interventionId or interventionId['status'] == 'rejected':
        return jsonify({"message": "The intervention record you are editing doesnt exist"}), 404

    if not intervien:
        return jsonify({
            'status':400,
            'data':[{'message': 'intervention record with that id doesnot exist'}]
        }),400

    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is not False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401

    return jsonify({"status": 200,
                    "data":[{'id':intervien['intervention_id'], 'message':'Updated intervention record status'}]
                    }), 200

            
@intervention_blueprint.route('/interventions/<int:intervention_id>', methods = ["DELETE"])
@required.token_required
def delete_intervention(current_user,intervention_id):

    """Endpoint for deleting intervention """
    
    
    intervien = intervention_db.get_single_intervention(intervention_id)
    interventionId = intervention_db.get_single_intervention(intervention_id)

    if not  intervien:
        return jsonify({
            'status':400,
            'data':[{'message': 'intervention with that id is not found'}]
        }),400

    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401


    intervention_db.delete_intervention(intervention_id)
    return jsonify({
       'status':200,
       'data':[{'id':intervention_id,'message': 'intervention record has been deleted'}]
    }),200

@intervention_blueprint.route('/interventions/<int:intervention_id>', methods = ["GET"])
@required.token_required
def get_single_intervention(current_user,intervention_id):

    """Endpoint for getting a specific intervention"""
    
    
    intervention = intervention_db.get_single_intervention(intervention_id)

    if not intervention:
        return jsonify({
            'status':400,
            'data':[{'message':'intervention with that id doesnot exist'}]
        }),400

    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401

    return jsonify({
        'status':200,
        'data': intervention
        }),200

@intervention_blueprint.route('/interventions', methods = ["GET"])
@required.token_required
def get_interventions(current_user):

    """Endpoint for getting intervention"""

   
    interventions = intervention_db.get_all_interventions()
    if not interventions:
        return jsonify({
            'status':400,
            'message':'intervention with that id doesnot exist'
        }),400
    
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401

    return jsonify({
        'status':200,
        'data': interventions
    }),200





    

