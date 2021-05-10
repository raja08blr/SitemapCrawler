import json
import boto3
from extRepLogger import extRepLogger

gParamStoreID = "EXT_REP_ENGINE"
gBaseConfig = "BASE_CONFIG"
gEnv = "DEV"
gStoreName = "EDGE"
gVersion = "V1"

class ParamStore:
    def __init__(self, env, storeName, version, runStamp, logObj):
        global gEnv
        global gStoreName
        global gVersion

        self.__runStamp = runStamp
        self.__logObj = logObj

    def __constructStoreName(self, base, env, store, version, config):
        path = "/" + base + "/" + env + "/" + store + "/" + version + "/" + config
        return path

    def getBaseConfig(self):
    
        paramStorePath = self.__constructStoreName(gParamStoreID, gEnv, gStoreName, gVersion, gBaseConfig)

        # Get the configuration Items From Parameter Store
        ps = {}
        self.__logObj.printLog(extRepLogger.logTypeInfo, self.__runStamp, "getBaseConfig",
                              "First time call to get the basic info from the parameter store", None)
        try:
            output = boto3.client('ssm').get_parameter(Name=paramStorePath)
            ps = json.loads(output['Parameter']['Value'])
            return ps
        except Exception as e:
            self.__logObj.printLog(extRepLogger.logTypeException, self.__runStamp, "getBaseConfig",
                                  "Exception occur while getting parameter from Parameter Store", e)
        return ps

    # Refresh Parameter Store
    def refreshParameterStore(self, payloadData):
        # self.__logObj.printLog(extRepLogger.logTypeInfo, self.__runStamp, "refreshParameterStore",
        #                       "--------->", None)
        global gEnv
        global gStoreName
        global gVersion

        # Get the configuration Items From Parameter Store
        parameterStore = {}

        env = payloadData["ENVIRONMENT"]
        version = payloadData["ENV_VERSION"]
        store = payloadData["STORE_NAME"]
        if env == gEnv and version == gVersion and store == gStoreName:
            self.__logObj.printLog(extRepLogger.logTypeInfo, self.__runStamp, "refreshParameterStore", "Parameter same no need to reload", None)
            # self.__logObj.printLog(extRepLogger.logTypeInfo, self.__runStamp, "refreshParameterStore",
            #                       "<---------", None)
            return 0, parameterStore
        storePath = self.__constructStoreName(gParamStoreID, env, store, version, gBaseConfig)
        try:
            output = boto3.client('ssm').get_parameter(Name=storePath)
            parameterStore = json.loads(output['Parameter']['Value'])
            gEnv = env
            gVersion = version
            gStoreName = store
            # self.__logObj.printLog(extRepLogger.logTypeInfo, self.__runStamp, "refreshParameterStore",
            #                       "<---------", None)
            return 0, parameterStore
        except Exception as e:
            self.__logObj.printLog(extRepLogger.logTypeException, self.__runStamp, "refreshParameterStore",
                                  "Exception occur while getting parameter from Parameter Store", e)

        return 1, parameterStore
