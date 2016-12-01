from kivy.uix.screenmanager import Screen
from application.network.NetworkInterface import NetworkInterface


class ChatFrame(Screen):
    def switch(self, roomID):
        self.parent.current = "chat"
        self.parent.parent.parent.get_screen('chatHandler').createExampleChat() # switches interface
        # TODO self.parent.get_screen('chatHandler').switchChat(chatId)

    # Load the chat
    def clickChatFrame(self, roomLabel, roomID, roomName):  # groupName / chatName
        print "Opening room... ID: " + roomID + " Name: " + roomName
        self.joinRoom(roomLabel, roomID, roomName)

    def joinRoom(self, roomLabel, roomID, roomName):
        if not self.dataIsJoined:
            NetworkInterface.Instance().joinRoom(roomID, "", "")
            roomLabel.color = (0, 1, 0)
            self.dataIsJoined = True
            print "Joined room " + roomName
        self.switch(roomID)





