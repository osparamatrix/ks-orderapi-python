# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Buy(object):
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
        'quantity': 'int',
        'orders': 'int'
    }

    attribute_map = {
        'price': 'price',
        'quantity': 'quantity',
        'orders': 'orders'
    }

    def __init__(self, price=None, quantity=None, orders=None, local_vars_configuration=None):  # noqa: E501
        """Buy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._price = None
        self._quantity = None
        self._orders = None
        self.discriminator = None

        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity
        if orders is not None:
            self.orders = orders

    @property
    def price(self):
        """Gets the price of this Buy.  # noqa: E501


        :return: The price of this Buy.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Buy.


        :param price: The price of this Buy.  # noqa: E501
        :type price: float
        """

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this Buy.  # noqa: E501


        :return: The quantity of this Buy.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Buy.


        :param quantity: The quantity of this Buy.  # noqa: E501
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def orders(self):
        """Gets the orders of this Buy.  # noqa: E501


        :return: The orders of this Buy.  # noqa: E501
        :rtype: int
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this Buy.


        :param orders: The orders of this Buy.  # noqa: E501
        :type orders: int
        """

        self._orders = orders

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
        if not isinstance(other, Buy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Buy):
            return True

        return self.to_dict() != other.to_dict()
