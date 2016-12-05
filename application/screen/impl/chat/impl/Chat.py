from kivy.uix.screenmanager import Screen
from application.manager.RoomManager import RoomManager
from application.network.NetworkInterface import NetworkInterface

class Chat(Screen):
    pass

    def sendMessage(self, textInput):
        messageText = textInput.text
        print "Text: " + messageText
        textInput.insert_text("test")
        NetworkInterface.Instance().sendRoomMessage(RoomManager.Instance().getActiveRoom(), messageText)
        return
