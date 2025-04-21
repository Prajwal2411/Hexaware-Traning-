# util/db_conn_util.py
import pyodbc
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection(property_file="db.properties"):
        connection_string = DBPropertyUtil.get_connection_string(property_file)
        return pyodbc.connect(connection_string)
