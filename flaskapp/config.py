import os
from dotenv import load_dotenv
    
class Config:
    load_dotenv()
    #DB CONNECT
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    #ROLLBAR CONNECTION
    WRITE = os.environ.get('WRITE')
    POST_SERVER_ITEM = os.environ.get('POST_SERVER_ITEM')
    POST_CLIENT_ITEM = os.environ.get('POST_CLIENT_ITEM')
    READ = os.environ.get('READ')
     
