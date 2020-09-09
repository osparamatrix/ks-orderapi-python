# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Instrument(object):
    """
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'instrumentToken': 'float',
        'lastPrice': 'float',
        'netChange': 'float',
        'netChangePercent': 'float',
        'averageTradedPrice': 'float',
        'lastTradedQuantity': 'float',
        'lastTradedTime': 'str',
        'openInterest': 'float',
        'totalTradeQuantity': 'float',
        'exchange': 'str',
        'instrumentName': 'str',
        'segment': 'str',
        'ohlc': 'OHLCQuote',
        'depth': 'Depth'
    }

    attribute_map = {
        'instrumentToken': 'instrumentToken',
        'lastPrice': 'lastPrice',
        'netChange': 'netChange',
        'netChangePercent': 'netChangePercent',
        'averageTradedPrice': 'averageTradedPrice',
        'lastTradedQuantity': 'lastTradedQuantity',
        'lastTradedTime': 'lastTradedTime',
        'openInterest': 'openInterest',
        'totalTradeQuantity': 'totalTradeQuantity',
        'exchange': 'exchange',
        'instrumentName': 'instrumentName',
        'segment': 'segment',
        'ohlc': 'ohlc',
        'depth': 'depth'
    }

    def __init__(self, instrumentToken=None, lastPrice=None, netChange=None, netChangePercent=None, averageTradedPrice=None, lastTradedQuantity=None, lastTradedTime=None, openInterest=None, totalTradeQuantity=None, exchange=None, instrumentName=None, segment=None, ohlc=None, depth=None, local_vars_configuration=None):  # noqa: E501
        """Instrument - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrumentToken = None
        self._lastPrice = None
        self._netChange = None
        self._netChangePercent = None
        self._averageTradedPrice = None
        self._lastTradedQuantity = None
        self._lastTradedTime = None
        self._openInterest = None
        self._totalTradeQuantity = None
        self._exchange = None
        self._instrumentName = None
        self._segment = None
        self._ohlc = None
        self._depth = None
        self.discriminator = None

        if instrumentToken is not None:
            self.instrumentToken = instrumentToken
        if lastPrice is not None:
            self.lastPrice = lastPrice
        if netChange is not None:
            self.netChange = netChange
        if netChangePercent is not None:
            self.netChangePercent = netChangePercent
        if averageTradedPrice is not None:
            self.averageTradedPrice = averageTradedPrice
        if lastTradedQuantity is not None:
            self.lastTradedQuantity = lastTradedQuantity
        if lastTradedTime is not None:
            self.lastTradedTime = lastTradedTime
        if openInterest is not None:
            self.openInterest = openInterest
        if totalTradeQuantity is not None:
            self.totalTradeQuantity = totalTradeQuantity
        if exchange is not None:
            self.exchange = exchange
        if instrumentName is not None:
            self.instrumentName = instrumentName
        if segment is not None:
            self.segment = segment
        if ohlc is not None:
            self.ohlc = ohlc
        if depth is not None:
            self.depth = depth

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this Instrument.  # noqa: E501


        :return: The instrumentToken of this Instrument.  # noqa: E501
        :rtype: float
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this Instrument.


        :param instrumentToken: The instrumentToken of this Instrument.  # noqa: E501
        :type instrumentToken: float
        """

        self._instrumentToken = instrumentToken

    @property
    def lastPrice(self):
        """Gets the lastPrice of this Instrument.  # noqa: E501


        :return: The lastPrice of this Instrument.  # noqa: E501
        :rtype: float
        """
        return self._lastPrice

    @lastPrice.setter
    def lastPrice(self, lastPrice):
        """Sets the lastPrice of this Instrument.


        :param lastPrice: The lastPrice of this Instrument.  # noqa: E501
        :type lastPrice: float
        """

        self._lastPrice = lastPrice

    @property
    def netChange(self):
        """Gets the netChange of this Instrument.  # noqa: E501


        :return: The netChange of this Instrument.  # noqa: E501
        :rtype: float
        """
        return self._netChange

    @netChange.setter
    def netChange(self, netChange):
        """Sets the netChange of this Instrument.


        :param netChange: The netChange of this Instrument.  # noqa: E501
        :type netChange: float
        """

        self._netChange = netChange

    @property
    def netChangePercent(self):
        """Gets the netChangePercent of this Instrument.  # noqa: E501


        :return: The netChangePercent of this Instrument.  # noqa: E501
        :rtype: float
        """
        return self._netChangePercent

    @netChangePercent.setter
    def netChangePercent(self, netChangePercent):
        """Sets the netChangePercent of this Instrument.


        :param netChangePercent: The netChangePercent of this Instrument.  # noqa: E501
        :type netChangePercent: float
        """

        self._netChangePercent = netChangePercent

    @property
    def averageTradedPrice(self):
        """Gets the averageTradedPrice of this Instrument.  # noqa: E501


        :return: The averageTradedPrice of this Instrument.  # noqa: E501
        :rtype: float
        """
        return self._averageTradedPrice

    @averageTradedPrice.setter
    def averageTradedPrice(self, averageTradedPrice):
        """Sets the averageTradedPrice of this Instrument.


        :param averageTradedPrice: The averageTradedPrice of this Instrument.  # noqa: E501
        :type averageTradedPrice: float
        """

        self._averageTradedPrice = averageTradedPrice

    @property
    def lastTradedQuantity(self):
        """Gets the lastTradedQuantity of this Instrument.  # noqa: E501


        :return: The lastTradedQuantity of this Instrument.  # noqa: E501
        :rtype: float
        """
        return self._lastTradedQuantity

    @lastTradedQuantity.setter
    def lastTradedQuantity(self, lastTradedQuantity):
        """Sets the lastTradedQuantity of this Instrument.


        :param lastTradedQuantity: The lastTradedQuantity of this Instrument.  # noqa: E501
        :type lastTradedQuantity: float
        """

        self._lastTradedQuantity = lastTradedQuantity

    @property
    def lastTradedTime(self):
        """Gets the lastTradedTime of this Instrument.  # noqa: E501

        Last Traded Time  # noqa: E501

        :return: The lastTradedTime of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._lastTradedTime

    @lastTradedTime.setter
    def lastTradedTime(self, lastTradedTime):
        """Sets the lastTradedTime of this Instrument.

        Last Traded Time  # noqa: E501

        :param lastTradedTime: The lastTradedTime of this Instrument.  # noqa: E501
        :type lastTradedTime: str
        """

        self._lastTradedTime = lastTradedTime

    @property
    def openInterest(self):
        """Gets the openInterest of this Instrument.  # noqa: E501


        :return: The openInterest of this Instrument.  # noqa: E501
        :rtype: float
        """
        return self._openInterest

    @openInterest.setter
    def openInterest(self, openInterest):
        """Sets the openInterest of this Instrument.


        :param openInterest: The openInterest of this Instrument.  # noqa: E501
        :type openInterest: float
        """

        self._openInterest = openInterest

    @property
    def totalTradeQuantity(self):
        """Gets the totalTradeQuantity of this Instrument.  # noqa: E501


        :return: The totalTradeQuantity of this Instrument.  # noqa: E501
        :rtype: float
        """
        return self._totalTradeQuantity

    @totalTradeQuantity.setter
    def totalTradeQuantity(self, totalTradeQuantity):
        """Sets the totalTradeQuantity of this Instrument.


        :param totalTradeQuantity: The totalTradeQuantity of this Instrument.  # noqa: E501
        :type totalTradeQuantity: float
        """

        self._totalTradeQuantity = totalTradeQuantity

    @property
    def exchange(self):
        """Gets the exchange of this Instrument.  # noqa: E501

        Exchange type  # noqa: E501

        :return: The exchange of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this Instrument.

        Exchange type  # noqa: E501

        :param exchange: The exchange of this Instrument.  # noqa: E501
        :type exchange: str
        """

        self._exchange = exchange

    @property
    def instrumentName(self):
        """Gets the instrumentName of this Instrument.  # noqa: E501

        Name of the instrument  # noqa: E501

        :return: The instrumentName of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._instrumentName

    @instrumentName.setter
    def instrumentName(self, instrumentName):
        """Sets the instrumentName of this Instrument.

        Name of the instrument  # noqa: E501

        :param instrumentName: The instrumentName of this Instrument.  # noqa: E501
        :type instrumentName: str
        """

        self._instrumentName = instrumentName

    @property
    def segment(self):
        """Gets the segment of this Instrument.  # noqa: E501

        Segment  # noqa: E501

        :return: The segment of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        """Sets the segment of this Instrument.

        Segment  # noqa: E501

        :param segment: The segment of this Instrument.  # noqa: E501
        :type segment: str
        """

        self._segment = segment

    @property
    def ohlc(self):
        """Gets the ohlc of this Instrument.  # noqa: E501


        :return: The ohlc of this Instrument.  # noqa: E501
        :rtype: OHLCQuote
        """
        return self._ohlc

    @ohlc.setter
    def ohlc(self, ohlc):
        """Sets the ohlc of this Instrument.


        :param ohlc: The ohlc of this Instrument.  # noqa: E501
        :type ohlc: OHLCQuote
        """

        self._ohlc = ohlc

    @property
    def depth(self):
        """Gets the depth of this Instrument.  # noqa: E501


        :return: The depth of this Instrument.  # noqa: E501
        :rtype: Depth
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this Instrument.


        :param depth: The depth of this Instrument.  # noqa: E501
        :type depth: Depth
        """

        self._depth = depth

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Instrument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Instrument):
            return True

        return self.to_dict() != other.to_dict()
