from application.Application import Application
from application.network.NetworkInterface import NetworkInterface

if __name__ == "__main__":
    if NetworkInterface.Instance().connectToServer():
        Application().run()
    else:
        print "SHIT HAPPEND!"
