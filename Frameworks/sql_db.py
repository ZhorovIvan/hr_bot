# pip install mysql-connector-python
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
import logging
import configparser as cp
from Frameworks.settings import *

class MySQLStorage():

    def __init__(self, config) -> None:
        self.config = config


    def create_connection(self) -> mysql.connector:
        '''
        Get connection
        '''
        try:
            mydb = mysql.connector.connect(
                        host = self.config['MYSQL']['localhost'],
                        port = self.config['MYSQL']['port'],
                        user = self.config['MYSQL']['user_name'],
                        password = self.config['MYSQL']['password'],
                        database = self.config['MYSQL']['db_name']
                    )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.ERROR("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.ERROR("Database does not exist")
            else:
                logging.ERROR(err)           
        return mydb


    def insert(self, data : str) -> bool:      
        '''
        Insetr row to mysql database
        '''
        query = ("INSERT INTO userdata (bio, emp_title, emp_number, emp_email) " +
                    f"VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}')")
        return self.__execute_query(query)


    def __execute_query(self, query : str) -> bool:
        try:
            con = self.create_connection()
            cursor = con.cursor(buffered=True)
            cursor.execute(query)
            con.commit()
            return True
        except:
            return False    
        finally:
            con.close()