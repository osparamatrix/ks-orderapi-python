# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ResSessionInitWeblink(object):
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
        'host': 'str',
        'keySize': 'int'
    }

    attribute_map = {
        'host': 'host',
        'keySize': 'keySize'
    }

    def __init__(self, host=None, keySize=None, local_vars_configuration=None):  # noqa: E501
        """ResSessionInitWeblink - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host = None
        self._keySize = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if keySize is not None:
            self.keySize = keySize

    @property
    def host(self):
        """Gets the host of this ResSessionInitWeblink.  # noqa: E501

        Weblink Host for API's.  # noqa: E501

        :return: The host of this ResSessionInitWeblink.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ResSessionInitWeblink.

        Weblink Host for API's.  # noqa: E501

        :param host: The host of this ResSessionInitWeblink.  # noqa: E501
        :type host: str
        """

        self._host = host

    @property
    def keySize(self):
        """Gets the keySize of this ResSessionInitWeblink.  # noqa: E501

        Weblink Port for API's  # noqa: E501

        :return: The keySize of this ResSessionInitWeblink.  # noqa: E501
        :rtype: int
        """
        return self._keySize

    @keySize.setter
    def keySize(self, keySize):
        """Sets the keySize of this ResSessionInitWeblink.

        Weblink Port for API's  # noqa: E501

        :param keySize: The keySize of this ResSessionInitWeblink.  # noqa: E501
        :type keySize: int
        """

        self._keySize = keySize

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
        if not isinstance(other, ResSessionInitWeblink):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResSessionInitWeblink):
            return True

        return self.to_dict() != other.to_dict()
