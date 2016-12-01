from kivy.app import App

from application.screen.ScreenManagement import ScreenManagement


class Application(App):
    def build(self):
        print "Building application"
        return ScreenManagement()
