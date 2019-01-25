import unittest
import json
from app import initialize_app
from .test_base import TestBase 
from  app.views import users_view

class AuthTestCase(TestBase):
    """Test case for the Authentication Blueprint."""
    
    def test_register_user(self):
        pass
       
 