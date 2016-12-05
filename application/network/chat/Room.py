from application.network.chat.ChatHistory import ChatHistory
import netstruct

class Room:
    def __init__(self, roomID, roomName, userCount):
        self.m_chatHistory = ChatHistory(roomID)
        self.m_roomID = roomID
        self.roomName = roomName
        self.userCount = userCount
        return

    def getRoomHistory(self):
        return self.m_chatHistory

    def getRoomID(self):
        return self.m_roomID

    def callbackRoomUpdate(self, data):
        return

    def callbackRoomAction(self, data):
        return

    def callbackRoomMessage(self, messageID, ownerID, content):
        print "Got Room MSG Callback"
        print "MessageID: " + messageID + " OwnerID: " + ownerID + " Content: " + content
        self.m_chatHistory.appendMessage(messageID, ownerID, content)
        return
