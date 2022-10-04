from peewee import *
from Frameworks.settings import *

config = read_config()

mysql_db = MySQLDatabase(config['MYSQL']['db_name'], 
                        user=config['MYSQL']['user_name'], 
                        password=config['MYSQL']['password'],
                        host=config['MYSQL']['localhost'], 
                        port=int(config['MYSQL']['port']))

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        
        database = mysql_db