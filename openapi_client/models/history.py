# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class History(object):
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
        'version': 'int',
        'orderQuantity': 'int',
        'price': 'float',
        'filledQuantity': 'int',
        'exchangeStatus': 'str',
        'status': 'str',
        'disclosedQuantity': 'int',
        'triggerPrice': 'float',
        'validity': 'str',
        'exchOrderId': 'str',
        'exchTradeId': 'str',
        'message': 'str',
        'activityTimestamp': 'str'
    }

    attribute_map = {
        'version': 'version',
        'orderQuantity': 'orderQuantity',
        'price': 'price',
        'filledQuantity': 'filledQuantity',
        'exchangeStatus': 'exchangeStatus',
        'status': 'status',
        'disclosedQuantity': 'disclosedQuantity',
        'triggerPrice': 'triggerPrice',
        'validity': 'validity',
        'exchOrderId': 'exchOrderId',
        'exchTradeId': 'exchTradeId',
        'message': 'message',
        'activityTimestamp': 'activityTimestamp'
    }

    def __init__(self, version=None, orderQuantity=None, price=None, filledQuantity=None, exchangeStatus=None, status=None, disclosedQuantity=None, triggerPrice=None, validity=None, exchOrderId=None, exchTradeId=None, message=None, activityTimestamp=None, local_vars_configuration=None):  # noqa: E501
        """History - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._orderQuantity = None
        self._price = None
        self._filledQuantity = None
        self._exchangeStatus = None
        self._status = None
        self._disclosedQuantity = None
        self._triggerPrice = None
        self._validity = None
        self._exchOrderId = None
        self._exchTradeId = None
        self._message = None
        self._activityTimestamp = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if orderQuantity is not None:
            self.orderQuantity = orderQuantity
        if price is not None:
            self.price = price
        if filledQuantity is not None:
            self.filledQuantity = filledQuantity
        if exchangeStatus is not None:
            self.exchangeStatus = exchangeStatus
        if status is not None:
            self.status = status
        if disclosedQuantity is not None:
            self.disclosedQuantity = disclosedQuantity
        if triggerPrice is not None:
            self.triggerPrice = triggerPrice
        if validity is not None:
            self.validity = validity
        if exchOrderId is not None:
            self.exchOrderId = exchOrderId
        if exchTradeId is not None:
            self.exchTradeId = exchTradeId
        if message is not None:
            self.message = message
        if activityTimestamp is not None:
            self.activityTimestamp = activityTimestamp

    @property
    def version(self):
        """Gets the version of this History.  # noqa: E501


        :return: The version of this History.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this History.


        :param version: The version of this History.  # noqa: E501
        :type version: int
        """

        self._version = version

    @property
    def orderQuantity(self):
        """Gets the orderQuantity of this History.  # noqa: E501


        :return: The orderQuantity of this History.  # noqa: E501
        :rtype: int
        """
        return self._orderQuantity

    @orderQuantity.setter
    def orderQuantity(self, orderQuantity):
        """Sets the orderQuantity of this History.


        :param orderQuantity: The orderQuantity of this History.  # noqa: E501
        :type orderQuantity: int
        """

        self._orderQuantity = orderQuantity

    @property
    def price(self):
        """Gets the price of this History.  # noqa: E501


        :return: The price of this History.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this History.


        :param price: The price of this History.  # noqa: E501
        :type price: float
        """

        self._price = price

    @property
    def filledQuantity(self):
        """Gets the filledQuantity of this History.  # noqa: E501


        :return: The filledQuantity of this History.  # noqa: E501
        :rtype: int
        """
        return self._filledQuantity

    @filledQuantity.setter
    def filledQuantity(self, filledQuantity):
        """Sets the filledQuantity of this History.


        :param filledQuantity: The filledQuantity of this History.  # noqa: E501
        :type filledQuantity: int
        """

        self._filledQuantity = filledQuantity

    @property
    def exchangeStatus(self):
        """Gets the exchangeStatus of this History.  # noqa: E501


        :return: The exchangeStatus of this History.  # noqa: E501
        :rtype: str
        """
        return self._exchangeStatus

    @exchangeStatus.setter
    def exchangeStatus(self, exchangeStatus):
        """Sets the exchangeStatus of this History.


        :param exchangeStatus: The exchangeStatus of this History.  # noqa: E501
        :type exchangeStatus: str
        """

        self._exchangeStatus = exchangeStatus

    @property
    def status(self):
        """Gets the status of this History.  # noqa: E501

        Order Status  # noqa: E501

        :return: The status of this History.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this History.

        Order Status  # noqa: E501

        :param status: The status of this History.  # noqa: E501
        :type status: str
        """
        allowed_values = ["placed", "approved", "delivered"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def disclosedQuantity(self):
        """Gets the disclosedQuantity of this History.  # noqa: E501


        :return: The disclosedQuantity of this History.  # noqa: E501
        :rtype: int
        """
        return self._disclosedQuantity

    @disclosedQuantity.setter
    def disclosedQuantity(self, disclosedQuantity):
        """Sets the disclosedQuantity of this History.


        :param disclosedQuantity: The disclosedQuantity of this History.  # noqa: E501
        :type disclosedQuantity: int
        """

        self._disclosedQuantity = disclosedQuantity

    @property
    def triggerPrice(self):
        """Gets the triggerPrice of this History.  # noqa: E501


        :return: The triggerPrice of this History.  # noqa: E501
        :rtype: float
        """
        return self._triggerPrice

    @triggerPrice.setter
    def triggerPrice(self, triggerPrice):
        """Sets the triggerPrice of this History.


        :param triggerPrice: The triggerPrice of this History.  # noqa: E501
        :type triggerPrice: float
        """

        self._triggerPrice = triggerPrice

    @property
    def validity(self):
        """Gets the validity of this History.  # noqa: E501


        :return: The validity of this History.  # noqa: E501
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this History.


        :param validity: The validity of this History.  # noqa: E501
        :type validity: str
        """
        allowed_values = ["GFD", "IOC"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and validity not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `validity` ({0}), must be one of {1}"  # noqa: E501
                .format(validity, allowed_values)
            )

        self._validity = validity

    @property
    def exchOrderId(self):
        """Gets the exchOrderId of this History.  # noqa: E501


        :return: The exchOrderId of this History.  # noqa: E501
        :rtype: str
        """
        return self._exchOrderId

    @exchOrderId.setter
    def exchOrderId(self, exchOrderId):
        """Sets the exchOrderId of this History.


        :param exchOrderId: The exchOrderId of this History.  # noqa: E501
        :type exchOrderId: str
        """

        self._exchOrderId = exchOrderId

    @property
    def exchTradeId(self):
        """Gets the exchTradeId of this History.  # noqa: E501


        :return: The exchTradeId of this History.  # noqa: E501
        :rtype: str
        """
        return self._exchTradeId

    @exchTradeId.setter
    def exchTradeId(self, exchTradeId):
        """Sets the exchTradeId of this History.


        :param exchTradeId: The exchTradeId of this History.  # noqa: E501
        :type exchTradeId: str
        """

        self._exchTradeId = exchTradeId

    @property
    def message(self):
        """Gets the message of this History.  # noqa: E501


        :return: The message of this History.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this History.


        :param message: The message of this History.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def activityTimestamp(self):
        """Gets the activityTimestamp of this History.  # noqa: E501


        :return: The activityTimestamp of this History.  # noqa: E501
        :rtype: str
        """
        return self._activityTimestamp

    @activityTimestamp.setter
    def activityTimestamp(self, activityTimestamp):
        """Sets the activityTimestamp of this History.


        :param activityTimestamp: The activityTimestamp of this History.  # noqa: E501
        :type activityTimestamp: str
        """

        self._activityTimestamp = activityTimestamp

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
        if not isinstance(other, History):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, History):
            return True

        return self.to_dict() != other.to_dict()
