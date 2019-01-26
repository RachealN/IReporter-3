import unittest
import json
from app import initialize_app
from .test_base import TestBase 
from  app.views import users_view

class AuthTestCase(TestBase):
    """Test case for the Authentication Blueprint."""
    
    def test_register_user(self):
        users = []
        response = self.client.post('/api/v1/auth/register',
        content_type='application/json',
        data=json.dumps(dict(
                self.user
                
        )))
        users.append(dict)
        self.assertEqual(response.status_code,str(response.data))
        self.assertIn("",str(response.data))
        self.assertTrue(len(users),2)
        self.assertNotEqual("user with id is not found",str(response.data))

       
 