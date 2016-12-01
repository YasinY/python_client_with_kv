from kivy.uix.screenmanager import Screen

from application.screen.impl.chat.impl.Chat import Chat


class ChatHandler(Screen):
    def switch(self):
        self.parent.current = "chosenChat"  # CHOSEN CHAT

    def loadChats(self):
        chats = [Chat(name="topkek", id="iogeojigeaojigea"), # INTERFACE CALL#GETCHATS
                 Chat(name="kektop", id="ggeapkgeapkogeapkoge"),
                 Chat(name="ggrgoriorgiorg", id="irgigssrggrgssrg")]
        for chat in chats:
            self.appendChat(chat.name, chat.id)
            print "Chat appended " + chat.name

    # maybe set properties here
    def appendChat(self, chatName, chatId):
        self.ids.chatContainer.add_widget(Chat(name=chatName, id=chatId))
