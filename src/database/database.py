import sqlite3

class Database:

    DB_NAME = "super_pug.db"

    @staticmethod
    def connect():
        return sqlite3.connect(Database.DB_NAME)