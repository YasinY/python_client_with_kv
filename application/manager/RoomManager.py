from application.network.chat.Room import Room
from application.lang.Singleton import Singleton

@Singleton
class RoomManager:
    def __init__(self):
        self.m_rooms = []
        self.m_activeRoom = None
        self.m_callbackChatUpdate = None

    def registerUpdateCallback(self, callback):
        self.m_callbackChatUpdate = callback

    def notifyRoomsAboutUpdate(self, roomID, ownerID, messageID, messageContent):
        if self.m_callbackChatUpdate:
            if self.m_activeRoom == roomID:
                self.m_callbackChatUpdate(roomID, ownerID, messageID, messageContent)

    def addRoom(self, roomID, roomName, userCount):
        print "Room Manager added room " + roomName
        self.m_rooms.append(Room(roomID, roomName, userCount))

    def setActiveRoom(self, roomID):
        self.m_activeRoom = roomID

    def getActiveRoom(self):
        return self.getRoomByID(self.m_activeRoom)

    def getRoomByID(self, roomID):
        for room in self.m_rooms:
            if room.getRoomID() == roomID:
                return room

        return None
