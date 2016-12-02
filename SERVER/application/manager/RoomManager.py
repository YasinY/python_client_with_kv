from application.lang.Singleton import Singleton
from application.database.DatabaseConnector import DatabaseConnector
from application.chat.Room import Room

@Singleton
class RoomManager:
    def __init__(self):
        self.m_rooms = []
        return

    def loadRoomsFromDB(self):
        print "Loading Rooms"
        for room in DatabaseConnector.Instance().executeQuery("SELECT * FROM chat_rooms"):
            self.m_rooms.append(Room(room[0], room[1]))
            print "Added Room ID: " + str(room[0]) + " Name: " + str(room[1])
        return

    def getAllRooms(self):
        return self.m_rooms

    def getRoomByID(self, roomID):
        for room in self.m_rooms:
            if room.getRoomID() == roomID:
                return room