import unittest
from  app.views import redflag_view
from app.views import interventions_view
from app import initialize_app
from app.models.database import DatabaseConnection
import json


db = DatabaseConnection() 
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
        
        self.intervention=dict(
            comment = "corruption",
            createdon = "2019-01-24 14:03:32.08278+03",
            image = "https://postimage/image1.jng",
            incidentType = "redflag",
            location = "234334.56443",
            status = "pending",
            createdBy = 1,
            video = "https://postvideo/Video5.jng"
           
            )

        self.interventions_empty = []
        self.interventions=[self.intervention,self.intervention]
        

        self.user = dict(
            firstname = "henry",
            lastname = "john",
            email = "keti@gmail.com",
            username = "tom",
            password = "12345678",
            phonenumber = "0705647463"
           
        ) 
       
        self.users_empty = []
        self.users=[self.user,self.user]

   
        self.credential = dict(
            email = "keti@gmail.com",
            password = "12879578",
        )
        self.credentials_empty = []
        self.credentials=[self.credential,self.credential]

    
        
    def tearDown(self,table_name):
        db.drop_table(incidents)
        

    