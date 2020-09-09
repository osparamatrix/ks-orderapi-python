# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Depth(object):
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
        'buy': 'list[Buy]',
        'sell': 'list[Sell]'
    }

    attribute_map = {
        'buy': 'buy',
        'sell': 'sell'
    }

    def __init__(self, buy=None, sell=None, local_vars_configuration=None):  # noqa: E501
        """Depth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._buy = None
        self._sell = None
        self.discriminator = None

        if buy is not None:
            self.buy = buy
        if sell is not None:
            self.sell = sell

    @property
    def buy(self):
        """Gets the buy of this Depth.  # noqa: E501


        :return: The buy of this Depth.  # noqa: E501
        :rtype: list[Buy]
        """
        return self._buy

    @buy.setter
    def buy(self, buy):
        """Sets the buy of this Depth.


        :param buy: The buy of this Depth.  # noqa: E501
        :type buy: list[Buy]
        """

        self._buy = buy

    @property
    def sell(self):
        """Gets the sell of this Depth.  # noqa: E501


        :return: The sell of this Depth.  # noqa: E501
        :rtype: list[Sell]
        """
        return self._sell

    @sell.setter
    def sell(self, sell):
        """Sets the sell of this Depth.


        :param sell: The sell of this Depth.  # noqa: E501
        :type sell: list[Sell]
        """

        self._sell = sell

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
        if not isinstance(other, Depth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Depth):
            return True

        return self.to_dict() != other.to_dict()
