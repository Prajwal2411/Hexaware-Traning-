# util/db_property_util.py
import configparser
import os

class DBPropertyUtil:
    @staticmethod
    def get_connection_string(property_file="db.properties"):
        # Get the absolute path to the properties file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        absolute_path = os.path.join(base_dir, "..", property_file)

        # Load the properties file
        config = configparser.ConfigParser()
        read_files = config.read(absolute_path)

        # Check if the file was found and loaded
        if not read_files:
            raise FileNotFoundError(f"Could not find the property file: {absolute_path}")

        if 'database' not in config:
            raise configparser.NoSectionError('database')

        # Extract the connection details
        host = config.get("database", "host")
        database = config.get("database", "database")
        driver = config.get("database", "driver")
        authentication = config.get("database", "authentication")

        # Construct and return the connection string
        if authentication.lower() == "windows":
            return f"DRIVER={{{driver}}};SERVER={host};DATABASE={database};Trusted_Connection=yes;"
        else:
            raise ValueError("Unsupported authentication method. Only 'windows' is supported.")
