# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ResLogin(object):
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
        'oneTimeToken': 'str',
        'mpin': 'str',
        'biometric': 'str',
        'message': 'str'
    }

    attribute_map = {
        'oneTimeToken': 'oneTimeToken',
        'mpin': 'mpin',
        'biometric': 'biometric',
        'message': 'message'
    }

    def __init__(self, oneTimeToken=None, mpin=None, biometric=None, message=None, local_vars_configuration=None):  # noqa: E501
        """ResLogin - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._oneTimeToken = None
        self._mpin = None
        self._biometric = None
        self._message = None
        self.discriminator = None

        if oneTimeToken is not None:
            self.oneTimeToken = oneTimeToken
        if mpin is not None:
            self.mpin = mpin
        if biometric is not None:
            self.biometric = biometric
        if message is not None:
            self.message = message

    @property
    def oneTimeToken(self):
        """Gets the oneTimeToken of this ResLogin.  # noqa: E501

        one Time Token generated on successful authentication  # noqa: E501

        :return: The oneTimeToken of this ResLogin.  # noqa: E501
        :rtype: str
        """
        return self._oneTimeToken

    @oneTimeToken.setter
    def oneTimeToken(self, oneTimeToken):
        """Sets the oneTimeToken of this ResLogin.

        one Time Token generated on successful authentication  # noqa: E501

        :param oneTimeToken: The oneTimeToken of this ResLogin.  # noqa: E501
        :type oneTimeToken: str
        """

        self._oneTimeToken = oneTimeToken

    @property
    def mpin(self):
        """Gets the mpin of this ResLogin.  # noqa: E501

        Mpin eligibiity flag, Y for True and N for False  # noqa: E501

        :return: The mpin of this ResLogin.  # noqa: E501
        :rtype: str
        """
        return self._mpin

    @mpin.setter
    def mpin(self, mpin):
        """Sets the mpin of this ResLogin.

        Mpin eligibiity flag, Y for True and N for False  # noqa: E501

        :param mpin: The mpin of this ResLogin.  # noqa: E501
        :type mpin: str
        """

        self._mpin = mpin

    @property
    def biometric(self):
        """Gets the biometric of this ResLogin.  # noqa: E501

        Biometric eligibiity flag, Y for True and N for False  # noqa: E501

        :return: The biometric of this ResLogin.  # noqa: E501
        :rtype: str
        """
        return self._biometric

    @biometric.setter
    def biometric(self, biometric):
        """Sets the biometric of this ResLogin.

        Biometric eligibiity flag, Y for True and N for False  # noqa: E501

        :param biometric: The biometric of this ResLogin.  # noqa: E501
        :type biometric: str
        """

        self._biometric = biometric

    @property
    def message(self):
        """Gets the message of this ResLogin.  # noqa: E501

        Confirmation message on login.  # noqa: E501

        :return: The message of this ResLogin.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ResLogin.

        Confirmation message on login.  # noqa: E501

        :param message: The message of this ResLogin.  # noqa: E501
        :type message: str
        """

        self._message = message

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
        if not isinstance(other, ResLogin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResLogin):
            return True

        return self.to_dict() != other.to_dict()
