# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ResNewSOROrder(object):
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
        'bse': 'Sor',
        'nse': 'Sor'
    }

    attribute_map = {
        'bse': 'BSE',
        'nse': 'NSE'
    }

    def __init__(self, bse=None, nse=None, local_vars_configuration=None):  # noqa: E501
        """ResNewSOROrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bse = None
        self._nse = None
        self.discriminator = None

        if bse is not None:
            self.bse = bse
        if nse is not None:
            self.nse = nse

    @property
    def bse(self):
        """Gets the bse of this ResNewSOROrder.  # noqa: E501


        :return: The bse of this ResNewSOROrder.  # noqa: E501
        :rtype: Sor
        """
        return self._bse

    @bse.setter
    def bse(self, bse):
        """Sets the bse of this ResNewSOROrder.


        :param bse: The bse of this ResNewSOROrder.  # noqa: E501
        :type bse: Sor
        """

        self._bse = bse

    @property
    def nse(self):
        """Gets the nse of this ResNewSOROrder.  # noqa: E501


        :return: The nse of this ResNewSOROrder.  # noqa: E501
        :rtype: Sor
        """
        return self._nse

    @nse.setter
    def nse(self, nse):
        """Sets the nse of this ResNewSOROrder.


        :param nse: The nse of this ResNewSOROrder.  # noqa: E501
        :type nse: Sor
        """

        self._nse = nse

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
        if not isinstance(other, ResNewSOROrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResNewSOROrder):
            return True

        return self.to_dict() != other.to_dict()
