from kivy.uix.screenmanager import Screen
from application.network.NetworkInterface import NetworkInterface
from application.screen.impl.chat.impl.Chat import Chat
from application.manager.RoomManager import RoomManager

class ChatHandler(Screen):
    def switch(self):
        self.parent.current = "chosenChat"  # CHOSEN CHAT

    def roomAddCallback(self, roomID, roomType, userCount, roomName):
        self.appendChat(roomName, roomID, userCount)
        RoomManager.Instance().addRoom(roomID, roomName, userCount)

    def loadChats(self):
        NetworkInterface.Instance().requestRoomList(self.roomAddCallback)

    # maybe set properties here
    def appendChat(self, chatName, chatId, chatUsers):
        self.ids.chatsContainer.add_widget(Chat(dataName=chatName, dataID=chatId, dataUserCount=chatUsers))
