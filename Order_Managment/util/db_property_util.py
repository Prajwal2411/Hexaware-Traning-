import configparser
import os

class DBPropertyUtil:
    @staticmethod
    def get_connection_string(property_file="db.properties"):
        config = configparser.ConfigParser()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        absolute_path = os.path.join(base_dir, "..", property_file)
        read_files = config.read(absolute_path)
        if not read_files:
            raise FileNotFoundError(f"Could not find the property file: {absolute_path}")

        host = config.get("database", "host")
        database = config.get("database", "database")
        driver = config.get("database", "driver")
        authentication = config.get("database", "authentication")

        if authentication.lower() == "windows":
            return f"DRIVER={{{driver}}};SERVER={host};DATABASE={database};Trusted_Connection=yes;"
        else:
            raise ValueError("Unsupported authentication method. Only 'windows' is supported.")
