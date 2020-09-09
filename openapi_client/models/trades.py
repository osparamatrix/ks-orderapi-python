# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Trades(object):
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
        'tradeId': 'float',
        'orderId': 'str',
        'exchangeTradeId': 'str',
        'instrumentName': 'str',
        'instrumentToken': 'str',
        'exchange': 'str',
        'price': 'float',
        'quantity': 'int',
        'transactionType': 'str',
        'product': 'str',
        'orderTimestamp': 'str',
        'tradeTimestamp': 'str'
    }

    attribute_map = {
        'tradeId': 'tradeId',
        'orderId': 'orderId',
        'exchangeTradeId': 'exchangeTradeId',
        'instrumentName': 'instrumentName',
        'instrumentToken': 'instrumentToken',
        'exchange': 'exchange',
        'price': 'price',
        'quantity': 'quantity',
        'transactionType': 'transactionType',
        'product': 'product',
        'orderTimestamp': 'orderTimestamp',
        'tradeTimestamp': 'tradeTimestamp'
    }

    def __init__(self, tradeId=None, orderId=None, exchangeTradeId=None, instrumentName=None, instrumentToken=None, exchange=None, price=None, quantity=None, transactionType=None, product=None, orderTimestamp=None, tradeTimestamp=None, local_vars_configuration=None):  # noqa: E501
        """Trades - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tradeId = None
        self._orderId = None
        self._exchangeTradeId = None
        self._instrumentName = None
        self._instrumentToken = None
        self._exchange = None
        self._price = None
        self._quantity = None
        self._transactionType = None
        self._product = None
        self._orderTimestamp = None
        self._tradeTimestamp = None
        self.discriminator = None

        if tradeId is not None:
            self.tradeId = tradeId
        if orderId is not None:
            self.orderId = orderId
        if exchangeTradeId is not None:
            self.exchangeTradeId = exchangeTradeId
        if instrumentName is not None:
            self.instrumentName = instrumentName
        if instrumentToken is not None:
            self.instrumentToken = instrumentToken
        if exchange is not None:
            self.exchange = exchange
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity
        if transactionType is not None:
            self.transactionType = transactionType
        if product is not None:
            self.product = product
        if orderTimestamp is not None:
            self.orderTimestamp = orderTimestamp
        if tradeTimestamp is not None:
            self.tradeTimestamp = tradeTimestamp

    @property
    def tradeId(self):
        """Gets the tradeId of this Trades.  # noqa: E501


        :return: The tradeId of this Trades.  # noqa: E501
        :rtype: float
        """
        return self._tradeId

    @tradeId.setter
    def tradeId(self, tradeId):
        """Sets the tradeId of this Trades.


        :param tradeId: The tradeId of this Trades.  # noqa: E501
        :type tradeId: float
        """

        self._tradeId = tradeId

    @property
    def orderId(self):
        """Gets the orderId of this Trades.  # noqa: E501


        :return: The orderId of this Trades.  # noqa: E501
        :rtype: str
        """
        return self._orderId

    @orderId.setter
    def orderId(self, orderId):
        """Sets the orderId of this Trades.


        :param orderId: The orderId of this Trades.  # noqa: E501
        :type orderId: str
        """

        self._orderId = orderId

    @property
    def exchangeTradeId(self):
        """Gets the exchangeTradeId of this Trades.  # noqa: E501


        :return: The exchangeTradeId of this Trades.  # noqa: E501
        :rtype: str
        """
        return self._exchangeTradeId

    @exchangeTradeId.setter
    def exchangeTradeId(self, exchangeTradeId):
        """Sets the exchangeTradeId of this Trades.


        :param exchangeTradeId: The exchangeTradeId of this Trades.  # noqa: E501
        :type exchangeTradeId: str
        """

        self._exchangeTradeId = exchangeTradeId

    @property
    def instrumentName(self):
        """Gets the instrumentName of this Trades.  # noqa: E501


        :return: The instrumentName of this Trades.  # noqa: E501
        :rtype: str
        """
        return self._instrumentName

    @instrumentName.setter
    def instrumentName(self, instrumentName):
        """Sets the instrumentName of this Trades.


        :param instrumentName: The instrumentName of this Trades.  # noqa: E501
        :type instrumentName: str
        """

        self._instrumentName = instrumentName

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this Trades.  # noqa: E501


        :return: The instrumentToken of this Trades.  # noqa: E501
        :rtype: str
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this Trades.


        :param instrumentToken: The instrumentToken of this Trades.  # noqa: E501
        :type instrumentToken: str
        """

        self._instrumentToken = instrumentToken

    @property
    def exchange(self):
        """Gets the exchange of this Trades.  # noqa: E501


        :return: The exchange of this Trades.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this Trades.


        :param exchange: The exchange of this Trades.  # noqa: E501
        :type exchange: str
        """
        allowed_values = ["NSE", "BSE", "NSE-FX", "MCX-CM", "NCDEX-CM"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and exchange not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `exchange` ({0}), must be one of {1}"  # noqa: E501
                .format(exchange, allowed_values)
            )

        self._exchange = exchange

    @property
    def price(self):
        """Gets the price of this Trades.  # noqa: E501


        :return: The price of this Trades.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Trades.


        :param price: The price of this Trades.  # noqa: E501
        :type price: float
        """

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this Trades.  # noqa: E501


        :return: The quantity of this Trades.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Trades.


        :param quantity: The quantity of this Trades.  # noqa: E501
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def transactionType(self):
        """Gets the transactionType of this Trades.  # noqa: E501


        :return: The transactionType of this Trades.  # noqa: E501
        :rtype: str
        """
        return self._transactionType

    @transactionType.setter
    def transactionType(self, transactionType):
        """Sets the transactionType of this Trades.


        :param transactionType: The transactionType of this Trades.  # noqa: E501
        :type transactionType: str
        """
        allowed_values = ["BUY", "SELL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and transactionType not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `transactionType` ({0}), must be one of {1}"  # noqa: E501
                .format(transactionType, allowed_values)
            )

        self._transactionType = transactionType

    @property
    def product(self):
        """Gets the product of this Trades.  # noqa: E501


        :return: The product of this Trades.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Trades.


        :param product: The product of this Trades.  # noqa: E501
        :type product: str
        """
        allowed_values = ["NORMAL", "SUPERMULTIPLE", "SUPERMULTIPLEOPTION", "MTF", "TSLONEW", "BRACKETNEW", "TSLO", "BRACKET", "GTC", "COD", "CONVERT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and product not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `product` ({0}), must be one of {1}"  # noqa: E501
                .format(product, allowed_values)
            )

        self._product = product

    @property
    def orderTimestamp(self):
        """Gets the orderTimestamp of this Trades.  # noqa: E501


        :return: The orderTimestamp of this Trades.  # noqa: E501
        :rtype: str
        """
        return self._orderTimestamp

    @orderTimestamp.setter
    def orderTimestamp(self, orderTimestamp):
        """Sets the orderTimestamp of this Trades.


        :param orderTimestamp: The orderTimestamp of this Trades.  # noqa: E501
        :type orderTimestamp: str
        """

        self._orderTimestamp = orderTimestamp

    @property
    def tradeTimestamp(self):
        """Gets the tradeTimestamp of this Trades.  # noqa: E501


        :return: The tradeTimestamp of this Trades.  # noqa: E501
        :rtype: str
        """
        return self._tradeTimestamp

    @tradeTimestamp.setter
    def tradeTimestamp(self, tradeTimestamp):
        """Sets the tradeTimestamp of this Trades.


        :param tradeTimestamp: The tradeTimestamp of this Trades.  # noqa: E501
        :type tradeTimestamp: str
        """

        self._tradeTimestamp = tradeTimestamp

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
        if not isinstance(other, Trades):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Trades):
            return True

        return self.to_dict() != other.to_dict()
