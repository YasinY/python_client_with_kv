from application.lang.Singleton import Singleton
from application.network.encryption.DiffieHellman import DiffieHellman
from application import Config
import socket

@Singleton
class NetworkInterface:
    def __init__(self):
        self.m_encryptionEnabled = False
        self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.m_remoteShared = None
        self.m_localShared = None
        self.m_DHModule = DiffieHellman()
        self.m_localSecret = None
        self.m_encryptionModule = None
        self.m_remoteHost = Config.SERVER_IP
        self.m_remotePort = Config.PORT

    def connectToServer(self):
        print "Connecting"
        try:
            self.m_socket.connect((self.m_remoteHost, self.m_remotePort))
            print "Connected"
            return True
        except Exception:
            print "Failed to Connect!"
            return False
