from django.core.management.base import BaseCommand, CommandError

from database.operations import execute_create_table_query



class Command(BaseCommand):
    """
    Assigns UserPoint with its respectiver customer.
    python manage.py assign_customer
    """
    help = "Assigns UserPoint with its respectiver customer."

    def handle(self, **options):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS "User" (
                id SERIAL PRIMARY KEY, 
                full_name VARCHAR(225) NOT NULL, 
                email VARCHAR(255), 
                address VARCHAR(255), 
                phone VARCHAR(20), 
                dob DATE, 
                gender gender_enum, 
                password VARCHAR(225) NOT NULL, 
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """

        execute_create_table_query(create_table_query)
        print("tables created.")

            

        
