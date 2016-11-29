import hashlib
import socket
from threading import Thread

import netstruct
from Crypto.Cipher import AES

from application.login.encryption.NaiveDiffiehellman import NaiveDiffieHellman


class Login:
    def __init__(self, remoteHost, remotePort):
        self.m_encryptionEnabled = True
        self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.m_remoteShared = None
        self.m_localShared = None
        self.m_myDH = NaiveDiffieHellman()
        self.m_mySecret = None
        self.m_encryptionModule = None
        self.m_remoteHost = remoteHost
        self.m_remotePort = remotePort

    def sendPacket(self, data):
        if self.m_encryptionEnabled:
            BS = 32
            self.m_encryptionModule = AES.new(self.mdkey.hexdigest(), AES.MODE_CBC, 'This is an IV456')
            pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
            encData = self.m_encryptionModule.encrypt(pad(data))
            self.m_socket.send(encData)
        else:
            self.m_socket.send(data)

    def handleHelloResponse(self, data):
        print "Remote Shared Key: ", str(data)
        remoteShared = long(data)
        print "Check Shared: ", str(remoteShared)
        mySecret = self.m_myDH.exchange(remoteShared)
        print "Secret: ", mySecret
        shakey = hashlib.sha256(str(mySecret))
        print "Key: ", shakey.hexdigest()
        self.m_localShared = self.m_myDH.shared()
        encPacket = netstruct.pack("i", 2)
        encPacket += str(self.m_localShared)
        print "local shared " + str(self.m_localShared)
        self.sendPacket(encPacket)
        self.m_encryptionEnabled = True
        self.mdkey = hashlib.md5(str(mySecret))
        self.m_encryptionModule = AES.new(self.mdkey.hexdigest(), AES.MODE_CBC, 'This is an IV456')
        print "Client: Enabling Encryption Layer"

    def listenloop(self):
        print "Listen Loop"
        while 1:
            data = self.m_socket.recv(1024)

            handlers = {
                0: self.handleHelloResponse,
                1: self.handleLoginResponse,
                2: None,
                3: None
            }

            if self.m_encryptionEnabled:
                self.m_encryptionModule = AES.new(self.mdkey.hexdigest(), AES.MODE_CBC, 'This is an IV456')
                print "Client: Handling Encrypted Packet"
                BS = 32
                decData = self.m_encryptionModule.decrypt(data)
                unpad = lambda s: s[:-ord(s[len(s) - 1:])]
                (packetID,), restData = netstruct.iter_unpack("i", unpad(decData))
                print "Encrypted Packet ID:", packetID
                handler = handlers.get(packetID)
                handler(restData)
            else:
                print "Client: Handling Uncrypted Packet"
                (packetID,), restData = netstruct.iter_unpack("i", data)
                print "Uncrypted Packet ID:", packetID
                handler = handlers.get(packetID)
                handler(restData)

    def handleLoginResponse(self, data):
        (statusResponse,), restData = netstruct.iter_unpack("i", data)
        if statusResponse == 0:
            self.handleLoginOkay(restData)
        else:
            self.handleLoginError(statusResponse, restData)

    def handleLoginOkay(self, data):
        print "Login Okay"

    def handleLoginError(self, errorCode, data):
        bErrorReason = netstruct.unpack("b$", data)
        errorReason = str(bErrorReason)
        errorEnum = {
            1: "General Error",
            2: "User Error",
            3: "Server Error"
        }
        print "Error: " + errorEnum[errorCode]

    def connect(self):
        print "Connecting..."
        self.m_socket.connect((self.m_remoteHost, self.m_remotePort))
        print "Connected!"
        self.m_handleThread = Thread(target=self.listenloop)
        self.m_handleThread.start()
        print "Message Handler created"

    def login(self, username, password):
        print "Logging in"
        print "User:", username
        print "Password:", password
        data = netstruct.pack("ib$b$", 4, username, password)
        self.sendPacket(data)


def remember(self, username):
    if self.hasCorrectFormat(username):
        print "saving username"
        pass


@staticmethod
def hasCorrectFormat(prefix):
    return len(prefix) > 4
