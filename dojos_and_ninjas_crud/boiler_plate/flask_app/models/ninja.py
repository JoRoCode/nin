
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Ninja:
    db = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.all_ninjas = []
        self.dojo_id = ['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?



    #     # Create Users Models
    @classmethod
    def create_ninja(cls, data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"""
        print(query)
        return connectToMySQL(cls.db).query_db(query, data)
    
    # Read Users Models
    @classmethod
    def get_one_ninja(cls, ninja_id):
        data = {'id': ninja_id}
        query = """SELECT * 
                FROM ninjas 
                WHERE id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        print(cls(results[0]))
        return cls(results[0])



    # Update Users Models

    @classmethod
    def edit_ninja(cls, ninja_id):
        data = {'id': ninja_id}
        query = """
            SELECT * 
            FROM ninjas
            WHERE ninja_id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results[0])
        return results[0]    

    @classmethod
    def update_ninja_info(cls, data):
        query = """
            UPDATE ninjas
            SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s
            WHERE ninja_id = %(ninja_id)s;"""
        print(query)
        return connectToMySQL(cls.db).query_db(query,data)
        
    # Delete Users Models
    
    @classmethod
    def delete_ninja(cls,ninja_id):
        query = """
            DELETE FROM ninjas
            WHERE ninja_id = %(ninja_id)s;"""
        data = {"ninja_id": ninja_id}
        return connectToMySQL(cls.db).query_db(query, data)