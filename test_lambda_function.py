import json
import unittest
from unittest import mock
from unittest.mock import patch
import lambda_function


class TestBaseSiteMapCrawlerLambda(unittest.TestCase):

    def setUp(self):
        self.event = {"RUN_STAMP": "0", "LOG_LEVEL": 3, "TEST_RUN": 1, "FORCE_CRAWL": 1, "GTI_ANALYSIS_NEEDED": 1,
                      "ATD_ANALYSIS_NEEDED": 0, "RETIREJS_ANAYSIS_NEEDED": 1, "DEVELOPER_ANALYSIS_NEEDED": 1,
                      "ENVIRONMENT": "DEV", "ENV_VERSION": "V1", "SHARD_THRESHHOLD": "20", "CRAWL_THRESHHOLD": "50",
                      "DOWNLOAD_THRESHHOLD": "10", "EndpointConfigName": "EXP-REP-Sentiment-Analysis-mxnet-EndPoint",
                      "EndpointName": "EXP-REP-SentimentAnalysis-mxnet-EndPoint",
                      "id": "biilfdcjgdkgcibilngpinbmckioefcg",
                      "name": "notrequired", "lastmod": "2020-08-31T01:42:19.000-07:00"}

    #@mock.patch("doCrawl", return_value=0)
    # @mock.patch("lambda_handler.parameterStore.ParamStore", return_value={1, 2})
    # @mock.patch("lambda_handler.paramStoreObj.refreshParameterStore",
    #             return_value=[0, {'StoreBaseURL': 'www.google.com'}])
    def testLambdaHandlerParameterTrue_para_1_retVal_0_crawl_Fail(self):
        event = {"RUN_STAMP": "0", "LOG_LEVEL": 3, "TEST_RUN": 1, "FORCE_CRAWL": 1, "GTI_ANALYSIS_NEEDED": 1,
                 "ATD_ANALYSIS_NEEDED": 0, "RETIREJS_ANAYSIS_NEEDED": 1, "DEVELOPER_ANALYSIS_NEEDED": 1,
                 "ENVIRONMENT": "DEV", "ENV_VERSION": "V1", "SHARD_THRESHHOLD": "20", "CRAWL_THRESHHOLD": "50",
                 "DOWNLOAD_THRESHHOLD": "10", "EndpointConfigName": "EXP-REP-Sentiment-Analysis-mxnet-EndPoint",
                 "EndpointName": "EXP-REP-SentimentAnalysis-mxnet-EndPoint", "id": "biilfdcjgdkgcibilngpinbmckioefcg",
                 "name": "notrequired", "lastmod": "2020-08-31T01:42:19.000-07:00"}
        with patch('lambda_function.parameterStore.ParamStore.getBaseConfig') as mockParamStoreGetBaseConfig:
            mockParamStoreGetBaseConfig.return_value = {}

            data = lambda_function.lambda_handler(event, None)
            bodyData = json.loads(data['body'])
            print("data:: ", bodyData)
        self.assertEqual(data,
                         {'statusCode': 2000, 'body': '"Server Error: Error in initating the crawl"'})

    # @mock.patch("doCrawl", return_value=0)
    # @mock.patch("lambda_handler.parameterStore.ParamStore", return_value={1, 2})
    # @mock.patch("lambda_handler.paramStoreObj.refreshParameterStore",
    #             return_value=[0, {'StoreBaseURL': 'www.google.com'}])
    # def testLambdaHandlerParameterTrue_para_1_retVal_0_crawl_Success(self, mock, mock1):
    #     self.gHaveBasicInfoFromParameterStore = 1
    #     self.gParameterStore = 1
    #     event = {"RUN_STAMP": "0", "LOG_LEVEL": 3, "TEST_RUN": 1, "FORCE_CRAWL": 1, "GTI_ANALYSIS_NEEDED": 1,
    #              "ATD_ANALYSIS_NEEDED": 0, "RETIREJS_ANAYSIS_NEEDED": 1, "DEVELOPER_ANALYSIS_NEEDED": 1,
    #              "ENVIRONMENT": "DEV", "ENV_VERSION": "V1", "SHARD_THRESHHOLD": "20", "CRAWL_THRESHHOLD": "50",
    #              "DOWNLOAD_THRESHHOLD": "10", "EndpointConfigName": "EXP-REP-Sentiment-Analysis-mxnet-EndPoint",
    #              "EndpointName": "EXP-REP-SentimentAnalysis-mxnet-EndPoint", "id": "biilfdcjgdkgcibilngpinbmckioefcg",
    #              "name": "notrequired", "lastmod": "2020-08-31T01:42:19.000-07:00"}
    #     data = lambda_function.lambda_handler(event, None)
    #     print("data:: ", data)
    #     self.assertEqual(data,
    #                      {'statusCode': 200, 'body': '"Success : Crawl initiated successfully"'})
    #
    # @mock.patch("doCrawl", return_value=0)
    # @mock.patch("lambda_handler.parameterStore.ParamStore", return_value={1, 2})
    # @mock.patch("lambda_handler.paramStoreObj.getBaseConfig", return_value={1, 2})
    # @mock.patch("lambda_handler.paramStoreObj.refreshParameterStore",
    #             return_value=[0, {'StoreBaseURL': 'www.google.com'}])
    # def testLambdaHandlerParameterTrue_para_1_retVal_1(self, mock, mock1):
    #     event = {"RUN_STAMP": "0", "LOG_LEVEL": 3, "TEST_RUN": 1, "FORCE_CRAWL": 1, "GTI_ANALYSIS_NEEDED": 1,
    #              "ATD_ANALYSIS_NEEDED": 0, "RETIREJS_ANAYSIS_NEEDED": 1, "DEVELOPER_ANALYSIS_NEEDED": 1,
    #              "ENVIRONMENT": "DEV", "ENV_VERSION": "V1", "SHARD_THRESHHOLD": "20", "CRAWL_THRESHHOLD": "50",
    #              "DOWNLOAD_THRESHHOLD": "10", "EndpointConfigName": "EXP-REP-Sentiment-Analysis-mxnet-EndPoint",
    #              "EndpointName": "EXP-REP-SentimentAnalysis-mxnet-EndPoint", "id": "biilfdcjgdkgcibilngpinbmckioefcg",
    #              "name": "notrequired", "lastmod": "2020-08-31T01:42:19.000-07:00"}
    #     data = lambda_function.lambda_handler(event, None)
    #     print("data:: ", data)
    #     self.assertEqual(data,
    #                      {'statusCode': 1000, 'body': '"Server Error: Error in fetching data from Parmeter Store"'})
    #
    # @mock.patch("lambda_handler.parameterStore.ParamStore", return_value={1, 2})
    # @mock.patch("lambda_handler.paramStoreObj.refreshParameterStore",
    #             return_value=[0, {'StoreBaseURL': 'www.google.com'}])
    # def testLambdaHandlerParameterFalse_para_0(self, mock, mock1):
    #     self.gHaveBasicInfoFromParameterStore = 0
    #     self.gParameterStore = 0
    #     event = {"RUN_STAMP": "0", "LOG_LEVEL": 3, "TEST_RUN": 1, "FORCE_CRAWL": 1, "GTI_ANALYSIS_NEEDED": 1,
    #              "ATD_ANALYSIS_NEEDED": 0, "RETIREJS_ANAYSIS_NEEDED": 1, "DEVELOPER_ANALYSIS_NEEDED": 1,
    #              "ENVIRONMENT": "DEV", "ENV_VERSION": "V1", "SHARD_THRESHHOLD": "20", "CRAWL_THRESHHOLD": "50",
    #              "DOWNLOAD_THRESHHOLD": "10", "EndpointConfigName": "EXP-REP-Sentiment-Analysis-mxnet-EndPoint",
    #              "EndpointName": "EXP-REP-SentimentAnalysis-mxnet-EndPoint", "id": "biilfdcjgdkgcibilngpinbmckioefcg",
    #              "name": "notrequired", "lastmod": "2020-08-31T01:42:19.000-07:00"}
    #     data = lambda_function.lambda_handler(event, None)
    #     print("data:: ", data)
    #     self.assertEqual(data["body"], "Server Error: Error in fetching data from Parmeter Store")
    #
    # def testdoCrawl(self):
    #     data = lambda_function.doCrawl({}, {})
    #     print("data:: ", data)
    #     self.assertEqual(data, 1)
    #
    # @mock.patch("crawlerObj.crawl", return_value=1)
    # def testdoCrawl_1(self):
    #     data = lambda_function.doCrawl({}, {})
    #     print("data:: ", data)
    #     self.assertEqual(data, 1)


if __name__ == '__main__':
    unittest.main()
