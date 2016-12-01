from application.network.chat.Room import Room
from application.lang.Singleton import Singleton

@Singleton
class RoomManager:
    def __init__(self):
        self.m_rooms = []

    def addRoom(self, roomID, roomName, userCount):
        print "Room Manager added room " + roomName
        self.m_rooms.append(Room(roomID, roomName, userCount))

    def getRoomByID(self, roomID):
        for room in self.m_rooms:
            if room.getRoomID() == roomID:
                return room

        return None
