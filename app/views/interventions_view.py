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
    
    
   
    request_data = request.get_json(force=True)
    # id = 1
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
    
    
    
    record = intervention_db.create_intervention(status, location,image,video,comment)
    print(record)
    interventionId = intervention_db.get_single_intervention(record['intervention_id'])
    
   

    return jsonify({'status':201,
                    'data':[{'id':record['intervention_id'],'message':'intervention record created'}]
    }),201

@intervention_blueprint.route('/interventions/<int:intervention_id>/location', methods = ['PATCH'])
def patch_location(intervention_id):

    request_data = request.get_json()

    location = request_data['location']

    if not (validate_input.validate_digits_input(location)):
        return jsonify({"message": "location Field should contain an integer"}), 400
        
   
    intervien = intervention_db.update_location(location,intervention_id)
    interventionId = intervention_db.get_single_intervention(intervien['intervention_id'])

    if not intervien:
        return jsonify({
            'status':400,
            'data':[{'message': 'intervention record with that id doesnot exist'}]
        }),400
    return jsonify({"status": 200,
                    "data":[{'id':intervien['intervention_id'], 'message':"Updated intervention record’s location"}]
                    }), 200
    

@intervention_blueprint.route('/interventions/<int:intervention_id>/comment', methods = ['PATCH'])
def patch_comment(intervention_id):

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
    return jsonify({"status": 200,
                    "data":[{'id':intervien['intervention_id'], 'message':"Updated intervention record’s comment"}]
                    }), 200

@intervention_blueprint.route('/interventions/<int:intervention_id>/status', methods = ['PATCH'])
def update_status(intervention_id):

    request_data = request.get_json()

    status = request_data['status']
   
    if not (validate_input.validate_string_input(status)):
        return jsonify({"message": "status Field should contain a string"}), 400

    intervien = intervention_db.update_status(status,intervention_id)
    interventionId = intervention_db.get_single_intervention(intervien['intervention_id'])
   
    print(intervien)
    if not intervien:
        return jsonify({
            'status':400,
            'data':[{'message': 'intervention record with that id doesnot exist'}]
        }),400
    return jsonify({"status": 200,
                    "data":[{'id':intervien['intervention_id'], 'message':'Updated intervention record status'}]
                    }), 200

            
@intervention_blueprint.route('/interventions/<int:intervention_id>', methods = ["DELETE"])
def delete_intervention(intervention_id):
    
    
    intervien = intervention_db.get_single_intervention(intervention_id)
    interventionId = intervention_db.get_single_intervention(intervention_id)

    if not  intervien:
        return jsonify({
            'status':400,
            'data':[{'message': 'intervention with that id is not found'}]
        }),400

    intervention_db.delete_intervention(intervention_id)
    return jsonify({
       'status':200,
       'data':[{'id':intervention_id,'message': 'intervention record has been deleted'}]
    }),200

@intervention_blueprint.route('/interventions/<int:intervention_id>', methods = ["GET"])
def get_single_intervention(intervention_id):
    
    
    intervention = intervention_db.get_single_intervention(intervention_id)

    if not intervention:
        return jsonify({
            'status':400,
            'data':[{'message':'intervention with that id doesnot exist'}]
        }),400
    return jsonify({
        'status':200,
        'data': intervention
        }),200

@intervention_blueprint.route('/interventions', methods = ["GET"])
def get_interventions():

    #  users = user_db.get_users()
    interventions = intervention_db.get_all_interventions()
    if not interventions:
        return jsonify({
            'status':400,
            'message':'intervention with that id doesnot exist'
        }),400


    return jsonify({
        'status':200,
        'data': interventions
    }),200





    

