from kivy.uix.screenmanager import Screen


class Chat(Screen):
    def switch(self):
        self.parent.current = "chatHandler"

    # Load the chat
    def openChat(self, groupName):  # groupName / chatName
        print "Opening chat.. " + groupName
