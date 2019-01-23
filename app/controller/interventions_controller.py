from flask import request,jsonify
from app.models.database import DatabaseConnection


con = DatabaseConnection()

class Intervention:
    def __init__(self):
        pass


    def create_intervention(self, status, location, comment):

           
        
            create_intervention= "INSERT INTO interventions (status, location, comment) VALUES ('{}','{}','{}') RETURNING id".format(status,location,comment)
            con.cursor.execute(create_intervention, ( status, location, comment))
            

    def update_location(self,location):
        update_location = " UPDATE interventions SET location='{}'".format(location)
        con.cursor.execute(update_location)

    
    def update_comment(self,comment):
        update_comment = " UPDATE interventions SET comment='{}'".format(comment)
        con.cursor.execute(update_comment)

    def update_status(self,status,intervention_id):
        update_status = "UPDATE interventions SET status='{}' WHERE intervention_id='{}' RETURNING intervention_id".format(status,intervention_id)
        con.cursor.execute(update_status)
        return con.cursor.fetchone()

    

    def get_all_interventions(self):
        
        get_all = "SELECT * FROM interventions"
        con.dict_cursor.execute(get_all)
        interventions = con.dict_cursor.fetchall()
        return interventions

    def get_single_intervention(self, id):
        
        intervention_query = "SELECT * FROM interventions WHERE id=%s"
        con.dict_cursor.execute(intervention_query, (id,))
        intervention = con.dict_cursor.fetchone()
        return intervention

