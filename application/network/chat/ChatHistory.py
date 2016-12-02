from application.network.chat.Message import Message
import os

class ChatHistory:
    def __init__(self, roomID):
        self.m_history = []
        self.m_roomID = roomID
        return

    def getMessageByID(self, messageID):
        for msg in self.m_history:
            if msg.getMessageID() == messageID:
                return msg

        return None

    def getWholeHistory(self):
        return self.m_history

    def getDisplayHistory(self):
        historyReturn = "---Start of History---" + os.linesep
        for msg in self.m_history:
            historyReturn += msg.getMessage() + os.linesep
        return historyReturn

    def getRoomID(self):
        return self.m_roomID

    def appendMessage(self, messageID, ownerID, content):
        print "Appending Message to RoomID: " + self.m_roomID
        self.m_history.append(Message(messageID, ownerID, self.m_roomID, content))
