from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    @classmethod 
    def get_all_from_dojo(cls, id):
        query = f"SELECT * FROM ninjas WHERE dojo_id = {id};"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, created_at, updated_at, dojo_id ) VALUES ( %(fname)s , %(last_name)s , %(age)s , NOW() , NOW() , %(dojo_id)s );"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )