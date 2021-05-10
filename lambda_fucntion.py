import json
import traceback

# layers import - event, enums, logger, param
import eventData
import extRepEnums
import extRepLogger
import parameterStore

# crawlers
import crawlerBase
import crawlerEdge
import crawlerMozilla
import crawlerChrome

# Global Variable
gHaveBasicInfoFromParameterStore = False
gParameterStore = {}


def doCrawl(logObj, eventDataObj):
    crawlerObj = None
    if eventDataObj.storeName == "EDGE":
        crawlerObj = crawlerEdge.CrawlerEdge(logObj, gParameterStore, eventDataObj)
    elif eventDataObj.storeName == "MOZILLA":
        crawlerObj = crawlerMozilla.CrawlerMozilla(logObj, gParameterStore, eventDataObj)
    elif eventDataObj.storeName == "CHROME":
        crawlerObj = crawlerChrome.CrawlerChrome(logObj, gParameterStore, eventDataObj)
    else:
        msg = "Unknown Extension Store : " + str(eventDataObj.storeName)
        logObj.printLog(extRepLogger.logTypeError, eventDataObj.runStamp, " doCrawl ", msg, None)
        return extRepEnums.EXT_REP_FAILURE

    retVal = crawlerObj.crawl()
    if retVal == extRepEnums.EXT_REP_FAILURE:
        msg = "Base Sitemap crawl Failed !!!"
        logObj.printLog(extRepLogger.logTypeError, eventDataObj.runStamp, " doCrawl ", msg, None)

    return retVal


def lambda_handler(event, context):
    # Reference for the Global Variables
    global gHaveBasicInfoFromParameterStore
    global gParameterStore

    # Response from the lambda
    responseData = {}

    # initialize logging
    logObj = extRepLogger.ExtRepLogger(extRepLogger.logTypeInfo)

    # Extract the event data
    eventDataObj = eventData.EventData(logObj)
    eventDataObj.extractData(event)

    # Set the logging level
    logObj.setLogLevel(eventDataObj.logLevel)

    # get the basic config from the Parameter Store
    paramStoreObj = parameterStore.ParamStore(eventDataObj.env, eventDataObj.storeName, eventDataObj.version,
                                              eventDataObj.runStamp, logObj)
    if gHaveBasicInfoFromParameterStore == False:
        gParameterStore = paramStoreObj.getBaseConfig()
        gHaveBasicInfoFromParameterStore = True

    # Check the Return value from getBaseConfig -
    if len(gParameterStore) == 0:
        gHaveBasicInfoFromParameterStore = False
        responseData["statusCode"] = extRepEnums.EXT_REP_SVR_ERROR_PARAM_STORE
        responseData["body"] = "Server Error: Error in fetching data from Parmeter Store"
    else:
        # Refresh The Parameter Store
        retVal, retParameterStore = paramStoreObj.refreshParameterStore(event)

        if retVal == 0:
            # Success -> Check if the retParameterStore is not empty
            if len(retParameterStore) != 0:
                gParameterStore = retParameterStore

            logObj.printLog(extRepLogger.logTypeInfo, eventDataObj.runStamp, " lambda_handler ",
                            "Got the Basic Configuration from Parameter Store", None)

            # Printing the Store Base URL - for the confirmation - later this log can be remove
            msg = "STORE NAME : " + str(gParameterStore['StoreBaseURL'])
            logObj.printLog(extRepLogger.logTypeInfo, eventDataObj.runStamp, " lambda_handler ", msg, None)

            # crawlStatus = doCrawl(logObj, eventDataObj);
            # if crawlStatus != extRepEnums.EXT_REP_SUCCESS:
            #     responseData["statusCode"] = extRepEnums.EXT_REP_CRAWL_ERROR
            #     responseData["body"] = json.dumps("Server Error: Error in initating the crawl")
            # else:
            #     responseData["statusCode"] = extRepEnums.EXT_REP_HTTP_OK
            #     responseData["body"] = json.dumps("Success : Crawl initiated successfully")
        # else:
            logObj.printLog(extRepLogger.logTypeError, eventDataObj.runStamp, " lambda_handler ",
                            "Failed to get the basic configuration from Parameter Store", None)
            # responseData["statusCode"] = EXT_REP_SVR_ERROR_PARAM_STORE
            responseData["body"] = json.dumps("Server Error: Error in fetching data from Parmeter Store")

    return responseData
