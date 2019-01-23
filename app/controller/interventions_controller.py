from flask import request,jsonify
from app.models.database import DatabaseConnection
from app.utilities.auth import AuthHelper


con = DatabaseConnection()
created = AuthHelper()

class Intervention:
    def __init__(self):
        pass


    def create_intervention(self,status, location,image,video, comment):

           
        
            create_intervention= "INSERT INTO interventions (createdBy,status, location,image,video, comment) VALUES ('{}','{}','{}','{}','{}','{}') RETURNING intervention_id".format(created.createdby_id(),status,location,image,video,comment)
            
            con.dict_cursor.execute(create_intervention)
            return con.dict_cursor.fetchone()
            
            

    def update_location(self,location,intervention_id):
        update_location = "UPDATE interventions SET location='{}' WHERE intervention_id='{}' RETURNING intervention_id".format(location,intervention_id)
        con.dict_cursor.execute(update_location)
        return con.dict_cursor.fetchone()

    
    def update_comment(self,comment,intervention_id):
        update_comment = "UPDATE interventions SET comment='{}' WHERE intervention_id='{}' RETURNING intervention_id".format(comment,intervention_id)
        con.dict_cursor.execute(update_comment)
        return con.dict_cursor.fetchone()

    def update_status(self,status,intervention_id):
        update_status = "UPDATE interventions SET status='{}' WHERE intervention_id='{}' RETURNING intervention_id".format(status,intervention_id)
        con.dict_cursor.execute(update_status)
        return con.dict_cursor.fetchone()

    

    def get_all_interventions(self):
        
        get_all = "SELECT * FROM interventions"
        con.dict_cursor.execute(get_all)
        interventions = con.dict_cursor.fetchall()
        return interventions

    def get_single_intervention(self, id):
        
        intervention_query = "SELECT * FROM interventions WHERE intervention_id=%s"
        con.dict_cursor.execute(intervention_query, [id])
        intervention = con.dict_cursor.fetchone()
        return intervention

    def delete_intervention(self,intervention_id):
        delete_record = "DELETE FROM interventions WHERE intervention_id='{0}'".format(intervention_id)
        con.cursor.execute(delete_record, (intervention_id,))

        
