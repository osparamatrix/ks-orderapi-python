# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Sor(object):
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
        'price': 'float',
        'quantity': 'float',
        'mesage': 'str',
        'orderId': 'str'
    }

    attribute_map = {
        'price': 'price',
        'quantity': 'quantity',
        'mesage': 'mesage',
        'orderId': 'orderId'
    }

    def __init__(self, price=None, quantity=None, mesage=None, orderId=None, local_vars_configuration=None):  # noqa: E501
        """Sor - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._price = None
        self._quantity = None
        self._mesage = None
        self._orderId = None
        self.discriminator = None

        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity
        if mesage is not None:
            self.mesage = mesage
        if orderId is not None:
            self.orderId = orderId

    @property
    def price(self):
        """Gets the price of this Sor.  # noqa: E501

        Price of the order at which order is placed  # noqa: E501

        :return: The price of this Sor.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Sor.

        Price of the order at which order is placed  # noqa: E501

        :param price: The price of this Sor.  # noqa: E501
        :type price: float
        """

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this Sor.  # noqa: E501

        Qunatity of the order placed in exchange.  # noqa: E501

        :return: The quantity of this Sor.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Sor.

        Qunatity of the order placed in exchange.  # noqa: E501

        :param quantity: The quantity of this Sor.  # noqa: E501
        :type quantity: float
        """

        self._quantity = quantity

    @property
    def mesage(self):
        """Gets the mesage of this Sor.  # noqa: E501

        Order confirmation mesage  # noqa: E501

        :return: The mesage of this Sor.  # noqa: E501
        :rtype: str
        """
        return self._mesage

    @mesage.setter
    def mesage(self, mesage):
        """Sets the mesage of this Sor.

        Order confirmation mesage  # noqa: E501

        :param mesage: The mesage of this Sor.  # noqa: E501
        :type mesage: str
        """

        self._mesage = mesage

    @property
    def orderId(self):
        """Gets the orderId of this Sor.  # noqa: E501

        Order ID of the order to be modified  # noqa: E501

        :return: The orderId of this Sor.  # noqa: E501
        :rtype: str
        """
        return self._orderId

    @orderId.setter
    def orderId(self, orderId):
        """Sets the orderId of this Sor.

        Order ID of the order to be modified  # noqa: E501

        :param orderId: The orderId of this Sor.  # noqa: E501
        :type orderId: str
        """

        self._orderId = orderId

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
        if not isinstance(other, Sor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Sor):
            return True

        return self.to_dict() != other.to_dict()
