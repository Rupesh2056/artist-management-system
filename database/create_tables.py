# from database.db import DbConnection
# import psycopg2

# with DbConnection() as conn:
#     cur = conn.cursor()
#     try:

#         # Create table with the specified fields
#         create_table_query = """
#         CREATE TABLE IF NOT EXISTS "User" (
#             id SERIAL PRIMARY KEY, 
#             full_name VARCHAR(225) NOT NULL, 
#             email VARCHAR(255), 
#             address VARCHAR(255), 
#             phone VARCHAR(20), 
#             dob DATE, 
#             gender gender_enum, 
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
#             updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         );
#         """
        
#         # Execute the query to create the table
#         cur.execute(create_table_query)
        
#         # Commit the transaction
#         conn.commit()

#         print("Table 'User' created successfully!")

#     except psycopg2.Error as e:
#         print(f"Error: {e}")
#         conn.rollback()
#         # cur.execute("CREATE TABLE user (id serial PRIMARY KEY, num integer, data varchar);")

# from .operations import execute_create_table_query


from .operations import execute_create_table_query

def main():
    
 

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


if __name__ == '__main__':
    main()