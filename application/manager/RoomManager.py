from application.network.chat.Room import Room
from application.lang.Singleton import Singleton

@Singleton
class RoomManager:
    def __init__(self):
        self.m_rooms = []

    def addRoom(self, roomID, roomName, userCount):
        self.m_rooms.append(Room(roomID, roomName))

    def getRoomByID(self, roomID):
        for room in self.m_rooms:
            if room.getRoomID() == roomID:
                return room

        return None
