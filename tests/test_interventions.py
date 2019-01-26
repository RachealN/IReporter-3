import unittest
from  app.views import interventions_view
from .test_base import TestBase  
from app import initialize_app
import json


class TestInterventions(TestBase):
    """This class represents the intervention test case"""

    def test_create_intervention(self):
        """Test API can create intervention (POST request)"""
       
        """Test API can create an intervention(POST request)"""

        
        self.user
        response = self.client.post('/api/v1/auth/register',
        content_type='application/json',
        data=json.dumps(self.user))

    
        self.credential
        
        response = self.client.post('/api/v1/auth/login',
        content_type='application/json',
        data=json.dumps(self.credential))

        token = json.loads(response.data.decode())
        token = token['token']
        
        

        redflags = []
        response = self.client.post('/api/v1/interventions',
        content_type='application/json',headers=dict(Authorization=token),
        data=json.dumps(dict(
            self.redflag
        )))
        
        redflags.append(dict)
        self.assertIn("",str(response.data))
        self.assertTrue(len(redflags),2)
        self.assertNotEqual("intervention not created",str(response.data))
        

    

        
        