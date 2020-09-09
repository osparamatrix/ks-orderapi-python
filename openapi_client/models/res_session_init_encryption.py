# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ResSessionInitEncryption(object):
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
        'type': 'str',
        'publickKey': 'str',
        'keySize': 'int'
    }

    attribute_map = {
        'type': 'type',
        'publickKey': 'publickKey',
        'keySize': 'keySize'
    }

    def __init__(self, type=None, publickKey=None, keySize=None, local_vars_configuration=None):  # noqa: E501
        """ResSessionInitEncryption - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._publickKey = None
        self._keySize = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if publickKey is not None:
            self.publickKey = publickKey
        if keySize is not None:
            self.keySize = keySize

    @property
    def type(self):
        """Gets the type of this ResSessionInitEncryption.  # noqa: E501

        Type of Encryption.  # noqa: E501

        :return: The type of this ResSessionInitEncryption.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResSessionInitEncryption.

        Type of Encryption.  # noqa: E501

        :param type: The type of this ResSessionInitEncryption.  # noqa: E501
        :type type: str
        """
        allowed_values = ["PLAIN", "BASE64", "RSA", "AES"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def publickKey(self):
        """Gets the publickKey of this ResSessionInitEncryption.  # noqa: E501

        Key Applicable in case of RSA,AES.  # noqa: E501

        :return: The publickKey of this ResSessionInitEncryption.  # noqa: E501
        :rtype: str
        """
        return self._publickKey

    @publickKey.setter
    def publickKey(self, publickKey):
        """Sets the publickKey of this ResSessionInitEncryption.

        Key Applicable in case of RSA,AES.  # noqa: E501

        :param publickKey: The publickKey of this ResSessionInitEncryption.  # noqa: E501
        :type publickKey: str
        """

        self._publickKey = publickKey

    @property
    def keySize(self):
        """Gets the keySize of this ResSessionInitEncryption.  # noqa: E501

        Applicable Key size of type of Encryption.  # noqa: E501

        :return: The keySize of this ResSessionInitEncryption.  # noqa: E501
        :rtype: int
        """
        return self._keySize

    @keySize.setter
    def keySize(self, keySize):
        """Sets the keySize of this ResSessionInitEncryption.

        Applicable Key size of type of Encryption.  # noqa: E501

        :param keySize: The keySize of this ResSessionInitEncryption.  # noqa: E501
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
        if not isinstance(other, ResSessionInitEncryption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResSessionInitEncryption):
            return True

        return self.to_dict() != other.to_dict()
