# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Stocks(object):
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
        'instrumentToken': 'int',
        'normal': 'float',
        'supermultiple': 'float',
        'mtf': 'float',
        'actualMTM': 'float',
        'actualPNL': 'float',
        'averageStockPrice': 'float',
        'bnstCredit': 'float',
        'buyOpenQtyLot': 'int',
        'buyOpenValue': 'float',
        'delStockPrice': 'float',
        'deliveryStatus': 'int',
        'exchange': 'str',
        'fnoBnstCredit': 'int',
        'fnoPremium': 'int',
        'hairCut': 'int',
        'holdStock': 'int',
        'instrumentName': 'str',
        'multiple': 'int',
        'multipleType': 'int',
        'mfHairCut': 'int',
        'netTrdQtyLot': 'int',
        'netTrdValue': 'float',
        'openingStockValue': 'float',
        'premium': 'float',
        'previousMTMTrades': 'int',
        'realizedPL': 'float',
        'sellOpenQtyLot': 'int',
        'sellOpenValue': 'int',
        'securityValuation': 'int',
        'securityValuationMTF': 'float',
        'stockBalance': 'int'
    }

    attribute_map = {
        'instrumentToken': 'instrumentToken',
        'normal': 'normal',
        'supermultiple': 'supermultiple',
        'mtf': 'mtf',
        'actualMTM': 'actualMTM',
        'actualPNL': 'actualPNL',
        'averageStockPrice': 'averageStockPrice',
        'bnstCredit': 'bnstCredit',
        'buyOpenQtyLot': 'buyOpenQtyLot',
        'buyOpenValue': 'buyOpenValue',
        'delStockPrice': 'delStockPrice',
        'deliveryStatus': 'deliveryStatus',
        'exchange': 'exchange',
        'fnoBnstCredit': 'fnoBnstCredit',
        'fnoPremium': 'fnoPremium',
        'hairCut': 'hairCut',
        'holdStock': 'holdStock',
        'instrumentName': 'instrumentName',
        'multiple': 'multiple',
        'multipleType': 'multipleType',
        'mfHairCut': 'mfHairCut',
        'netTrdQtyLot': 'netTrdQtyLot',
        'netTrdValue': 'netTrdValue',
        'openingStockValue': 'openingStockValue',
        'premium': 'premium',
        'previousMTMTrades': 'previousMTMTrades',
        'realizedPL': 'realizedPL',
        'sellOpenQtyLot': 'sellOpenQtyLot',
        'sellOpenValue': 'sellOpenValue',
        'securityValuation': 'securityValuation',
        'securityValuationMTF': 'securityValuationMTF',
        'stockBalance': 'stockBalance'
    }

    def __init__(self, instrumentToken=None, normal=None, supermultiple=None, mtf=None, actualMTM=None, actualPNL=None, averageStockPrice=None, bnstCredit=None, buyOpenQtyLot=None, buyOpenValue=None, delStockPrice=None, deliveryStatus=None, exchange=None, fnoBnstCredit=None, fnoPremium=None, hairCut=None, holdStock=None, instrumentName=None, multiple=None, multipleType=None, mfHairCut=None, netTrdQtyLot=None, netTrdValue=None, openingStockValue=None, premium=None, previousMTMTrades=None, realizedPL=None, sellOpenQtyLot=None, sellOpenValue=None, securityValuation=None, securityValuationMTF=None, stockBalance=None, local_vars_configuration=None):  # noqa: E501
        """Stocks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrumentToken = None
        self._normal = None
        self._supermultiple = None
        self._mtf = None
        self._actualMTM = None
        self._actualPNL = None
        self._averageStockPrice = None
        self._bnstCredit = None
        self._buyOpenQtyLot = None
        self._buyOpenValue = None
        self._delStockPrice = None
        self._deliveryStatus = None
        self._exchange = None
        self._fnoBnstCredit = None
        self._fnoPremium = None
        self._hairCut = None
        self._holdStock = None
        self._instrumentName = None
        self._multiple = None
        self._multipleType = None
        self._mfHairCut = None
        self._netTrdQtyLot = None
        self._netTrdValue = None
        self._openingStockValue = None
        self._premium = None
        self._previousMTMTrades = None
        self._realizedPL = None
        self._sellOpenQtyLot = None
        self._sellOpenValue = None
        self._securityValuation = None
        self._securityValuationMTF = None
        self._stockBalance = None
        self.discriminator = None

        if instrumentToken is not None:
            self.instrumentToken = instrumentToken
        if normal is not None:
            self.normal = normal
        if supermultiple is not None:
            self.supermultiple = supermultiple
        if mtf is not None:
            self.mtf = mtf
        if actualMTM is not None:
            self.actualMTM = actualMTM
        if actualPNL is not None:
            self.actualPNL = actualPNL
        if averageStockPrice is not None:
            self.averageStockPrice = averageStockPrice
        if bnstCredit is not None:
            self.bnstCredit = bnstCredit
        if buyOpenQtyLot is not None:
            self.buyOpenQtyLot = buyOpenQtyLot
        if buyOpenValue is not None:
            self.buyOpenValue = buyOpenValue
        if delStockPrice is not None:
            self.delStockPrice = delStockPrice
        if deliveryStatus is not None:
            self.deliveryStatus = deliveryStatus
        if exchange is not None:
            self.exchange = exchange
        if fnoBnstCredit is not None:
            self.fnoBnstCredit = fnoBnstCredit
        if fnoPremium is not None:
            self.fnoPremium = fnoPremium
        if hairCut is not None:
            self.hairCut = hairCut
        if holdStock is not None:
            self.holdStock = holdStock
        if instrumentName is not None:
            self.instrumentName = instrumentName
        if multiple is not None:
            self.multiple = multiple
        if multipleType is not None:
            self.multipleType = multipleType
        if mfHairCut is not None:
            self.mfHairCut = mfHairCut
        if netTrdQtyLot is not None:
            self.netTrdQtyLot = netTrdQtyLot
        if netTrdValue is not None:
            self.netTrdValue = netTrdValue
        if openingStockValue is not None:
            self.openingStockValue = openingStockValue
        if premium is not None:
            self.premium = premium
        if previousMTMTrades is not None:
            self.previousMTMTrades = previousMTMTrades
        if realizedPL is not None:
            self.realizedPL = realizedPL
        if sellOpenQtyLot is not None:
            self.sellOpenQtyLot = sellOpenQtyLot
        if sellOpenValue is not None:
            self.sellOpenValue = sellOpenValue
        if securityValuation is not None:
            self.securityValuation = securityValuation
        if securityValuationMTF is not None:
            self.securityValuationMTF = securityValuationMTF
        if stockBalance is not None:
            self.stockBalance = stockBalance

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this Stocks.  # noqa: E501


        :return: The instrumentToken of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this Stocks.


        :param instrumentToken: The instrumentToken of this Stocks.  # noqa: E501
        :type instrumentToken: int
        """

        self._instrumentToken = instrumentToken

    @property
    def normal(self):
        """Gets the normal of this Stocks.  # noqa: E501

        Order Status  # noqa: E501

        :return: The normal of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._normal

    @normal.setter
    def normal(self, normal):
        """Sets the normal of this Stocks.

        Order Status  # noqa: E501

        :param normal: The normal of this Stocks.  # noqa: E501
        :type normal: float
        """

        self._normal = normal

    @property
    def supermultiple(self):
        """Gets the supermultiple of this Stocks.  # noqa: E501

        Order Status  # noqa: E501

        :return: The supermultiple of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._supermultiple

    @supermultiple.setter
    def supermultiple(self, supermultiple):
        """Sets the supermultiple of this Stocks.

        Order Status  # noqa: E501

        :param supermultiple: The supermultiple of this Stocks.  # noqa: E501
        :type supermultiple: float
        """

        self._supermultiple = supermultiple

    @property
    def mtf(self):
        """Gets the mtf of this Stocks.  # noqa: E501

        Order Status  # noqa: E501

        :return: The mtf of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._mtf

    @mtf.setter
    def mtf(self, mtf):
        """Sets the mtf of this Stocks.

        Order Status  # noqa: E501

        :param mtf: The mtf of this Stocks.  # noqa: E501
        :type mtf: float
        """

        self._mtf = mtf

    @property
    def actualMTM(self):
        """Gets the actualMTM of this Stocks.  # noqa: E501


        :return: The actualMTM of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._actualMTM

    @actualMTM.setter
    def actualMTM(self, actualMTM):
        """Sets the actualMTM of this Stocks.


        :param actualMTM: The actualMTM of this Stocks.  # noqa: E501
        :type actualMTM: float
        """

        self._actualMTM = actualMTM

    @property
    def actualPNL(self):
        """Gets the actualPNL of this Stocks.  # noqa: E501


        :return: The actualPNL of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._actualPNL

    @actualPNL.setter
    def actualPNL(self, actualPNL):
        """Sets the actualPNL of this Stocks.


        :param actualPNL: The actualPNL of this Stocks.  # noqa: E501
        :type actualPNL: float
        """

        self._actualPNL = actualPNL

    @property
    def averageStockPrice(self):
        """Gets the averageStockPrice of this Stocks.  # noqa: E501


        :return: The averageStockPrice of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._averageStockPrice

    @averageStockPrice.setter
    def averageStockPrice(self, averageStockPrice):
        """Sets the averageStockPrice of this Stocks.


        :param averageStockPrice: The averageStockPrice of this Stocks.  # noqa: E501
        :type averageStockPrice: float
        """

        self._averageStockPrice = averageStockPrice

    @property
    def bnstCredit(self):
        """Gets the bnstCredit of this Stocks.  # noqa: E501


        :return: The bnstCredit of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._bnstCredit

    @bnstCredit.setter
    def bnstCredit(self, bnstCredit):
        """Sets the bnstCredit of this Stocks.


        :param bnstCredit: The bnstCredit of this Stocks.  # noqa: E501
        :type bnstCredit: float
        """

        self._bnstCredit = bnstCredit

    @property
    def buyOpenQtyLot(self):
        """Gets the buyOpenQtyLot of this Stocks.  # noqa: E501


        :return: The buyOpenQtyLot of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._buyOpenQtyLot

    @buyOpenQtyLot.setter
    def buyOpenQtyLot(self, buyOpenQtyLot):
        """Sets the buyOpenQtyLot of this Stocks.


        :param buyOpenQtyLot: The buyOpenQtyLot of this Stocks.  # noqa: E501
        :type buyOpenQtyLot: int
        """

        self._buyOpenQtyLot = buyOpenQtyLot

    @property
    def buyOpenValue(self):
        """Gets the buyOpenValue of this Stocks.  # noqa: E501


        :return: The buyOpenValue of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._buyOpenValue

    @buyOpenValue.setter
    def buyOpenValue(self, buyOpenValue):
        """Sets the buyOpenValue of this Stocks.


        :param buyOpenValue: The buyOpenValue of this Stocks.  # noqa: E501
        :type buyOpenValue: float
        """

        self._buyOpenValue = buyOpenValue

    @property
    def delStockPrice(self):
        """Gets the delStockPrice of this Stocks.  # noqa: E501


        :return: The delStockPrice of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._delStockPrice

    @delStockPrice.setter
    def delStockPrice(self, delStockPrice):
        """Sets the delStockPrice of this Stocks.


        :param delStockPrice: The delStockPrice of this Stocks.  # noqa: E501
        :type delStockPrice: float
        """

        self._delStockPrice = delStockPrice

    @property
    def deliveryStatus(self):
        """Gets the deliveryStatus of this Stocks.  # noqa: E501


        :return: The deliveryStatus of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._deliveryStatus

    @deliveryStatus.setter
    def deliveryStatus(self, deliveryStatus):
        """Sets the deliveryStatus of this Stocks.


        :param deliveryStatus: The deliveryStatus of this Stocks.  # noqa: E501
        :type deliveryStatus: int
        """

        self._deliveryStatus = deliveryStatus

    @property
    def exchange(self):
        """Gets the exchange of this Stocks.  # noqa: E501


        :return: The exchange of this Stocks.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this Stocks.


        :param exchange: The exchange of this Stocks.  # noqa: E501
        :type exchange: str
        """

        self._exchange = exchange

    @property
    def fnoBnstCredit(self):
        """Gets the fnoBnstCredit of this Stocks.  # noqa: E501


        :return: The fnoBnstCredit of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._fnoBnstCredit

    @fnoBnstCredit.setter
    def fnoBnstCredit(self, fnoBnstCredit):
        """Sets the fnoBnstCredit of this Stocks.


        :param fnoBnstCredit: The fnoBnstCredit of this Stocks.  # noqa: E501
        :type fnoBnstCredit: int
        """

        self._fnoBnstCredit = fnoBnstCredit

    @property
    def fnoPremium(self):
        """Gets the fnoPremium of this Stocks.  # noqa: E501


        :return: The fnoPremium of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._fnoPremium

    @fnoPremium.setter
    def fnoPremium(self, fnoPremium):
        """Sets the fnoPremium of this Stocks.


        :param fnoPremium: The fnoPremium of this Stocks.  # noqa: E501
        :type fnoPremium: int
        """

        self._fnoPremium = fnoPremium

    @property
    def hairCut(self):
        """Gets the hairCut of this Stocks.  # noqa: E501


        :return: The hairCut of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._hairCut

    @hairCut.setter
    def hairCut(self, hairCut):
        """Sets the hairCut of this Stocks.


        :param hairCut: The hairCut of this Stocks.  # noqa: E501
        :type hairCut: int
        """

        self._hairCut = hairCut

    @property
    def holdStock(self):
        """Gets the holdStock of this Stocks.  # noqa: E501


        :return: The holdStock of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._holdStock

    @holdStock.setter
    def holdStock(self, holdStock):
        """Sets the holdStock of this Stocks.


        :param holdStock: The holdStock of this Stocks.  # noqa: E501
        :type holdStock: int
        """

        self._holdStock = holdStock

    @property
    def instrumentName(self):
        """Gets the instrumentName of this Stocks.  # noqa: E501


        :return: The instrumentName of this Stocks.  # noqa: E501
        :rtype: str
        """
        return self._instrumentName

    @instrumentName.setter
    def instrumentName(self, instrumentName):
        """Sets the instrumentName of this Stocks.


        :param instrumentName: The instrumentName of this Stocks.  # noqa: E501
        :type instrumentName: str
        """

        self._instrumentName = instrumentName

    @property
    def multiple(self):
        """Gets the multiple of this Stocks.  # noqa: E501


        :return: The multiple of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._multiple

    @multiple.setter
    def multiple(self, multiple):
        """Sets the multiple of this Stocks.


        :param multiple: The multiple of this Stocks.  # noqa: E501
        :type multiple: int
        """

        self._multiple = multiple

    @property
    def multipleType(self):
        """Gets the multipleType of this Stocks.  # noqa: E501


        :return: The multipleType of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._multipleType

    @multipleType.setter
    def multipleType(self, multipleType):
        """Sets the multipleType of this Stocks.


        :param multipleType: The multipleType of this Stocks.  # noqa: E501
        :type multipleType: int
        """

        self._multipleType = multipleType

    @property
    def mfHairCut(self):
        """Gets the mfHairCut of this Stocks.  # noqa: E501


        :return: The mfHairCut of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._mfHairCut

    @mfHairCut.setter
    def mfHairCut(self, mfHairCut):
        """Sets the mfHairCut of this Stocks.


        :param mfHairCut: The mfHairCut of this Stocks.  # noqa: E501
        :type mfHairCut: int
        """

        self._mfHairCut = mfHairCut

    @property
    def netTrdQtyLot(self):
        """Gets the netTrdQtyLot of this Stocks.  # noqa: E501


        :return: The netTrdQtyLot of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._netTrdQtyLot

    @netTrdQtyLot.setter
    def netTrdQtyLot(self, netTrdQtyLot):
        """Sets the netTrdQtyLot of this Stocks.


        :param netTrdQtyLot: The netTrdQtyLot of this Stocks.  # noqa: E501
        :type netTrdQtyLot: int
        """

        self._netTrdQtyLot = netTrdQtyLot

    @property
    def netTrdValue(self):
        """Gets the netTrdValue of this Stocks.  # noqa: E501


        :return: The netTrdValue of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._netTrdValue

    @netTrdValue.setter
    def netTrdValue(self, netTrdValue):
        """Sets the netTrdValue of this Stocks.


        :param netTrdValue: The netTrdValue of this Stocks.  # noqa: E501
        :type netTrdValue: float
        """

        self._netTrdValue = netTrdValue

    @property
    def openingStockValue(self):
        """Gets the openingStockValue of this Stocks.  # noqa: E501


        :return: The openingStockValue of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._openingStockValue

    @openingStockValue.setter
    def openingStockValue(self, openingStockValue):
        """Sets the openingStockValue of this Stocks.


        :param openingStockValue: The openingStockValue of this Stocks.  # noqa: E501
        :type openingStockValue: float
        """

        self._openingStockValue = openingStockValue

    @property
    def premium(self):
        """Gets the premium of this Stocks.  # noqa: E501


        :return: The premium of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._premium

    @premium.setter
    def premium(self, premium):
        """Sets the premium of this Stocks.


        :param premium: The premium of this Stocks.  # noqa: E501
        :type premium: float
        """

        self._premium = premium

    @property
    def previousMTMTrades(self):
        """Gets the previousMTMTrades of this Stocks.  # noqa: E501


        :return: The previousMTMTrades of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._previousMTMTrades

    @previousMTMTrades.setter
    def previousMTMTrades(self, previousMTMTrades):
        """Sets the previousMTMTrades of this Stocks.


        :param previousMTMTrades: The previousMTMTrades of this Stocks.  # noqa: E501
        :type previousMTMTrades: int
        """

        self._previousMTMTrades = previousMTMTrades

    @property
    def realizedPL(self):
        """Gets the realizedPL of this Stocks.  # noqa: E501


        :return: The realizedPL of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._realizedPL

    @realizedPL.setter
    def realizedPL(self, realizedPL):
        """Sets the realizedPL of this Stocks.


        :param realizedPL: The realizedPL of this Stocks.  # noqa: E501
        :type realizedPL: float
        """

        self._realizedPL = realizedPL

    @property
    def sellOpenQtyLot(self):
        """Gets the sellOpenQtyLot of this Stocks.  # noqa: E501


        :return: The sellOpenQtyLot of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._sellOpenQtyLot

    @sellOpenQtyLot.setter
    def sellOpenQtyLot(self, sellOpenQtyLot):
        """Sets the sellOpenQtyLot of this Stocks.


        :param sellOpenQtyLot: The sellOpenQtyLot of this Stocks.  # noqa: E501
        :type sellOpenQtyLot: int
        """

        self._sellOpenQtyLot = sellOpenQtyLot

    @property
    def sellOpenValue(self):
        """Gets the sellOpenValue of this Stocks.  # noqa: E501


        :return: The sellOpenValue of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._sellOpenValue

    @sellOpenValue.setter
    def sellOpenValue(self, sellOpenValue):
        """Sets the sellOpenValue of this Stocks.


        :param sellOpenValue: The sellOpenValue of this Stocks.  # noqa: E501
        :type sellOpenValue: int
        """

        self._sellOpenValue = sellOpenValue

    @property
    def securityValuation(self):
        """Gets the securityValuation of this Stocks.  # noqa: E501


        :return: The securityValuation of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._securityValuation

    @securityValuation.setter
    def securityValuation(self, securityValuation):
        """Sets the securityValuation of this Stocks.


        :param securityValuation: The securityValuation of this Stocks.  # noqa: E501
        :type securityValuation: int
        """

        self._securityValuation = securityValuation

    @property
    def securityValuationMTF(self):
        """Gets the securityValuationMTF of this Stocks.  # noqa: E501


        :return: The securityValuationMTF of this Stocks.  # noqa: E501
        :rtype: float
        """
        return self._securityValuationMTF

    @securityValuationMTF.setter
    def securityValuationMTF(self, securityValuationMTF):
        """Sets the securityValuationMTF of this Stocks.


        :param securityValuationMTF: The securityValuationMTF of this Stocks.  # noqa: E501
        :type securityValuationMTF: float
        """

        self._securityValuationMTF = securityValuationMTF

    @property
    def stockBalance(self):
        """Gets the stockBalance of this Stocks.  # noqa: E501


        :return: The stockBalance of this Stocks.  # noqa: E501
        :rtype: int
        """
        return self._stockBalance

    @stockBalance.setter
    def stockBalance(self, stockBalance):
        """Sets the stockBalance of this Stocks.


        :param stockBalance: The stockBalance of this Stocks.  # noqa: E501
        :type stockBalance: int
        """

        self._stockBalance = stockBalance

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
        if not isinstance(other, Stocks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Stocks):
            return True

        return self.to_dict() != other.to_dict()
