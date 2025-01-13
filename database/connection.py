'''
Unused Context manager for db connection
'''
# import psycopg2
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