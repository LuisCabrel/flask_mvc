#from _mysql_connector import MySQL

from application import app
# sfrom flask_mysqldb import MySQL
#import pymysql
import mysql.connector
from flask_mysqldb import MySQL



class Database:
    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'tuto_video'
    mysql = MySQL(app)

    def __init__(self):
        pass

    def get_connection(self):
        return self.mysql
