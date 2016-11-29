from kivy.app import App
from kivy.core.window import Window

from LoginScreenWidgets import LoginScreenWidgets


# Init for the LoginScreen

class LoginScreen(App):
    def build(self):
        Window.size = (742, 530)
        return LoginScreenWidgets()
