from threading import Thread
from application.network.encryption.DiffieHellman import DiffieHellman
from application.network.encryption.EncryptionModule import EncryptionModule
from application.database.DatabaseConnector import DatabaseConnector
from application.manager.RoomManager import RoomManager
from application.network.ChatMessage import ChatMessage
import netstruct
import hashlib
import bcrypt
from construct import *

class RemoteClient:
    def __init__(self, socketConnection):
        self.m_clientSocket = socketConnection
        self.m_clientID = 0
        self.m_clientNick = "Empty"
        self.m_handleThread = None
        self.m_handleThread = Thread(target=self.listenLoop)
        self.m_handleThread.start()
        self.m_DHModule = DiffieHellman()
        self.m_encryptionEnabled = False
        self.m_encryptionModule = None
        self.m_DHShared = self.m_DHModule.shared()
        self.m_remoteShared = None
        self.m_secret = None
        self.m_MD5Key = None
        self.m_packetHandlers = {
            0: self.handleHello,
            1: self.handleAuth,
            2: self.handleEncryption,
            3: self.handleRoomMessage,
            4: self.handleLogin,
            5: self.handleRoomListRequest,
            6: self.handleJoinRoomRequest,
            7: self.handleRegister
        }

        self.m_lengthdString = Struct(
            "length" / Int32ub,
            "data" / String(this.length, encoding="utf8"),
        )

        self.sendHelloPacket()  # Initiate Key Exchange

    def getUserID(self):
        return self.m_clientNick

    def handleRoomMessage(self, data):
        (roomid, ), restData = netstruct.iter_unpack("b$", data)

        messageData = self.m_lengthdString.parse(restData)

        room = RoomManager.Instance().getRoomByID(roomid)
        room.broadcastRoomMessage(ChatMessage(self, roomid, messageData.data))

    def handleJoinRoomRequest(self, data):
        (roomid, password) = netstruct.unpack("b$b$", data)
        print "User Joining Room " + roomid
        room = RoomManager.Instance().getRoomByID(roomid)
        if room:
            room.joinRoom(self)
            print "User Joined Room " + room.getRoomName()

    def broadcastMessage(self, message):
        msgData = netstruct.pack("b$b$b$", message.getRoomID(), message.getMessageID(), message.getOwnerID())
        content = message.getMessage()
        msgData += self.m_lengthdString.build(dict(length=len(content), data=content, ))
        self.sendPacket(3, msgData)
        return

    def handleRoomListRequest(self, data):
        print "Got Room List Request"
        for room in RoomManager.Instance().getAllRooms():
            roomPacket = netstruct.pack("b$iib$", room.getRoomID(), 0, 1337, room.getRoomName())
            self.sendPacket(2, roomPacket)

    def handleHello(self, data):
        (bClientNick) = netstruct.unpack("b$", data)
        self.m_clientNick = bClientNick[0]

        print "Hello from '" + self.m_clientNick + "'"
        return

    def handleAuth(self, data):
        print "HANDLER: handleAuth"
        return

    def handleEncryption(self, data):
        print "HANDLER: handleEncryption"
        self.m_remoteShared = long(data)
        self.m_secret = self.m_DHModule.exchange(self.m_remoteShared)
        self.m_MD5Key = hashlib.md5(str(self.m_secret))
        self.m_encryptionModule = EncryptionModule(self.m_MD5Key.hexdigest())
        self.m_encryptionEnabled = True
        print "Server: Enabling Encryption Layer"
        return

    def handleRegister(self, data):
        (dUsername, dPassword) = netstruct.unpack("b$b$", data)
        username = str(dUsername)
        password = str(dPassword)

        print "Login:", username
        print "Passwort:", password

        userExists = False

        for userrow in DatabaseConnector.Instance().getConnector().execute("SELECT * FROM chat_users WHERE username=?",
                                                                           (username.lower(),)):
            userExists = True

        if userExists:
            responseData = netstruct.pack("ib$", 3, "Username already Exists")
            self.sendPacket(1, responseData)
            return

        pwhash = bcrypt.hashpw(password, bcrypt.gensalt())
        DatabaseConnector.Instance().getConnector().execute("INSERT INTO chat_users (id, username, password, ismod, isadmin, lastlogin, lastip, banned, banreason, banliftdate) VALUES(NULL, ?, ?, 0, 0, NULL, '0.0.0.0', 0, '', 0) ", (username.lower(), pwhash, ))
        DatabaseConnector.Instance().writeDB()
        self.m_clientNick = username
        responseData = netstruct.pack("ib$", 0, "")
        self.sendPacket(1, responseData)

    def handleLogin(self, data):
        (dUsername, dPassword) = netstruct.unpack("b$b$", data)
        username = str(dUsername)
        password = str(dPassword)

        print "Login:", username
        print "Passwort:", password

        loginValid = False

        errorCode = 0
        errorReason = ""
        userIsBanned = 0
        banReason = ""
        banLift = -1

        for userrow in DatabaseConnector.Instance().getConnector().execute("SELECT * FROM chat_users WHERE username=?",
                                                                           (username.lower(),)):
            if bcrypt.checkpw(password.encode('utf-8'), userrow[2].encode('utf-8')):
                loginValid = True
                userIsBanned = userrow[7]
                banReason = userrow[8]
                banLift = userrow[9]

        if loginValid:
            print "Login is Valid"
            if userIsBanned != 0:
                errorCode = 2
                errorReason = "Banned: " + str(banReason)
                print "User is Banned!"
        else:
            print "Login is Invalid"
            errorCode = 1
            errorReason = "Username/Password Invalid"

        self.m_clientNick = username
        responseData = netstruct.pack("ib$", errorCode, errorReason)
        self.sendPacket(1, responseData)

    def listenLoop(self):
        while True:
            try:

                data = self.m_clientSocket.recv(1024 * 16)  # 16KB Buffer
                if len(data) == 0:
                    print "Client Disconnected"
                    return

                if self.m_encryptionEnabled:
                    print "Encrypted Packet"
                    decData = self.m_encryptionModule.decryptData(data)
                    (packetID,), restData = netstruct.iter_unpack("i", decData)
                    print "PacketID: " + str(packetID)
                    self.m_packetHandlers.get(packetID)(restData)
                else:
                    print "Uncrypted Packet"
                    (packetID,), restData = netstruct.iter_unpack("i", data)
                    print "PacketID: " + str(packetID)
                    self.m_packetHandlers.get(packetID)(restData)
            except Exception:
                RoomManager.Instance().removeUserFromAllRooms(self)
                print "Disconnected due to Error in Handling"
                return

    def sendPacket(self, packetID, data):
        try:
            packetData = netstruct.pack("i", packetID)
            packetData += data
            if self.m_encryptionEnabled:
                encData = self.m_encryptionModule.encryptData(packetData)
                self.m_clientSocket.send(encData)
            else:
                self.m_clientSocket.send(packetData)
        except Exception:
            RoomManager.Instance().removeUserFromAllRooms(self)
            print "Send Packet Failed"
            return

    def sendHelloPacket(self):
        self.sendPacket(0, str(self.m_DHShared))
        return