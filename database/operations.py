

user_select_fields = ""

# class DbConnection:
#     def __enter__(self):
#          # Connect to your PostgreSQL database
#         self.connection = psycopg2.connect(
#             dbname="cloco", 
#             user="postgres", 
#             password="postgres", 
#             host="localhost",   # Use 'localhost' if running locally or the IP of the remote server
#             port="5432"         # Default PostgreSQL port
#         )

#         # Create a cursor object to interact with the database
#         # self.cur = conn.cursor()

#         # Check if the connection is successful
#         print("Connected to the database!")
        

#         return self.connection

#         # Close the cursor and connection when done
#         # cur.close()
#         # conn.close()
#         # print("connection closed")

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         self.connection.close()
#         print("connection closed.")

from django.db import connection
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
# django.setup()

def execute_select_query(query,filters=None):
        with connection.cursor() as cursor:
                cursor.execute(query) if not filters else cursor.execute(query,filters)
                rows = cursor.fetchall()
        return rows

def execute_select_first_query(query,filters=None):
        with connection.cursor() as cursor:
                cursor.execute(query) if not filters else cursor.execute(query,filters)
                row = cursor.fetchone()
        return row

def execute_insert_query(query,values):
        with connection.cursor() as cursor:
                cursor.execute(query,values)


def execute_create_table_query(query):
        with connection.cursor() as cursor:
                cursor.execute(query)
                # conn.commit()

def execute_create_enum_query(query):
       with connection.cursor() as cursor:
                cursor.execute(query)

def check_if_exists(query,values):
        with connection.cursor() as cursor:
                cursor.execute (query,values)
                return cursor.fetchone()[0]
        


                        

