# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class OHLCQuote(object):
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
        'instrumentName': 'str',
        'instrumentToken': 'int',
        'open': 'float',
        'high': 'float',
        'low': 'float',
        'close': 'float'
    }

    attribute_map = {
        'instrumentName': 'instrumentName',
        'instrumentToken': 'instrumentToken',
        'open': 'open',
        'high': 'high',
        'low': 'low',
        'close': 'close'
    }

    def __init__(self, instrumentName=None, instrumentToken=None, open=None, high=None, low=None, close=None, local_vars_configuration=None):  # noqa: E501
        """OHLCQuote - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrumentName = None
        self._instrumentToken = None
        self._open = None
        self._high = None
        self._low = None
        self._close = None
        self.discriminator = None

        if instrumentName is not None:
            self.instrumentName = instrumentName
        if instrumentToken is not None:
            self.instrumentToken = instrumentToken
        if open is not None:
            self.open = open
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if close is not None:
            self.close = close

    @property
    def instrumentName(self):
        """Gets the instrumentName of this OHLCQuote.  # noqa: E501

        Name of the instrument  # noqa: E501

        :return: The instrumentName of this OHLCQuote.  # noqa: E501
        :rtype: str
        """
        return self._instrumentName

    @instrumentName.setter
    def instrumentName(self, instrumentName):
        """Sets the instrumentName of this OHLCQuote.

        Name of the instrument  # noqa: E501

        :param instrumentName: The instrumentName of this OHLCQuote.  # noqa: E501
        :type instrumentName: str
        """

        self._instrumentName = instrumentName

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this OHLCQuote.  # noqa: E501


        :return: The instrumentToken of this OHLCQuote.  # noqa: E501
        :rtype: int
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this OHLCQuote.


        :param instrumentToken: The instrumentToken of this OHLCQuote.  # noqa: E501
        :type instrumentToken: int
        """

        self._instrumentToken = instrumentToken

    @property
    def open(self):
        """Gets the open of this OHLCQuote.  # noqa: E501


        :return: The open of this OHLCQuote.  # noqa: E501
        :rtype: float
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this OHLCQuote.


        :param open: The open of this OHLCQuote.  # noqa: E501
        :type open: float
        """

        self._open = open

    @property
    def high(self):
        """Gets the high of this OHLCQuote.  # noqa: E501


        :return: The high of this OHLCQuote.  # noqa: E501
        :rtype: float
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this OHLCQuote.


        :param high: The high of this OHLCQuote.  # noqa: E501
        :type high: float
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this OHLCQuote.  # noqa: E501


        :return: The low of this OHLCQuote.  # noqa: E501
        :rtype: float
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this OHLCQuote.


        :param low: The low of this OHLCQuote.  # noqa: E501
        :type low: float
        """

        self._low = low

    @property
    def close(self):
        """Gets the close of this OHLCQuote.  # noqa: E501


        :return: The close of this OHLCQuote.  # noqa: E501
        :rtype: float
        """
        return self._close

    @close.setter
    def close(self, close):
        """Sets the close of this OHLCQuote.


        :param close: The close of this OHLCQuote.  # noqa: E501
        :type close: float
        """

        self._close = close

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
        if not isinstance(other, OHLCQuote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OHLCQuote):
            return True

        return self.to_dict() != other.to_dict()
