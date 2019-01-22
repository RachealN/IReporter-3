import unittest
from  app.views import interventions_view
from .test_base import TestBase  
from app import initialize_app
import json


class TestInterventions(TestBase):
    """This class represents the redflag test case"""

    def test_create_intervention(self):
        pass