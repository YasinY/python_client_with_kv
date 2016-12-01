from application.network.chat.ChatHistory import ChatHistory
import netstruct

class Room:
    def __init__(self, roomID, roomName, userCount):
        self.m_chatHistory = ChatHistory()
        self.m_roomID = roomID
        self.roomName = roomName
        self.userCount = userCount
        return

    def getRoomID(self):
        return self.m_roomID

    def callbackRoomUpdate(self, data):
        return

    def callbackRoomAction(self, data):
        return

    def callbackRoomMessage(self, data):
        (message, ownerID, content) = netstruct.unpack("b$b$b$", data)
        self.m_chatHistory.appendMessage(message, ownerID, content)
        return
