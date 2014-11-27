import psycopg2
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tdvtpvxbzvxrqc:GpTck_d1IKA2tv3lu-7JZEMR0F@ec2-54-197-241-82.compute-1.amazonaws.com/dakr17pq1c5236'

# Create database connection object
db = SQLAlchemy(app)


class ConnectionFactory:


    def create(self):

        host = "host = 'ec2-54-197-241-82.compute-1.amazonaws.com'" 
        dbname = "dbname = 'dakr17pq1c5236'" 
        user = "user = 'tdvtpvxbzvxrqc'" 
        password = "password = 'GpTck_d1IKA2tv3lu-7JZEMR0F'"

        conn_string = " ".join([host, dbname, user, password])
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute('SELECT version()')          
        ver = cursor.fetchone()
	conn.close()

        return ver

