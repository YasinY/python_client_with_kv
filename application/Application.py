from kivy.app import App
from kivy.core.window import Window

from application.screen.ScreenManagement import ScreenManagement


class Application(App):
    def build(self):
        print "Building application"
        return ScreenManagement()
