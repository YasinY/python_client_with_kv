from application.network.chat.ChatHistory import ChatHistory

class Room:
    def __init__(self, roomid, roomname):
        self.m_ChatHistory = ChatHistory()
        return

    def callbackRoomUpdate(self, data):
        return

    def callbackRoomAction(self, data):
        return

    def callbackRoomMessage(self, data):
        return
