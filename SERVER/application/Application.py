from application.manager.RoomManager import RoomManager
from application.network.ChatServer import ChatServer
from time import sleep

class Application:
    def __init__(self):
        print "Chat Server Loading"
        self.m_chatServer = None
        return

    def run(self):
        print "Server Starting..."
        RoomManager.Instance().loadRoomsFromDB()
        self.m_chatServer = ChatServer()
        self.m_chatServer.startServer()
        while True:
            sleep(1)
