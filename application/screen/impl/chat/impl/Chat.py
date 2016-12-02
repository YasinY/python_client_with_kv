from kivy.uix.screenmanager import Screen
from application.manager.RoomManager import RoomManager
from application.network.NetworkInterface import NetworkInterface

class Chat(Screen):
    pass

    def sendMessage(self, textInput):
        print "Text: " + textInput.text
        messageText = textInput.text
        NetworkInterface.Instance().sendRoomMessage(RoomManager.Instance().getActiveRoom(), messageText)
        textInput.text = ""
        return
