from application.network.RemoteClient import RemoteClient
import application.Config
import socket
from threading import Thread

class ChatServer:
    def __init__(self):
        self.m_acceptorSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.m_acceptorSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.m_acceptorSocket.bind((application.Config.SERVER_IP, application.Config.PORT))
        self.m_listenThread = None
        self.m_connectedClients = []
        return

    def acceptorThread(self):
        self.m_acceptorSocket.listen(1)
        while True:
            conn, remoteAddr = self.m_acceptorSocket.accept()
            print "New Connecting from " + str(remoteAddr)
            self.m_connectedClients.append(RemoteClient(conn))
        return

    def startServer(self):
        self.m_listenThread = Thread(target=self.acceptorThread)
        self.m_listenThread.start()
        return

    def stopServer(self):
        return