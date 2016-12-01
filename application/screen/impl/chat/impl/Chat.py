from kivy.uix.screenmanager import Screen
from application.network.NetworkInterface import NetworkInterface

class Chat(Screen):
    def switch(self):
        self.parent.current = "chatHandler"

    # Load the chat
    def openChat(self, roomLabel, roomID, roomName):  # groupName / chatName
        print "Opening chat... ID: " + roomID + " Name: " + roomName
        if not self.dataIsJoined:
            NetworkInterface.Instance().joinRoom(roomID, "", "")
            roomLabel.color = (0, 1, 0)
            self.dataIsJoined = True
