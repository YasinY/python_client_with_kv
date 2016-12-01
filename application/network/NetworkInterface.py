from application.lang.Singleton import Singleton
from application.network.encryption.DiffieHellman import DiffieHellman
from application.network.encryption.EncyptionModule import EncryptionModule
from application import Config
import socket
import netstruct
from threading import Thread
import hashlib

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
        self.m_MD5Key = None
        self.m_loginCallback = None
        self.m_roomAddCallback = None
        self.m_packetHandlers = {
            0: self.handleHelloResponse,
            1: self.handleLoginResponse,
            2: self.handleRoomAdd,
            3: self.handleRoomMessage
        }

    def handleRoomMessage(self, data):


    def handleRoomAdd(self, data):
        (roomid, roomtype, usercount, roomname) = netstruct.unpack("b$iib$", data)
        self.m_roomAddCallback(roomid, roomtype, usercount, roomname)
        print "ID: " + roomid
        print "Type: " + str(roomtype)
        print "Users: " + str(usercount)
        print "Name: " + roomname

    def requestRoomList(self, roomAddCallback):
        self.m_roomAddCallback = roomAddCallback;
        self.sendPacket(5, "")

    def sendPacket(self, packetID, data):
        packetData = netstruct.pack("i", packetID)
        packetData += data
        if self.m_encryptionEnabled:
            print "Sending Encrypted Packet"
            encData = self.m_encryptionModule.encryptData(packetData)
            self.m_socket.send(encData)
        else:
            print "Sending Plain Packet"
            self.m_socket.send(packetData)

    def handleHelloResponse(self, data):
        print "Got Hello Response"
        print "Remote Shared Key: ", str(data)
        self.m_remoteShared = long(data)
        self.m_localSecret = self.m_DHModule.exchange(self.m_remoteShared)
        self.m_localShared = self.m_DHModule.shared()
        self.sendPacket(2, str(self.m_localShared))
        self.m_encryptionEnabled = True
        self.m_MD5Key = hashlib.md5(str(self.m_localSecret))
        self.m_encryptionModule = EncryptionModule(self.m_MD5Key.hexdigest())
        print "Enabling Local Encryption Layer"

    def handleLoginOkay(self, data):
        print "Login Okay"
        self.m_loginCallback(True, data)
        return

    def handleLoginError(self, status, data):
        print "Login Error"
        self.m_loginCallback(False, data)
        return

    def handleLoginResponse(self, data):
        print "Got Login Response"
        (statusResponse,), restData = netstruct.iter_unpack("i", data)
        if statusResponse == 0:
            self.handleLoginOkay(restData)
        else:
            self.handleLoginError(statusResponse, restData)

    def login(self, username, password, callback):
        self.m_loginCallback = callback
        data = netstruct.pack("b$b$", username, password)
        self.sendPacket(4, data)

    def joinRoom(self, roomid, password, callback):
        data = netstruct.pack("b$b$", roomid, password)
        self.sendPacket(6, data)

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
