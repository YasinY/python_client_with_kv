from kivy.uix.widget import Widget

from application import Config


# Interface for KV file
from application.login.impl.Login import Login


class LoginScreenWidgets(Widget):

    # login is at kv
    def login(self, username, password):
        login = Login(Config.SERVER_IP, Config.PORT)
        login.connect()
        login.login(username, password)

    # TODO REMEMBER
    def save(self, username):
        self.loginState.remember(username)
