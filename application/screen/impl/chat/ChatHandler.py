import os

from kivy.uix.screenmanager import Screen
from application.network.NetworkInterface import NetworkInterface
from application.manager.RoomManager import RoomManager
from application.screen.impl.chat.impl.Chat import Chat
from application.screen.impl.chat.impl.ChatFrame import ChatFrame


# INTERFACE for CHATS (LEFT NODES) AND CHAT (RIGHT NODE)
class ChatHandler(Screen):

    def roomAddCallback(self, roomID, roomType, userCount, roomName):
        self.appendChatFrame(roomName, roomID, userCount)
        RoomManager.Instance().addRoom(roomID, roomName, userCount)

    def loadChatFrames(self):
        NetworkInterface.Instance().requestRoomList(self.roomAddCallback)

    # maybe set properties here
    def appendChatFrame(self, chatName, chatId, chatUsers):
        self.ids.chatsContainer.add_widget(ChatFrame(dataName=chatName, dataID=chatId, dataUserCount=chatUsers))

    # DUMMY DEF TODO REMOVE
    def createExampleChat(self):
        chatContainer = self.ids.chatContainer;
        children = self.ids.chatContainer.children
        if len(children) >= 1:  # If amount of childrens are 1 or above 1 (unlikely going to happen, but just in case so chats don't stack)
            for widget in children:
                chatContainer.remove_widget(widget)
        else:
            chatContainer.add_widget(Chat(dataChatHistory="HEIL HITLER", dataMemberList="Bennet, Yasin, Lasse"))

    def switchChat(self, roomId):
        chatContainer = self.ids.chatContainer;
        children = self.ids.chatContainer.children
        if len(children) >= 1:  # If amount of childrens are 1 or above 1 (unlikely going to happen, but just in case so chats don't stack)
            for widget in children:
                chatContainer.remove_widget(widget)
        else:
            chatContainer.add_widget(self.getRoomProperties(roomId))

    def getRoomProperties(self, id):
        # Do Request on server here, query with "id"
        chatHistory = ["Bennet: Heil Hitler!", "Yasin: Heil den Fuehrer!", "Lasse: NEIN NEIN NEIN NEIN NEIN"]
        memberList = ["Bennet der Judenschaender, Lasse der Schlaechter, Yasin der fuehrende Propagandavorstandssitzender"]
        return Chat(dataChatHistory=self.iterateList(chatHistory), dataMemberList=self.iterateList(memberList))
        # Query by ID, return Chathistory, memberlist

    def iterateList(self, list):
        return "".join(str(prefix) for prefix in list)
