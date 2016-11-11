import os

SECRET_KEY = 'dylan is a bitch'
DEBUG = True

# SQL DB Settings
DB_USERNAME = 'onarru'
DB_PASSWORD = ''
BLOG_DB_NAME = 'blog'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (
    DB_USERNAME, 
    DB_PASSWORD, 
    DB_HOST, 
    BLOG_DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True