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

        self.redflag=dict(
            comment = "corruption",
            createdon = "2019-01-24 14:03:32.08278+03",
            image = "https://postimage/image1.jng",
            incidentType = "redflag",
            location = "234334.56443",
            status = "pending",
            createdBy = 1,
            video = "https://postvideo/Video5.jng"
           
            )

        self.redflags_empty = []
        self.redflags=[self.redflag,self.redflag]
        

        self.user = dict(
            firstname = "okello",
            lastname = "opio",
            othernames = "heloo",
            email = "odetah@gmail.com",
            username = "Ahabwe",
            password = "123588856",
            phonenumber = "0786576572",
            isAdmin = "False"
        )  
        self.users_empty = []
        self.users=[self.user,self.user]

   
        self.credential = dict(
            email = "odetah@gmail.com",
            password = "123588856",
        )
        self.credentials_empty = []
        self.credentials=[self.credential,self.credential]

    
        
    def tearDown(self):
        pass
    #    self.redflags.clear()
    #    self.users.clear()
    #    self.interventions.clear()


    