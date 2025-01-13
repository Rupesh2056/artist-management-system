import os
from django.db import connection
# import django
from typing import Any


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
# django.setup()

def execute_select_query(query,filters=None) -> list[tuple]:
        '''
        Executes Database query and returns List of tuples.
        '''
        with connection.cursor() as cursor:
                cursor.execute(query) if not filters else cursor.execute(query,filters)
                rows = cursor.fetchall()
        return rows

def execute_select_first_query(query,filters=None) -> tuple:
        with connection.cursor() as cursor:
                cursor.execute(query) if not filters else cursor.execute(query,filters)
                row = cursor.fetchone()
        return row

def execute_insert_query(query,values) -> None:
        ''''
        Executes Insert query to database.
        '''
        with connection.cursor() as cursor:
                cursor.execute(query,values)


def execute_create_table_query(query) -> None:
        ''''
        Executes Create Table query to database.
        '''
        with connection.cursor() as cursor:
                cursor.execute(query)


def execute_create_enum_query(query) -> None:
       ''''
        Executes Create Enum query to database.
        '''
       with connection.cursor() as cursor:
                cursor.execute(query)

def check_if_exists(query,values) -> Any:
        '''
        Returns either Tuple or None
        '''
        with connection.cursor() as cursor:
                cursor.execute (query,values)
                return cursor.fetchone()[0]
        

def execute_db_query(query,filters) -> None:
        with connection.cursor() as cursor:
                cursor.execute(query) if not filters else cursor.execute(query,filters)





                        

