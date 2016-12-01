from kivy.app import App

from application.screen.ScreenManagement import ScreenManagement

from kivy import Config

Config.set('graphics', 'multisamples', '0')
Config.set('kivy', 'show_fps', '1')
Config.set('kivy', 'log_level', 'error')

class Application(App):
    def build(self):
        print "Building application"
        return ScreenManagement()
