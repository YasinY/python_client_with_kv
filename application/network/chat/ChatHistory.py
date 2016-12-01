from application.network.chat.Message import Message

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

    def getRoomID(self):
        return self.m_roomID

    def appendMessage(self, messageID, ownerID, content):
        self.m_history.append(Message(messageID, ownerID, self.m_roomID, content))
