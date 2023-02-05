from sqlalchemy import create_engine

# Configuration variables for the database
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'comp208'
USERNAME = 'root'
PASSWORD = 'SXc2002627SXc'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI