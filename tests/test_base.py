import unittest
from  app.views import redflag_view
from app.views import interventions_view
from app import initialize_app
import json


class TestBase(unittest.TestCase):
    
    def setUp(self):
        """Define test variables and initialize app."""

        self.app = initialize_app()
        self.client = self.app.test_client(self)
        
    def tearDown(self):
        pass
    #    self.redflags.clear()
    #    self.users.clear()
    #    self.interventions.clear()


    