from django.core.management.base import BaseCommand

from database.operations import execute_create_table_query,execute_create_enum_query


class Command(BaseCommand):
    """
    Creates All required Enums and Tables
    """
    help = "Creates All required Enums and Tables"

    def handle(self, **options):
        enums = {
            "gender_enum" : ('m','f','o'),
            "user_type_enum" : ('admin','artist_manager','artist'),
            "genre_enum" : ('rnb','classic','country','rock','jazz','funk','metal'),
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
 
        create_user_table_query = """
            CREATE TABLE IF NOT EXISTS user_user (
                id SERIAL PRIMARY KEY, 
                full_name VARCHAR(225) NOT NULL , 
                email VARCHAR(255) NOT NULL UNIQUE, 
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
        
        create_artist_table_query = '''
                CREATE TABLE IF NOT EXISTS music_artist (
                    id SERIAL PRIMARY KEY,
                    user_id INT UNIQUE  REFERENCES user_user(id) ON DELETE CASCADE,
                    artist_manager_id INT REFERENCES user_user(id) ON DELETE CASCADE,
                    first_album_release_year int,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

                );
                '''
        
        create_album_table_query = '''
                CREATE TABLE IF NOT EXISTS music_album (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(225) NOT NULL , 
                    artist_id int REFERENCES music_artist(id) ON DELETE CASCADE,
                    release_date DATE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    
                );
                '''
        
        create_music_table_query = '''
                CREATE TABLE IF NOT EXISTS music_music (
                    id SERIAL PRIMARY KEY,
                    album_id int REFERENCES music_album(id) ON DELETE CASCADE,
                    title VARCHAR(225) NOT NULL , 
                    genre genre_enum,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    
                );
                '''

        execute_create_table_query(create_user_table_query)
        execute_create_table_query(create_artist_table_query)
        execute_create_table_query(create_album_table_query)
        execute_create_table_query(create_music_table_query)
        print("tables created.")

            

        
