from kivy.uix.screenmanager import Screen


class ChatHandler(Screen):
    def switch(self):
        self.parent.current = "chosenChat"  # CHOSEN CHAT
