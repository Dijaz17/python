from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash

class Message:
    def __init__( self , data ):
        self.id = data['id']
        self.message = data['message']
        self.sender_id = data['sender_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO messages ( message, sender_id, created_at, updated_at, users_id ) VALUES ( %(message)s , %(sender_id)s , NOW() , NOW() , %(recipient_id)s );" 
        return MySQLConnection('private_wall_schema').query_db( query, data )

    @classmethod
    def get_messages(cls, users_id):
        query = f"SELECT * FROM messages WHERE users_id = {users_id};"
        results = MySQLConnection('private_wall_schema').query_db(query)
        messages = []
        for message in results:
            messages.append( cls(message) )
        return messages

    @classmethod
    def delete(cls, message_id):
        query = f"DELETE FROM messages WHERE id = {message_id};" 
        return MySQLConnection('private_wall_schema').query_db( query )