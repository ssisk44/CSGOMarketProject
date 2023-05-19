import os
import mysql.connector
from dotenv import load_dotenv

'''Create a mySQLConnection'''
class Connection:
    load_dotenv()

    def __init__(self, database=os.getenv('DB_DATABASE')):
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = database
        self.connection = None

    def connect(self, debug=False):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if debug:
                print("Connected to MySQL database:", self.database)
        except Exception as e:
            print('Exception connecting to database', self.database, ': \n', e)

    def disconnect(self, debug=False):
        if self.connection.is_connected():
            self.connection.close()
            if debug:
                print("Disconnected from MySQL database.")

    def start_transaction(self, debug=False):
        self.connection.start_transaction()
        if debug:
            print("Transaction started.")

    def commit_transaction(self, debug=False):
        self.connection.commit()
        if debug:
            print("Transaction committed.")

    def rollback_transaction(self):
        self.connection.rollback()
        print("Transaction rolled back.")

    def execute_query(self, query, debug=False):
        try:
            if debug:
                print("Query Beginning Execution")
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(e)


    def getDatabaseName(self):
        return self.database

    def setDatabaseName(self, name):
        self.database = name
