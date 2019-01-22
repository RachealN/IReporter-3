from flask import Flask
from app.views.redflag_view import redflag_blueprint
from app.views.users_view import Auth_blueprint
from app.views.interventions_view import intervention_blueprint





def initialize_app():
    app = Flask(__name__)
   
    app.register_blueprint(redflag_blueprint, url_prefix='/api/v1')
    app.register_blueprint(Auth_blueprint, url_prefix='/api/v1' )
    app.register_blueprint(intervention_blueprint, url_prefix='/api/v1' )
    
    

    return app