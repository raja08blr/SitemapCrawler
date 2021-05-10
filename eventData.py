from extRepLogger import extRepLogger


class EventData:
    def __init__(self, logObj):
        self.__logObj = logObj

    def extractData(self, event):
        try:
            self.runStamp = event["RUN_STAMP"]
            self.logLevel = event["LOG_LEVEL"]
            self.__logObj.setLogLevel(self.logLevel)
            self.isTestRun = event["TEST_RUN"]
            self.pageNumber = event["TEST_PAGE_NUMBER"]
            self.testCategory = event["TEST_CATEGORY"]
            self.env = event["ENVIRONMENT"]
            self.version = event["ENV_VERSION"]
            self.storeName = event["STORE_NAME"]
            self.isGtiAnalysisNeeded = event["GTI_ANALYSIS_NEEDED"]
            self.isATDAnalysisNeeded = event["ATD_ANALYSIS_NEEDED"]
            self.isRetireJsAnalysisNeeded = event["RETIREJS_ANAYSIS_NEEDED"]
            self.isDeveloperAnalsysisNeeded = event["DEVELOPER_ANALYSIS_NEEDED"]
            self.isDngAPIAnalysisNeeded = event["DANGEROUS_API_ANALYSIS_NEEDED"]
            self.isStrideAnalsysisNeeded = event["STRIDE_ANALYSIS_NEEDED"]
            self.isSNSPublishNeeded = event["SNS_PUBLISH_NEEDED"]
            self.forceCrawl = event["FORCE_CRAWL"]
        except Exception as e:
            self.__logObj.printLog(extRepLogger.logTypeException, "Default RunStamp", "extractData",
                                   "Exception occur while getting parameter from Event Object", e)

    def getPayloadData(self):
        payload = {
            "RUN_STAMP": self.runStamp,
            "LOG_LEVEL": self.logLevel,
            "TEST_RUN": self.isTestRun,
            "TEST_PAGE_NUMBER": self.pageNumber,
            "TEST_CATEGORY": self.testCategory,
            "ENVIRONMENT": self.env,
            "ENV_VERSION": self.version,
            "STORE_NAME": self.storeName,
            "GTI_ANALYSIS_NEEDED": self.isGtiAnalysisNeeded,
            "ATD_ANALYSIS_NEEDED": self.isATDAnalysisNeeded,
            "RETIREJS_ANAYSIS_NEEDED": self.isRetireJsAnalysisNeeded,
            "DEVELOPER_ANALYSIS_NEEDED": self.isDeveloperAnalsysisNeeded,
            "DANGEROUS_API_ANALYSIS_NEEDED": self.isDngAPIAnalysisNeeded,
            "STRIDE_ANALYSIS_NEEDED": self.isStrideAnalsysisNeeded,
            "SNS_PUBLISH_NEEDED": self.isSNSPublishNeeded,
            "FORCE_CRAWL": self.forceCrawl
        }
        return payload
