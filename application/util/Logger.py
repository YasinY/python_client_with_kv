from application.lang.Singleton import Singleton

@Singleton
class Logger:
    def __init__(self):
        self.m_logToConsole = False
        self.m_logToFile = False
        self.m_logFileName = None
        self.m_logFile = None
        self.m_logLevels = {
            0: "DEBUG",
            1: "INFO",
            2: "WARNING",
            3: "ERROR"
        }

    def setLogToConsole(self, enableLogging):
        self.m_logToConsole = enableLogging

    def setLogToFile(self, enableLogging):
        if not self.m_logFileName:
            self.m_logFile = file.open(self.m_logFileName, "w+")

    def log(self, msgLevel, msgCategory, msgContent):
        logType = self.m_logLevels.get(msgLevel)
        logMsg = "[" + logType + "] [" + msgCategory + "] " + msgContent
        if self.m_logToConsole:
            print logMsg
