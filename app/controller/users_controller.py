from flask import request, jsonify,make_response, json
from app.models.database import DatabaseConnection



con = DatabaseConnection()

class User:
    
    def register_user(self,firstname,lastname,email,password,phonenumber,username):
        """This Function registers a user"""

        reg_user = "INSERT INTO users (firstname,lastname,email,password,phonenumber,username)\
                                         VALUES (%s,%s,%s,%s,%s,%s)"
        con.cursor.execute(reg_user, (firstname,lastname,email,password,phonenumber,username))
       
    def check_user_by_username(self,username):

        """ Function to get_user_by_username"""

        check_for_unique_username = "SELECT id,username,isAdmin\
                                 FROM users WHERE username = %s"
        con.cursor.execute(check_for_unique_username, (username,))
        row = con.cursor.fetchone()
        return row

    def check_user_by_email(self,email):

        """ Function to get_user_by_email"""

        check_for_unique_email = "SELECT id,firstname,lastname,email,password,phonenumber,username\
                                 FROM users WHERE email = %s"
        con.cursor.execute(check_for_unique_email, (email,))
        row = con.cursor.fetchone()
        return row

    def login(self,email):

        """This function logins in a user"""

        check_unique_email = "SELECT email WHERE username =%s"
        con.cursor.execute(check_unique_email,(email))
        row = con.cursor.fetchone()
        return row

