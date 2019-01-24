from flask import request,jsonify
from app.models.database import DatabaseConnection
from app.utilities.auth import AuthHelper


db = DatabaseConnection()
createdby = AuthHelper()

class Redflag:
    def __init__(self):
        pass


    def create_redflag(self,status, location,image,video, comment):

           
        
            create_redflag= "INSERT INTO redflags (status, location,image,video, comment) VALUES ('{}','{}','{}','{}','{}') RETURNING redflag_id".format(status,location,image,video,comment)
            
            db.dict_cursor.execute(create_redflag,(status,location,image,video,comment))
            return db.dict_cursor.fetchone()

    def get_single_redflag(self, id):
        redflag_query = "SELECT * FROM redflags WHERE redflag_id=%s"
        db.dict_cursor.execute(redflag_query, [id])
        redflag = db.dict_cursor.fetchone()
        return redflag

    def patch_redflag_status(self,status,user_id):
        update_status = "UPDATE redflags SET status='{}' WHERE redflag_id='{}' RETURNING redflag_id".format(status,user_id)
        db.dict_cursor.execute(update_status)
        return db.dict_cursor.fetchone()

    def get_all_redflags(self):
        
        get_all = "SELECT * FROM redflags"
        db.dict_cursor.execute(get_all)
        redflags = db.dict_cursor.fetchall()
        return redflags

    def delete_redflag(self,redflag_id):
        delete_redflag = "DELETE FROM redflags WHERE redflag_id='{0}'".format(redflag_id)
        db.cursor.execute(delete_redflag, (redflag_id,))
