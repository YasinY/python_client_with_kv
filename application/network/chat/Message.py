import time
import datetime

class Message:
    def __init__(self, messageID, ownerID, roomID, messageContent):
        self.m_messageID = messageID
        self.m_ownerID = ownerID
        self.m_roomID = roomID
        self.m_messageContent = messageContent
        self.m_recvTime = int(time.time())

    def getMessageID(self):
        return self.m_messageID

    def getMessage(self):
        return self.m_messageContent

    def getOwnerID(self):
        return self.m_ownerID

    def getDisplayTimeStamp(self):
        return datetime.datetime.fromtimestamp(self.m_recvTime).strftime('%H:%M:%S')
