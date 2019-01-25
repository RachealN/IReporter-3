from flask import request,jsonify
from app.models.database import DatabaseConnection
from app.utilities.auth import AuthHelper


con = DatabaseConnection()
created = AuthHelper()

class Incident:
    def __init__(self):
        pass


    def create_incident(self,status, location,image,video, comment):

           
        
            create_incident= "INSERT INTO incidents (status, location,image,video, comment) VALUES ('{}','{}','{}','{}','{}') RETURNING incident_id".format(status,location,image,video,comment)
            
            print(create_incident)
            con.dict_cursor.execute(create_incident,(status,location,image,video,comment))
            return con.dict_cursor.fetchone()

    
            
            

    def update_location(self,location,incident_id):
        update_location = "UPDATE incidents SET location='{}' WHERE incident_id='{}' RETURNING incident_id".format(location,incident_id)
        con.dict_cursor.execute(update_location)
        return con.dict_cursor.fetchone()

    
    def update_comment(self,comment,incident_id):
        update_comment = "UPDATE incidents SET comment='{}' WHERE incident_id='{}' RETURNING incident_id".format(comment,incident_id)
        con.dict_cursor.execute(update_comment)
        return con.dict_cursor.fetchone()

    def update_status(self,status,incident_id):
        update_status = "UPDATE incidents SET status='{}' WHERE incident_id='{}' RETURNING incident_id".format(status,incident_id)
        print(update_status)
        con.dict_cursor.execute(update_status)
        inter = con.dict_cursor.fetchone()

        return inter

    

    def get_all_incidents(self):
        
        get_all = "SELECT * FROM incidents"
        con.dict_cursor.execute(get_all)
        incidents = con.dict_cursor.fetchall()
        return incidents

    def get_single_incident(self, id):
        
        incident_query = "SELECT * FROM incidents WHERE incident_id=%s"
        con.dict_cursor.execute(incident_query, [id])
        incident = con.dict_cursor.fetchone()
        return incident

    def delete_incident(self,incident_id):
        delete_record = "DELETE FROM interventions WHERE incident_id='{0}'".format(incident_id)
        con.cursor.execute(delete_record, (incident_id,))

        
