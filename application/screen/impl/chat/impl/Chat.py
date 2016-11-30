from kivy.core.text.markup import MarkupLabel
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from application.screen.impl.chat.impl import ChatWidgets


class Chat(Screen):
    def switch(self):
        self.parent.current = "chatHandler"

    # Load the chat
    def openChat(self, groupName):  # groupName / chatName
        print "Opening chat.. " + groupName
