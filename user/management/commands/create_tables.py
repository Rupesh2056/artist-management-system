from django.core.management.base import BaseCommand, CommandError

from database.operations import execute_create_table_query,execute_create_enum_query
import psycopg2


class Command(BaseCommand):
    """
    Creates All required Enums and Tables
    """
    help = "Creates All required Enums and Tables"

    def handle(self, **options):
        enums = {
            "gender_enum" : ('m','f','o'),
            "user_type_enum" : ('admin','artist_manager','artist'),
        }
        for name,values in enums.items():
            query = f"""
                    DO $$
                    BEGIN
                        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = '{name}') THEN
                            CREATE TYPE {name} AS ENUM {values};
                        END IF;
                    END $$;
                """

            execute_create_enum_query(query)
 
        create_table_query = """
            CREATE TABLE IF NOT EXISTS "User" (
                id SERIAL PRIMARY KEY, 
                full_name VARCHAR(225) NOT NULL, 
                email VARCHAR(255), 
                address VARCHAR(255), 
                phone VARCHAR(20), 
                dob DATE, 
                gender gender_enum, 
                user_type user_type_enum,
                password VARCHAR(225) NOT NULL, 
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """

        execute_create_table_query(create_table_query)
        print("tables created.")

            

        
