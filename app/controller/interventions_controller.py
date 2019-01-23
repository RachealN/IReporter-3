from flask import request,jsonify
from app.models.database import DatabaseConnection


con = DatabaseConnection()

class Intervention:
    def __init__(self):
        pass


    def create_intervention(self, status, location, comment):

           
        
            create_intervention= "INSERT INTO interventions (status, location, comment) VALUES (%s,%s,%s)"
            con.cursor.execute(create_intervention, ( status, location, comment))

    def update_location(self,location):
        update_location = " UPDATE interventions SET location='{}'".format(location)
        con.cursor.execute(update_location)

    
    def update_comment(self,comment):
        update_comment = " UPDATE interventions SET comment='{}'".format(comment)
        con.cursor.execute(update_comment)
