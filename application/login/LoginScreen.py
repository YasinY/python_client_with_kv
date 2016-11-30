from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from application.login.LoginScreenWidgets import LoginScreenWidgets


class LoginScreen(Screen):
    def __build__(self):
        Builder.load_file("./login/LoginScreen.kv")
        return LoginScreenWidgets()
