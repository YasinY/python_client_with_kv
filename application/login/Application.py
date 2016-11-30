from kivy.app import App
from kivy.core.window import Window

from LoginScreenWidgets import LoginScreenWidgets


# Init for the LoginScreen
from application.login.LoginScreen import LoginScreen


class Application(App):
    def build(self):
        Window.size = (742, 530)
        print "Building application"
        return LoginScreen().__build__()
