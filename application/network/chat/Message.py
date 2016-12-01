class Message:
    def __init__(self, messageID, ownerID, roomID, messageContent):
        self.m_messageID = messageID
        self.m_ownerID = ownerID
        self.m_roomID = roomID
        self.m_messageContent = messageContent

    def getMessageID(self):
        return self.m_messageID