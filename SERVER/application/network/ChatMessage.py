class ChatMessage:
    def __init__(self, user, roomID, content):
        self.m_messageID = "mid_1"
        self.m_ownerID = user.getUserID()
        self.m_roomID = roomID
        self.m_messageContent = content

    def getMessageID(self):
        return self.m_messageID

    def getMessage(self):
        return self.m_messageContent

    def getRoomID(self):
        return self.m_roomID

    def getOwnerID(self):
        return self.m_ownerID