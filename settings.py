import os

SECRET_KEY = '\xf6\x04n\xb9\x1c,\x8e4\xf8\xac\xb2\n\xa3\x0c\x9dP\xa43p\xa7Z\x0ci3'
DEBUG = True

DB_USERNAME = 'bloguser'
DB_PASSWORD = ''
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_IMAGES_DEST = '/var/www/flask-projects/BlogProject/flask_blog/static/images'
UPLOADED_IMAGES_URL = '/static/images/'
