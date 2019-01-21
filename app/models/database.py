import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask,jsonify
import os

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = dict(
                database = 'ireportcorruption',
                user = 'postgres',
                password = 'pstgress'
            )
            self.conn = psycopg2.connect(**self.connection)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            self.dict_cursor = self.conn.cursor(cursor_factory=RealDictCursor)

        except Exception:
            return jsonify({"message": "Cannot connect to database"})

    def create_db_tables(self):
        """
            Create users table
        """
        create_users_table = (
            """CREATE TABLE IF NOT EXISTS
            users(
                id SERIAL PRIMARY KEY NOT NULL,
                firstname VARCHAR(50) NOT NULL,
                lastname VARCHAR(50) NOT NULL,
                email VARCHAR(50) UNIQUE,
                password INTEGER NOT NULL,
                phonenumber INTEGER NOT NULL,
                username VARCHAR(50) NOT NULL,
                registered TIMESTAMPTZ DEFAULT Now(),
                isAdmin VARCHAR(20) DEFAULT False
            );"""
        )
        create_redflags_table = (
            """CREATE TABLE IF NOT EXISTS
            redflags(
                redflag_id SERIAL PRIMARY KEY NOT NULL,
                id INTEGER,
                status VARCHAR(20),
                createdOn TIMESTAMPTZ DEFAULT Now(),
                location VARCHAR(30),
                image VARCHAR(30),
                video VARCHAR(30),
                comment VARCHAR(100),
                FOREIGN KEY (id) REFERENCES users(id) ON UPDATE CASCADE
                );""")

        create_interventions_table = (
            """CREATE TABLE IF NOT EXISTS
           interventions(
                intervention_id SERIAL PRIMARY KEY NOT NULL,
                id INTEGER,
                status VARCHAR(20),
                createdOn TIMESTAMPTZ DEFAULT Now(),
                location VARCHAR(30),
                comment VARCHAR(100),
                FOREIGN KEY (id) REFERENCES users(id) ON UPDATE CASCADE
                );""")


        """
            execute cursor object to create tables
        """
        self.cursor.execute(create_users_table)
        self.cursor.execute(create_redflags_table)
        self.cursor.execute(create_interventions_table)
        
    def drop_table(self, table_name):
        """
            truncate a table
            :param table_name:
        """
        self.cursor.execute(
            "TRUNCATE TABLE {} RESTART IDENTITY CASCADE".format(table_name))

if __name__ == '__main__':
    con = DatabaseConnection()
    con.create_db_tables()

