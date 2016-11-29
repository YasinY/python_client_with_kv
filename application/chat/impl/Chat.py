from kivy.app import App
from kivy.core.window import Window

from application.chat.impl.ChatWidgets import ChatWidgets


class Chat(App):
    def build(self):
        Window.size = (700, 500)
        return ChatWidgets()

# TODO REMOVE!!!
if __name__ == "__main__":
    Chat().run()
