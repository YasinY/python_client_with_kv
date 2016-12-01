from application.network.chat.ChatHistory import ChatHistory

class Room:
    def __init__(self, roomID, roomName):
        self.m_chatHistory = ChatHistory()
        return

    def callbackRoomUpdate(self, data):
        return

    def callbackRoomAction(self, data):
        return

    def callbackRoomMessage(self, data):
        self.m_chatHistory.appendMessage("", "msg_1", "Content")
        return
