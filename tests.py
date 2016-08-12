# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from flask_blog import app, db

from author.models import *
from blog.models import *

class UserTest(unittest.TestCase):
    def setUp(self):
        db_username = app.config['DB_USERNAME']
        db_password = app.config['DB_PASSWORD']
        blog_database_name = 'blog'
        db_host = app.config['DB_HOST']
        self.db_uri = "mysql+pymysql://%s:%s@%s/" % (db_username, db_password, db_host)
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['BLOG_DATABASE_NAME'] = 'test_blog'
        app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri + app.config['BLOG_DATABASE_NAME']
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("CREATE DATABASE " + app.config['BLOG_DATABASE_NAME'])
        db.create_all()
        conn.close()
        self.app = app.test_client()
        
    def tearDown(self):
        db.session.remove()
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("DROP DATABASE " + app.config['BLOG_DATABASE_NAME'])
        conn.close()
        
    def create_blog(self):
        return self.app.post('/setup', data=dict(
            name='My Test Blog',
            fullname='Jorge Escobar',
            email='jorge@fromzero.io',
            username='jorge',
            password='test',
            confirm='test'),
        follow_redirects=True)
        
    def test_create_blog(self):
        rv = self.create_blog()
        assert 'Blog created' in str(rv.data)
        
if __name__ == '__main__':
    unittest.main()
