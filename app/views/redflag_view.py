from flask import Blueprint,request,json,jsonify



redflag_blueprint = Blueprint("redflag_blueprint", __name__)

"""Endpoint for the index page"""

@redflag_blueprint.route('/')
def index():
    response = {
        "status":200,
        "message":"Welcome to I-Reporter"

    }
    return jsonify(response)
