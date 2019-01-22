from flask import request,jsonify
import datetime
import jwt
from functools import wraps
import app


class AuthHelper:
    
    def __init__(self):
        self.secret_key = "thisismyireportersecretkey"

    def encode_auth_token(self, user):
        
        """Generates the access Token"""     

        payload = jwt.encode({
                
                'sub': user,
                'exp': datetime.datetime.now() + datetime.timedelta(minutes=30)},
                    self.secret_key).decode('utf-8'),
               
        return payload

    
    def decode_token(self,payload):
        
        """Decodes the  token from the Authoriazation header"""

        Token = jwt.decode(payload, self.secret_key, algorithms=['HS256'])
        return Token
        

    
    def token_required(self,f):
        @wraps(f)
        def decorated(*args, **kwargs):
            """This function is the decorator for protecting the routes"""
            
            payload = None
            
            
            if 'Authorization' in request.headers:
                payload = request.headers['Authorization'].split(" ")[1]
                
            if not payload:
                return jsonify({'message':'Token is missing'}), 401
                

            try:
                
                current_user = jwt.decode(payload,self.secret_key)
               
                
            except:
                return jsonify({'message':'Token is invalid'}),401
            return f( current_user,*args,**kwargs)
        return decorated


