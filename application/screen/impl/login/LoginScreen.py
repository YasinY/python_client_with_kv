from kivy.uix.screenmanager import Screen

from application.network.NetworkInterface import NetworkInterface


class LoginScreen(Screen):
    def switch(self):
        # TODO OR DO LOGIN CHECK HERE
        self.parent.current = 'chatHandler'
        self.parent.get_screen('chatHandler').loadChatFrames()

    def loginCallback(self, status, data):
        if status:
            self.switch()
        else:
            print "Error"

    def login(self, username, password):  # DO LOGIN HERE
        print "Logging in: " + username + " password " + password
        if not self.canLogin(username, password):
            print "Insufficient credentials"
        else:
            NetworkInterface.Instance().login(username, password, self.loginCallback)

    def canLogin(self, username, password):
        if len(username) >= 4 and len(password) >= 4:
            return True
        else:
            return False
            # return lambda x: len(username) >= 6 and len(password) >= 4, True, False fml how does this shit work
