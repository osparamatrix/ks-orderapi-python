# coding: utf-8

"""
    KS Trade API's

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.market_details_quote import MarketDetailsQuote  # noqa: E501
from openapi_client.rest import ApiException

class TestMarketDetailsQuote(unittest.TestCase):
    """MarketDetailsQuote unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MarketDetailsQuote
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.market_details_quote.MarketDetailsQuote()  # noqa: E501
        if include_optional :
            return MarketDetailsQuote(
                instrumentName = '0', 
                instrumentToken = 56, 
                lastUpdatedTime = 56, 
                lastTradedTime = 56, 
                lastPrice = 1.337, 
                lastTradedQuantity = 56, 
                totalBuyQuantity = 56, 
                totalSellQuantity = 56, 
                averageTradedPrice = 1.337, 
                openInterest = 56, 
                netChange = 1.337, 
                dprLow = 1.337, 
                dprHigh = 1.337, 
                ohlc = openapi_client.models.ohlc.OHLC(
                    open = 1.337, 
                    high = 1.337, 
                    low = 1.337, 
                    close = 1.337, ), 
                depth = openapi_client.models.depth.Depth(
                    buy = openapi_client.models.depth_buy.DepthBuy(
                        price = 1.337, 
                        quantity = 56, 
                        orders = 56, ), 
                    sell = openapi_client.models.depth_sell.DepthSell(
                        price = 1.337, 
                        quantity = 56, 
                        orders = 56, ), )
            )
        else :
            return MarketDetailsQuote(
        )

    def testMarketDetailsQuote(self):
        """Test MarketDetailsQuote"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
