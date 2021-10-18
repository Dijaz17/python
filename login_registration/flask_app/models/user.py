from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
import re

email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s , NOW() , NOW() );" 
        return MySQLConnection('login_registration_schema').query_db( query, data )

    @classmethod
    def get_indiv_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s ;'
        results = MySQLConnection('login_registration_schema').query_db( query, data )
        users = []
        for user in results:
            users.append( User(user) )
        return users

    @staticmethod
    def validate_registration(data):
        is_valid = True 
        if len(data['first_name']) < 2 or len(data['first_name']) > 45 or not data['first_name'].isalpha():
            flash("First name must be between 2 characters and 45 characters with alphabetical letters only.")
            is_valid = False
        if len(data['last_name']) < 2 or len(data['last_name']) > 45 or not data['last_name'].isalpha():
            flash("Last name must be between 2 characters and 45 characters with alphabetical letters only.")
            is_valid = False
        if not email_re.match(data['email']) or len(data['email']) > 90: 
            flash("Email must be in valid email format.")
            is_valid = False
        if len(User.get_indiv_by_email(data)) > 0:
            flash("Email already in use.")
            is_valid = False
        if len(data['password']) < 8 or len(data['password']) > 45:
            flash("Password must be between 8 characters and 45 characters long.")
            is_valid = False
        if data['pass_conf'] != data['password']:
            flash("Confirm password must be the same as password.")
            is_valid = False
        return is_valid

    