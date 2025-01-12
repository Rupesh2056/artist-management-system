from psycopg2 import sql
from django.contrib.auth.hashers import make_password,check_password
from user.models import User
from django.db import connection

def authenticate(email,password):
        query = sql.SQL("""
            SELECT *
            FROM "User"
            WHERE email = %s
                """)
        
        with connection.cursor() as cursor:
                cursor.execute (query,(email,))
                result = cursor.fetchone()
                if result:
                        result = result[1:]
                        fields = User.get_fields()
                        data = {}
                        for index,field in enumerate(fields):
                                if result[index]:
                                        data[field] = result[index] 
                        user = User(**data)
                        hashed_password =user.password
                        if check_password(password,hashed_password):
                                return user
                return None
        
def get_user(email):
        query = sql.SQL("""
            SELECT *
            FROM "User"
            WHERE email = %s
                """)
        
        with connection.cursor() as cursor:
                cursor.execute (query,(email,))
                result = cursor.fetchone()
                if result:
                        result = result[1:]
                        fields = User.get_fields()
                        data = {}
                        for index,field in enumerate(fields):
                                if result[index]:
                                        data[field] = result[index] 
                        user = User(**data)
                        return user
                return None