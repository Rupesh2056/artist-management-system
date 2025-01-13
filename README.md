##Project Setup:

1. Clone the repo:
    `git clone git@github.com:Rupesh2056/artist-management-system.git`
2. Create virtual environment
   `python3 -m venv venv`
3. Activate the virtual environment created
   `source \venve\bin\activate`
4. Install dependencies
   `pip install -r requirements.txt`


##Configurations:
1. Create a postgres database database 
2. Create .env file
   a. `cp .env-sample .env`
   b. Make the necessary changes on the .env file for your database connection

3. Run the server
   `python manage.py runserver`
   
4. Create necessary Tables with the management command.
   `python manage.py create_tables` 
 