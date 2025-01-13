from psycopg2 import sql
from django.contrib.auth.hashers import make_password,check_password
from user.models import User
from django.db import connection

def get_user(email):
        return User.get_from_db(email=email)

def authenticate(email,password):
        user = get_user(email)
        if user:       
                if check_password(password,user.password):
                        return user
        

        