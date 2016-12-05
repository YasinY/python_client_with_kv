import os

from kivy.uix.screenmanager import Screen
import netstruct
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
            (errorCode, errorReason) = netstruct.unpack("ib$", data)
            errorReasons = {
                1: "Login: ",
                2: "User: ",
                3: "Register: "
            }
            self.dataErrorText = errorReasons.get(errorCode) + errorReason
            print "Error"

    def register(self, username, password):
        print "Regging: " + username + " password ****"
        if not self.canLogin(username, password):
            self.dataErrorText = "Insufficient credentials"
        else:
            NetworkInterface.Instance().register(username, password, self.loginCallback)

    def login(self, username, password):  # DO LOGIN HERE
        print "Logging in: " + username + " password ****"
        if not self.canLogin(username, password):
            self.dataErrorText = "Insufficient credentials"
        else:
            self.dataErrorText = "Logging in.." + os.linesep + "If this takes too long, the server may be having a rough time." + os.linesep + "Please try again later."
            NetworkInterface.Instance().login(username, password, self.loginCallback)

    def canLogin(self, username, password):
        if len(username) >= 4 and len(password) >= 4:
            return True
        else:
            return False
            # return lambda x: len(username) >= 6 and len(password) >= 4, True, False fml how does this shit work
