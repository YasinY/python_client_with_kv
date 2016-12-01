from kivy.uix.screenmanager import Screen
from application.network.NetworkInterface import NetworkInterface
from application.screen.impl.chat.impl.Chat import Chat


class ChatHandler(Screen):
    def switch(self):
        self.parent.current = "chosenChat"  # CHOSEN CHAT

    def roomAddCallback(self, roomid, roomtype, usercount, roomname):
        self.appendChat(roomname, roomid, usercount)

    def loadChats(self):
        NetworkInterface.Instance().requestRoomList(self.roomAddCallback)

    # maybe set properties here
    def appendChat(self, chatName, chatId, chatUsers):
        self.ids.chatsContainer.add_widget(Chat(dataName=chatName, dataID=chatId, dataUserCount=chatUsers))
