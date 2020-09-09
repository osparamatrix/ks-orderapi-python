# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ResSession2FA(object):
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
        'userId': 'str',
        'clientCode': 'str',
        'clientName': 'str',
        'emailId': 'str',
        'phoneNo': 'str',
        'enabledSegments': 'list[str]',
        'enabledProducts': 'list[str]',
        'sessionToken': 'str',
        'publicToken': 'str',
        'loginTime': 'int'
    }

    attribute_map = {
        'userId': 'userId',
        'clientCode': 'clientCode',
        'clientName': 'clientName',
        'emailId': 'emailId',
        'phoneNo': 'phoneNo',
        'enabledSegments': 'enabledSegments',
        'enabledProducts': 'enabledProducts',
        'sessionToken': 'sessionToken',
        'publicToken': 'publicToken',
        'loginTime': 'loginTime'
    }

    def __init__(self, userId=None, clientCode=None, clientName=None, emailId=None, phoneNo=None, enabledSegments=None, enabledProducts=None, sessionToken=None, publicToken=None, loginTime=None, local_vars_configuration=None):  # noqa: E501
        """ResSession2FA - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._userId = None
        self._clientCode = None
        self._clientName = None
        self._emailId = None
        self._phoneNo = None
        self._enabledSegments = None
        self._enabledProducts = None
        self._sessionToken = None
        self._publicToken = None
        self._loginTime = None
        self.discriminator = None

        if userId is not None:
            self.userId = userId
        if clientCode is not None:
            self.clientCode = clientCode
        if clientName is not None:
            self.clientName = clientName
        if emailId is not None:
            self.emailId = emailId
        if phoneNo is not None:
            self.phoneNo = phoneNo
        if enabledSegments is not None:
            self.enabledSegments = enabledSegments
        if enabledProducts is not None:
            self.enabledProducts = enabledProducts
        if sessionToken is not None:
            self.sessionToken = sessionToken
        if publicToken is not None:
            self.publicToken = publicToken
        if loginTime is not None:
            self.loginTime = loginTime

    @property
    def userId(self):
        """Gets the userId of this ResSession2FA.  # noqa: E501

        ID of the user  # noqa: E501

        :return: The userId of this ResSession2FA.  # noqa: E501
        :rtype: str
        """
        return self._userId

    @userId.setter
    def userId(self, userId):
        """Sets the userId of this ResSession2FA.

        ID of the user  # noqa: E501

        :param userId: The userId of this ResSession2FA.  # noqa: E501
        :type userId: str
        """

        self._userId = userId

    @property
    def clientCode(self):
        """Gets the clientCode of this ResSession2FA.  # noqa: E501

        Unique client code  # noqa: E501

        :return: The clientCode of this ResSession2FA.  # noqa: E501
        :rtype: str
        """
        return self._clientCode

    @clientCode.setter
    def clientCode(self, clientCode):
        """Sets the clientCode of this ResSession2FA.

        Unique client code  # noqa: E501

        :param clientCode: The clientCode of this ResSession2FA.  # noqa: E501
        :type clientCode: str
        """

        self._clientCode = clientCode

    @property
    def clientName(self):
        """Gets the clientName of this ResSession2FA.  # noqa: E501

        Full name of the client  # noqa: E501

        :return: The clientName of this ResSession2FA.  # noqa: E501
        :rtype: str
        """
        return self._clientName

    @clientName.setter
    def clientName(self, clientName):
        """Sets the clientName of this ResSession2FA.

        Full name of the client  # noqa: E501

        :param clientName: The clientName of this ResSession2FA.  # noqa: E501
        :type clientName: str
        """

        self._clientName = clientName

    @property
    def emailId(self):
        """Gets the emailId of this ResSession2FA.  # noqa: E501

        Email ID of the user  # noqa: E501

        :return: The emailId of this ResSession2FA.  # noqa: E501
        :rtype: str
        """
        return self._emailId

    @emailId.setter
    def emailId(self, emailId):
        """Sets the emailId of this ResSession2FA.

        Email ID of the user  # noqa: E501

        :param emailId: The emailId of this ResSession2FA.  # noqa: E501
        :type emailId: str
        """

        self._emailId = emailId

    @property
    def phoneNo(self):
        """Gets the phoneNo of this ResSession2FA.  # noqa: E501

        Registered phone number of the user  # noqa: E501

        :return: The phoneNo of this ResSession2FA.  # noqa: E501
        :rtype: str
        """
        return self._phoneNo

    @phoneNo.setter
    def phoneNo(self, phoneNo):
        """Sets the phoneNo of this ResSession2FA.

        Registered phone number of the user  # noqa: E501

        :param phoneNo: The phoneNo of this ResSession2FA.  # noqa: E501
        :type phoneNo: str
        """

        self._phoneNo = phoneNo

    @property
    def enabledSegments(self):
        """Gets the enabledSegments of this ResSession2FA.  # noqa: E501

        Enabled segments of the user - equity, currency etc  # noqa: E501

        :return: The enabledSegments of this ResSession2FA.  # noqa: E501
        :rtype: list[str]
        """
        return self._enabledSegments

    @enabledSegments.setter
    def enabledSegments(self, enabledSegments):
        """Sets the enabledSegments of this ResSession2FA.

        Enabled segments of the user - equity, currency etc  # noqa: E501

        :param enabledSegments: The enabledSegments of this ResSession2FA.  # noqa: E501
        :type enabledSegments: list[str]
        """

        self._enabledSegments = enabledSegments

    @property
    def enabledProducts(self):
        """Gets the enabledProducts of this ResSession2FA.  # noqa: E501

        Enabled products for the user - normal, supermultiple etc  # noqa: E501

        :return: The enabledProducts of this ResSession2FA.  # noqa: E501
        :rtype: list[str]
        """
        return self._enabledProducts

    @enabledProducts.setter
    def enabledProducts(self, enabledProducts):
        """Sets the enabledProducts of this ResSession2FA.

        Enabled products for the user - normal, supermultiple etc  # noqa: E501

        :param enabledProducts: The enabledProducts of this ResSession2FA.  # noqa: E501
        :type enabledProducts: list[str]
        """

        self._enabledProducts = enabledProducts

    @property
    def sessionToken(self):
        """Gets the sessionToken of this ResSession2FA.  # noqa: E501

        Access token required for trading calls  # noqa: E501

        :return: The sessionToken of this ResSession2FA.  # noqa: E501
        :rtype: str
        """
        return self._sessionToken

    @sessionToken.setter
    def sessionToken(self, sessionToken):
        """Sets the sessionToken of this ResSession2FA.

        Access token required for trading calls  # noqa: E501

        :param sessionToken: The sessionToken of this ResSession2FA.  # noqa: E501
        :type sessionToken: str
        """

        self._sessionToken = sessionToken

    @property
    def publicToken(self):
        """Gets the publicToken of this ResSession2FA.  # noqa: E501

        Public token required for broadcast session  # noqa: E501

        :return: The publicToken of this ResSession2FA.  # noqa: E501
        :rtype: str
        """
        return self._publicToken

    @publicToken.setter
    def publicToken(self, publicToken):
        """Sets the publicToken of this ResSession2FA.

        Public token required for broadcast session  # noqa: E501

        :param publicToken: The publicToken of this ResSession2FA.  # noqa: E501
        :type publicToken: str
        """

        self._publicToken = publicToken

    @property
    def loginTime(self):
        """Gets the loginTime of this ResSession2FA.  # noqa: E501

        Login time of the user in epoch format  # noqa: E501

        :return: The loginTime of this ResSession2FA.  # noqa: E501
        :rtype: int
        """
        return self._loginTime

    @loginTime.setter
    def loginTime(self, loginTime):
        """Sets the loginTime of this ResSession2FA.

        Login time of the user in epoch format  # noqa: E501

        :param loginTime: The loginTime of this ResSession2FA.  # noqa: E501
        :type loginTime: int
        """

        self._loginTime = loginTime

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
        if not isinstance(other, ResSession2FA):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResSession2FA):
            return True

        return self.to_dict() != other.to_dict()
