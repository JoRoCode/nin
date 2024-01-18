
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import ninja

# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Dojo: 
    
    db = "dojos_and_ninjas_schema" #which database are you using for this project
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas=[]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?


    # Create Users Models        
    @classmethod
    def create_dojo(cls, data):
        query = """INSERT INTO dojos (name, created_at, updated_at) 
        VALUES (%(name)s, NOW(), NOW());"""
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    # Read Users Models
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one_dojo(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {'id': dojo_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

# This will get all ninjas
    @classmethod
    def get_dojo_with_ninjas_by_id(cls, dojo_id): 
        data = {"id": dojo_id}
        query = """
            SELECT * 
            FROM dojos
            LEFT JOIN ninjas 
            ON dojos.id = ninjas.dojo_id
            WHERE id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        dojo = cls(results[0])
        if results[0]["ninja_id"]:
            for data in results:
                ninja_data = {
                    "id": data["ninja_id"],
                    "first_name": data["first_name"],
                    "last_name": data["Last_name"],
                    "age": data["age"],
                    "created_at": data["ninjas.created_at"],
                    "updated_at": data["ninjas.updated_at"]
                                }
                dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    # Update Users Models



    # Delete Users Models