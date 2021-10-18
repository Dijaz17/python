from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def get_indiv(cls, id):
        query = f"SELECT * FROM users WHERE id = {id};"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def update(cls, data, id):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(last_name)s, email=%(email)s " + f"WHERE id={id};"
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def destroy(cls, id):
        query = f"DELETE FROM users WHERE id={id};"
        return connectToMySQL('users_schema').query_db( query )
    