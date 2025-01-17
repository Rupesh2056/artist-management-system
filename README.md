
**Prerequisites:**
   - Python
   - postgresql


## Project Setup:

1. Clone the repo:

    `git clone git@github.com:Rupesh2056/artist-management-system.git`

2. Create virtual environment with venv (or virtualenv if venv is not available)

   `python3 -m venv venv`

3. Activate the virtual environment created

   `source /venve/bin/activate` (for linux)
   `venv\Scripts\activate` (for windows)
   

4. Install dependencies

   `pip install -r requirements.txt`


## Configurations:
1. Create a postgres database
   psql -U <username>
   CREATE DATABASE <database_name>;

2. Create .env file
   a. `cp .env-sample .env`
   b. Make the necessary changes on the .env file for your database connection


3. Create necessary Tables with the management command.

   ```python manage.py create_tables```
  
4. Create directory on project level for session files:

   ```mkdir session_files```

5. Run the server
   `python manage.py runserver`

6. Open browser and navigate to 
   
