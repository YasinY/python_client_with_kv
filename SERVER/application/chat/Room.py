import hashlib

class Room:
    def __init__(self, roomID, roomName):
        self.m_roomID = roomID
        self.m_roomName = roomName
        self.m_members = []

    def joinRoom(self, user):
        self.m_members.append(user);

    def getRoomID(self):
        return str(hashlib.md5(self.m_roomName + "|" + str(self.m_roomID)).hexdigest())

    def getRoomName(self):
        return self.m_roomName

    def broadcastRoomMessage(self, message):
        for client in self.m_members:
            client.broadcastMessage(message)

    def removeUser(self, user):
        try:
            self.m_members.remove(user)
        except ValueError:
            return
