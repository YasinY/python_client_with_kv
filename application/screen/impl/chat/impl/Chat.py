from kivy.uix.screenmanager import Screen
from application.manager.RoomManager import RoomManager
from application.network.NetworkInterface import NetworkInterface

class Chat(Screen):
    pass

    def sendMessage(self, textInput):
        messageText = textInput.text
        print "Text: " + messageText
        if len(messageText) > 120:
            print "Message is too long"
            return
        NetworkInterface.Instance().sendRoomMessage(RoomManager.Instance().getActiveRoom(), messageText)
        textInput.text = ""
        return
