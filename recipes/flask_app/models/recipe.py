from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_thirty = data['under_thirty']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes ( name, description, under_thirty, instructions, date_made, created_at, updated_at, user_id ) VALUES ( %(name)s , %(description)s , %(under_thirty)s , %(instructions)s , %(date_made)s , NOW() , NOW() , %(user_id)s );" 
        return MySQLConnection('recipes_schema').query_db( query, data )

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = MySQLConnection('recipes_schema').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, under_thirty = %(under_thirty)s, instructions = %(instructions)s, date_made = %(date_made)s, user_id = %(user_id)s WHERE id = %(id)s" 
        return MySQLConnection('recipes_schema').query_db( query, data )

    @classmethod
    def delete(cls, recipe_id):
        query = f"DELETE FROM recipes WHERE id = {recipe_id};" 
        return MySQLConnection('recipes_schema').query_db( query )

    @staticmethod
    def validate_recipe(data):
        is_valid = True 
        if len(data['name']) < 3 or len(data['name']) > 80:
            flash("Name must be between 3 characters and 80 characters.")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be between at least 3 characters.")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Instructions must be between at least 3 characters.")
            is_valid = False
        return is_valid