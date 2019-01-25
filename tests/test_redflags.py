import unittest
from  app.views import redflag_view
from .test_base import TestBase  
from app import initialize_app
import json



class TestRedFlag(TestBase):
    """This class represents the redflag test case"""

    def test_index(self):
        response = self.client.get('/api/v1/')
        data = response.data.decode()
        message ={"message": "Welcome to I-Reporter", "status": 200}
        self.assertEqual(json.loads(data), message)

    def test_created_redflag(self):
        """Test API can create a redflag(POST request)"""

        pass

        
       
    