import json
import boto3

# layers import - logger
from extRepLogger import extRepLogger

class SnsUtils:
    def __init__(self, logObj, eventDataObj):
        self.__logObj = logObj
        self.__eventDataObj = eventDataObj
        self.__sns = boto3.client('sns')
        
        
    def publishSnsMsg(self, message, topic):
        response = None
        if self.__eventDataObj.isSNSPublishNeeded == 1:
            try:
                response = self.__sns.publish(
                    TopicArn= topic,
                    Message=str(json.dumps(message)),
                )
            except Exception as e:
                msg = "Exception occured while publishing the SNS for Message " + str(message) + " Topic: " + str(topic)
                self.__logObj.printLog(extRepLogger.logTypeException, self.__eventDataObj.runStamp, "publishSnsMsg",msg, e)
        else:
            msg = "SNS Flag set to do not publish SNS"
            self.__logObj.printLog(extRepLogger.logTypeInfo, self.__eventDataObj.runStamp, "publishSnsMsg",msg, None)
        return response