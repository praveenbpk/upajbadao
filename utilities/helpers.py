import pymysql
from os import environ 
import config
from utilities.errors import *

host = config.db_host
username = config.db_username
password = config.db_password
database_name = config.db_name


def openDbconnection():
	try:
		connection = pymysql.connect(host=host, user=username, passwd=password, db=database_name,port=3306)
		cursor = connection.cursor(pymysql.cursors.DictCursor)
		return connection, cursor
	except Exception as e:
		return str(e)