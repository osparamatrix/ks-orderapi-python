# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class MarketDetailsQuote(object):
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
        'depth': 'list[Depth]'
    }

    attribute_map = {
        'depth': 'depth'
    }

    def __init__(self, depth=None, local_vars_configuration=None):  # noqa: E501
        """MarketDetailsQuote - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._depth = None
        self.discriminator = None

        if depth is not None:
            self.depth = depth

    @property
    def depth(self):
        """Gets the depth of this MarketDetailsQuote.  # noqa: E501


        :return: The depth of this MarketDetailsQuote.  # noqa: E501
        :rtype: list[Depth]
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this MarketDetailsQuote.


        :param depth: The depth of this MarketDetailsQuote.  # noqa: E501
        :type depth: list[Depth]
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
        if not isinstance(other, MarketDetailsQuote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarketDetailsQuote):
            return True

        return self.to_dict() != other.to_dict()
