from application.lang.Singleton import Singleton
from application.network.encryption.DiffieHellman import DiffieHellman
from application import Config
import socket
import netstruct
from threading import Thread

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
        self.m_handleThread = None
        self.m_packetHandlers = {
            0: self.handleHelloResponse,
            1: self.handleLoginResponse
        }

    def handleHelloResponse(self, data):
        print "Got Hello Response"

    def handleLoginResponse(self, data):
        print "Got Login Response"

    def listenLoop(self):
        print "Listen Loop Begin..."
        while True:
            data = self.m_socket.recv(1024 * 16) # 16KB Recv Buffer
            if self.m_encryptionEnabled:
                print "Encrypted Packet"
                decData = self.m_encryptionModule.decryptData(data)
                (packetID,), restData = netstruct.iter_unpack("i", decData)
                self.m_packetHandlers.get(packetID)(restData)
            else:
                print "Uncrypted Packet"
                (packetID,), restData = netstruct.iter_unpack("i", data)
                self.m_packetHandlers.get(packetID)(restData)

    def connectToServer(self):
        print "Connecting"
        try:
            self.m_socket.connect((self.m_remoteHost, self.m_remotePort))
            print "Connected"
            self.m_handleThread = Thread(target=self.listenLoop)
            self.m_handleThread.start()
            print "Listen Thread Up n' Running"
            return True
        except Exception:
            print "Failed to Connect!"
            return False
