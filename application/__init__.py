from application.Application import Application
from application.network.NetworkInterface import NetworkInterface

if __name__ == "__main__":
    NetworkInterface.Instance().connectToServer()
    Application().run()
