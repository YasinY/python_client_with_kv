from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget


# Interface for KV file


class LoginScreenWidgets(Widget):

    # login is at kv
    def login(self, username, password):
        print "doing login, username: " + username + ", pass: " + password
        # TODO IF LOGIN VALID
        self.createChatHandler()

    def createChatHandler(self):
        screenManager = ScreenManager()
        Builder.load_file("./chat/impl/Chat.kv")
        screenManager.add_widget(Screen(name='test'))
        screenManager.current = 'test'
    # TODO REMEMBER
    def save(self, username):
        self.loginState.remember(username)
