from flask import Blueprint,request,json,jsonify
from app.controller.interventions_controller import Intervention
from app.validation import Validator
import datetime




intervention_blueprint = Blueprint("intervention_blueprint",__name__)

validate_input = Validator()
record = Intervention()


@intervention_blueprint.route('/interventions', methods = ["POST"])
def create_intervention():
    
    
   
    request_data = request.get_json(force=True)
    id = 1
    status = 'pending'
    createdOn = datetime.date.today().strftime('%Y-%m-%d')
    location = request_data['location']
    comment = request_data['comment']
    
    
    if not (validate_input.validate_digits_input(location)):
        return jsonify({"message": "location Field should contain an integer"}), 400
   
    if not (validate_input.validate_string_input(comment)):
        return jsonify({"message": "comment Field should contain strings"}), 400
    
    record.create_intervention(status, location,comment)

    return jsonify({"message": "Created intervention record"}), 201

@intervention_blueprint.route('/interventions/<int:id>/location', methods = ['PATCH'])
def patch_location(id):

    request_data = request.get_json()

    location = request_data['location']

    if not (validate_input.validate_digits_input(location)):
        return jsonify({"message": "location Field should contain an integer"}), 400
        
    record.update_location(location)
    return jsonify({"message":"Updated intervention record’s location"})



    

