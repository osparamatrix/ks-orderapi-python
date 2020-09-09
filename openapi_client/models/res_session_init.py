# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ResSessionInit(object):
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
        'encryption': 'ResSessionInitEncryption',
        'redirect': 'ResSessionInitRedirect',
        'weblink': 'ResSessionInitWeblink',
        'message': 'str',
        'userType': 'str',
        'status': 'str'
    }

    attribute_map = {
        'encryption': 'encryption',
        'redirect': 'redirect',
        'weblink': 'weblink',
        'message': 'message',
        'userType': 'userType',
        'status': 'status'
    }

    def __init__(self, encryption=None, redirect=None, weblink=None, message=None, userType=None, status=None, local_vars_configuration=None):  # noqa: E501
        """ResSessionInit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._encryption = None
        self._redirect = None
        self._weblink = None
        self._message = None
        self._userType = None
        self._status = None
        self.discriminator = None

        if encryption is not None:
            self.encryption = encryption
        if redirect is not None:
            self.redirect = redirect
        if weblink is not None:
            self.weblink = weblink
        if message is not None:
            self.message = message
        if userType is not None:
            self.userType = userType
        if status is not None:
            self.status = status

    @property
    def encryption(self):
        """Gets the encryption of this ResSessionInit.  # noqa: E501


        :return: The encryption of this ResSessionInit.  # noqa: E501
        :rtype: ResSessionInitEncryption
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this ResSessionInit.


        :param encryption: The encryption of this ResSessionInit.  # noqa: E501
        :type encryption: ResSessionInitEncryption
        """

        self._encryption = encryption

    @property
    def redirect(self):
        """Gets the redirect of this ResSessionInit.  # noqa: E501


        :return: The redirect of this ResSessionInit.  # noqa: E501
        :rtype: ResSessionInitRedirect
        """
        return self._redirect

    @redirect.setter
    def redirect(self, redirect):
        """Sets the redirect of this ResSessionInit.


        :param redirect: The redirect of this ResSessionInit.  # noqa: E501
        :type redirect: ResSessionInitRedirect
        """

        self._redirect = redirect

    @property
    def weblink(self):
        """Gets the weblink of this ResSessionInit.  # noqa: E501


        :return: The weblink of this ResSessionInit.  # noqa: E501
        :rtype: ResSessionInitWeblink
        """
        return self._weblink

    @weblink.setter
    def weblink(self, weblink):
        """Sets the weblink of this ResSessionInit.


        :param weblink: The weblink of this ResSessionInit.  # noqa: E501
        :type weblink: ResSessionInitWeblink
        """

        self._weblink = weblink

    @property
    def message(self):
        """Gets the message of this ResSessionInit.  # noqa: E501

        Response message from API...  # noqa: E501

        :return: The message of this ResSessionInit.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ResSessionInit.

        Response message from API...  # noqa: E501

        :param message: The message of this ResSessionInit.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def userType(self):
        """Gets the userType of this ResSessionInit.  # noqa: E501

        Type of User based G : Global, V : View Only, A : Admin, D : Dealer...  # noqa: E501

        :return: The userType of this ResSessionInit.  # noqa: E501
        :rtype: str
        """
        return self._userType

    @userType.setter
    def userType(self, userType):
        """Sets the userType of this ResSessionInit.

        Type of User based G : Global, V : View Only, A : Admin, D : Dealer...  # noqa: E501

        :param userType: The userType of this ResSessionInit.  # noqa: E501
        :type userType: str
        """
        allowed_values = ["G", "V", "A", "D"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and userType not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `userType` ({0}), must be one of {1}"  # noqa: E501
                .format(userType, allowed_values)
            )

        self._userType = userType

    @property
    def status(self):
        """Gets the status of this ResSessionInit.  # noqa: E501

        Account status for a userid in system.In case of status apart from Active, redirection to weblink host is expected.  # noqa: E501

        :return: The status of this ResSessionInit.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResSessionInit.

        Account status for a userid in system.In case of status apart from Active, redirection to weblink host is expected.  # noqa: E501

        :param status: The status of this ResSessionInit.  # noqa: E501
        :type status: str
        """
        allowed_values = ["Inactive", "Deactive", "Closed", "Active", "Success"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, ResSessionInit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResSessionInit):
            return True

        return self.to_dict() != other.to_dict()
