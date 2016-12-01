from application.Application import Application
from application.network.NetworkInterface import NetworkInterface
from application.util.Logger import Logger
import os

if __name__ == "__main__":
    Logger.Instance().setLogToConsole(True)
    Logger.Instance().log(0, "Init", "Loaded Logger")
    Logger.Instance().log(0, "Networking", "Connecting to Server")
    if NetworkInterface.Instance().connectToServer():
        try:
            Logger.Instance().log(0, "Networking", "Connected, Running Main App")
            Application().run()
            os._exit(0)
        except KeyboardInterrupt:
            print "Cleanup Needed!"
            os._exit(0)
    else:
        Logger.Instance().log(3, "Networking", "Failed to Connect to the Server")
