import logging
import traceback

logTypeException = 0
logTypeCritical = 1
logTypeError = 2
logTypeInfo = 3
logTypeDebug = 4

class ExtRepLogger:
    def __init__(self, level):
        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)
        self.setLogLevel(level)  

    def setLogLevel(self, level):
        if level <= logTypeCritical:
            self.log.setLevel(logging.CRITICAL)
        elif level == logTypeError:
            self.log.setLevel(logging.ERROR)
        elif level == logTypeInfo:
            self.log.setLevel(logging.INFO)
        elif level == logTypeDebug:
            self.log.setLevel(logging.DEBUG)

    def printLog(self, level, runStamp, funcName, message, exceptions, *parameters):
        messageString = ""
        if message is not None :
            messageString = "RUN_STAMP " + runStamp + " :: " + funcName + " :: " + message
        else:
            messageString = "RUN_STAMP " + runStamp + " :: " + funcName
        if level == logTypeException:
            self.log.exception(messageString.join(traceback.format_exception(etype=type(exceptions), value=exceptions, tb=exceptions.__traceback__)))
        elif level == logTypeCritical:
            self.log.critical(messageString)
        elif level == logTypeError:
            self.log.error(messageString)
        elif level == logTypeInfo:
            self.log.info(messageString)
        elif level == logTypeDebug:
            self.log.debug(messageString)
