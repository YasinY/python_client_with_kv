import os

from kivy.uix.image import Image
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

    def chatUpdateCallback(self, roomID, ownerID, messageID, messageContent):
        print "!!!!!!!!! Update Callback"
        chatContainer = self.ids.chatContainer
        children = self.ids.chatContainer.children
        if len(children) >= 1:
            for widget in children:
                if isinstance(widget, Image):
                    return
                chatContainer.remove_widget(widget)

        chatContainer.add_widget(self.getRoomProperties(roomID))

    def switchChat(self, roomId):
        RoomManager.Instance().setActiveRoom(roomId)
        RoomManager.Instance().registerUpdateCallback(self.chatUpdateCallback)
        chatContainer = self.ids.chatContainer
        children = self.ids.chatContainer.children
        if len(children) >= 1:
            for widget in children:
                chatContainer.remove_widget(widget)

        chatContainer.add_widget(self.getRoomProperties(roomId))

    def getRoomProperties(self, id):
        # Do Request on server here, query with "id"
        currentRoom = RoomManager.Instance().getRoomByID(id)
        roomHistory = currentRoom.getRoomHistory()
        wholeHistory = roomHistory.getWholeHistory()
        memberList = ["Work, In, Progress"]  # TODO do dis
        return Chat(dataChatHistory=roomHistory.getDisplayHistory(),
                    dataMemberList=self.iterateList(memberList),
                    dataLastMessage=wholeHistory[-1:])

    def iterateList(self, list):
        return "".join(str(prefix) for prefix in list)
