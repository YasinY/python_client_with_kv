from application.lang.Singleton import Singleton
import sqlite3

@Singleton
class DatabaseConnector:
    def __init__(self):
        print "Connecting to server.db"
        self.m_db = sqlite3.connect("server.db", check_same_thread=False)
        print "Connected"
        return

    def executeQuery(self, query):
        return self.m_db.execute(query)

    def getConnector(self):
        return self.m_db