# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Open(object):
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
        'denominator': 'int',
        'exchange': 'str',
        'exposureMargin': 'int',
        'exposureMarginTotal': 'int',
        'fnoBnstCredit': 'int',
        'fnoPremium': 'int',
        'grossUtilization': 'float',
        'hairCut': 'int',
        'holdStock': 'int',
        'instrumentName': 'str',
        'marginType': 'str',
        'maxCODQty': 'int',
        'multiple': 'int',
        'multipleType': 'int',
        'multiplier': 'int',
        'netTrdQtyLot': 'int',
        'netTrdValue': 'float',
        'normalSqOffQty': 'float',
        'openingStockValue': 'float',
        'premium': 'float',
        'previousMTMTrades': 'float',
        'rbiRefRate': 'int',
        'realizedPL': 'float',
        'sellOpenQtyLot': 'int',
        'sellOpenValue': 'int',
        'spanMargin': 'int',
        'spanMarginTotal': 'float',
        'spreadTotal': 'float',
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
        'denominator': 'denominator',
        'exchange': 'exchange',
        'exposureMargin': 'exposureMargin',
        'exposureMarginTotal': 'exposureMarginTotal',
        'fnoBnstCredit': 'fnoBnstCredit',
        'fnoPremium': 'fnoPremium',
        'grossUtilization': 'grossUtilization',
        'hairCut': 'hairCut',
        'holdStock': 'holdStock',
        'instrumentName': 'instrumentName',
        'marginType': 'marginType',
        'maxCODQty': 'maxCODQty',
        'multiple': 'multiple',
        'multipleType': 'multipleType',
        'multiplier': 'multiplier',
        'netTrdQtyLot': 'netTrdQtyLot',
        'netTrdValue': 'netTrdValue',
        'normalSqOffQty': 'normalSqOffQty',
        'openingStockValue': 'openingStockValue',
        'premium': 'premium',
        'previousMTMTrades': 'previousMTMTrades',
        'rbiRefRate': 'rbiRefRate',
        'realizedPL': 'realizedPL',
        'sellOpenQtyLot': 'sellOpenQtyLot',
        'sellOpenValue': 'sellOpenValue',
        'spanMargin': 'spanMargin',
        'spanMarginTotal': 'spanMarginTotal',
        'spreadTotal': 'spreadTotal',
        'stockBalance': 'stockBalance'
    }

    def __init__(self, instrumentToken=None, normal=None, supermultiple=None, mtf=None, actualMTM=None, actualPNL=None, averageStockPrice=None, bnstCredit=None, buyOpenQtyLot=None, buyOpenValue=None, delStockPrice=None, deliveryStatus=None, denominator=None, exchange=None, exposureMargin=None, exposureMarginTotal=None, fnoBnstCredit=None, fnoPremium=None, grossUtilization=None, hairCut=None, holdStock=None, instrumentName=None, marginType=None, maxCODQty=None, multiple=None, multipleType=None, multiplier=None, netTrdQtyLot=None, netTrdValue=None, normalSqOffQty=None, openingStockValue=None, premium=None, previousMTMTrades=None, rbiRefRate=None, realizedPL=None, sellOpenQtyLot=None, sellOpenValue=None, spanMargin=None, spanMarginTotal=None, spreadTotal=None, stockBalance=None, local_vars_configuration=None):  # noqa: E501
        """Open - a model defined in OpenAPI"""  # noqa: E501
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
        self._denominator = None
        self._exchange = None
        self._exposureMargin = None
        self._exposureMarginTotal = None
        self._fnoBnstCredit = None
        self._fnoPremium = None
        self._grossUtilization = None
        self._hairCut = None
        self._holdStock = None
        self._instrumentName = None
        self._marginType = None
        self._maxCODQty = None
        self._multiple = None
        self._multipleType = None
        self._multiplier = None
        self._netTrdQtyLot = None
        self._netTrdValue = None
        self._normalSqOffQty = None
        self._openingStockValue = None
        self._premium = None
        self._previousMTMTrades = None
        self._rbiRefRate = None
        self._realizedPL = None
        self._sellOpenQtyLot = None
        self._sellOpenValue = None
        self._spanMargin = None
        self._spanMarginTotal = None
        self._spreadTotal = None
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
        if denominator is not None:
            self.denominator = denominator
        if exchange is not None:
            self.exchange = exchange
        if exposureMargin is not None:
            self.exposureMargin = exposureMargin
        if exposureMarginTotal is not None:
            self.exposureMarginTotal = exposureMarginTotal
        if fnoBnstCredit is not None:
            self.fnoBnstCredit = fnoBnstCredit
        if fnoPremium is not None:
            self.fnoPremium = fnoPremium
        if grossUtilization is not None:
            self.grossUtilization = grossUtilization
        if hairCut is not None:
            self.hairCut = hairCut
        if holdStock is not None:
            self.holdStock = holdStock
        if instrumentName is not None:
            self.instrumentName = instrumentName
        if marginType is not None:
            self.marginType = marginType
        if maxCODQty is not None:
            self.maxCODQty = maxCODQty
        if multiple is not None:
            self.multiple = multiple
        if multipleType is not None:
            self.multipleType = multipleType
        if multiplier is not None:
            self.multiplier = multiplier
        if netTrdQtyLot is not None:
            self.netTrdQtyLot = netTrdQtyLot
        if netTrdValue is not None:
            self.netTrdValue = netTrdValue
        if normalSqOffQty is not None:
            self.normalSqOffQty = normalSqOffQty
        if openingStockValue is not None:
            self.openingStockValue = openingStockValue
        if premium is not None:
            self.premium = premium
        if previousMTMTrades is not None:
            self.previousMTMTrades = previousMTMTrades
        if rbiRefRate is not None:
            self.rbiRefRate = rbiRefRate
        if realizedPL is not None:
            self.realizedPL = realizedPL
        if sellOpenQtyLot is not None:
            self.sellOpenQtyLot = sellOpenQtyLot
        if sellOpenValue is not None:
            self.sellOpenValue = sellOpenValue
        if spanMargin is not None:
            self.spanMargin = spanMargin
        if spanMarginTotal is not None:
            self.spanMarginTotal = spanMarginTotal
        if spreadTotal is not None:
            self.spreadTotal = spreadTotal
        if stockBalance is not None:
            self.stockBalance = stockBalance

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this Open.  # noqa: E501


        :return: The instrumentToken of this Open.  # noqa: E501
        :rtype: int
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this Open.


        :param instrumentToken: The instrumentToken of this Open.  # noqa: E501
        :type instrumentToken: int
        """

        self._instrumentToken = instrumentToken

    @property
    def normal(self):
        """Gets the normal of this Open.  # noqa: E501

        Order Status  # noqa: E501

        :return: The normal of this Open.  # noqa: E501
        :rtype: float
        """
        return self._normal

    @normal.setter
    def normal(self, normal):
        """Sets the normal of this Open.

        Order Status  # noqa: E501

        :param normal: The normal of this Open.  # noqa: E501
        :type normal: float
        """

        self._normal = normal

    @property
    def supermultiple(self):
        """Gets the supermultiple of this Open.  # noqa: E501

        Order Status  # noqa: E501

        :return: The supermultiple of this Open.  # noqa: E501
        :rtype: float
        """
        return self._supermultiple

    @supermultiple.setter
    def supermultiple(self, supermultiple):
        """Sets the supermultiple of this Open.

        Order Status  # noqa: E501

        :param supermultiple: The supermultiple of this Open.  # noqa: E501
        :type supermultiple: float
        """

        self._supermultiple = supermultiple

    @property
    def mtf(self):
        """Gets the mtf of this Open.  # noqa: E501

        Order Status  # noqa: E501

        :return: The mtf of this Open.  # noqa: E501
        :rtype: float
        """
        return self._mtf

    @mtf.setter
    def mtf(self, mtf):
        """Sets the mtf of this Open.

        Order Status  # noqa: E501

        :param mtf: The mtf of this Open.  # noqa: E501
        :type mtf: float
        """

        self._mtf = mtf

    @property
    def actualMTM(self):
        """Gets the actualMTM of this Open.  # noqa: E501


        :return: The actualMTM of this Open.  # noqa: E501
        :rtype: float
        """
        return self._actualMTM

    @actualMTM.setter
    def actualMTM(self, actualMTM):
        """Sets the actualMTM of this Open.


        :param actualMTM: The actualMTM of this Open.  # noqa: E501
        :type actualMTM: float
        """

        self._actualMTM = actualMTM

    @property
    def actualPNL(self):
        """Gets the actualPNL of this Open.  # noqa: E501


        :return: The actualPNL of this Open.  # noqa: E501
        :rtype: float
        """
        return self._actualPNL

    @actualPNL.setter
    def actualPNL(self, actualPNL):
        """Sets the actualPNL of this Open.


        :param actualPNL: The actualPNL of this Open.  # noqa: E501
        :type actualPNL: float
        """

        self._actualPNL = actualPNL

    @property
    def averageStockPrice(self):
        """Gets the averageStockPrice of this Open.  # noqa: E501


        :return: The averageStockPrice of this Open.  # noqa: E501
        :rtype: float
        """
        return self._averageStockPrice

    @averageStockPrice.setter
    def averageStockPrice(self, averageStockPrice):
        """Sets the averageStockPrice of this Open.


        :param averageStockPrice: The averageStockPrice of this Open.  # noqa: E501
        :type averageStockPrice: float
        """

        self._averageStockPrice = averageStockPrice

    @property
    def bnstCredit(self):
        """Gets the bnstCredit of this Open.  # noqa: E501


        :return: The bnstCredit of this Open.  # noqa: E501
        :rtype: float
        """
        return self._bnstCredit

    @bnstCredit.setter
    def bnstCredit(self, bnstCredit):
        """Sets the bnstCredit of this Open.


        :param bnstCredit: The bnstCredit of this Open.  # noqa: E501
        :type bnstCredit: float
        """

        self._bnstCredit = bnstCredit

    @property
    def buyOpenQtyLot(self):
        """Gets the buyOpenQtyLot of this Open.  # noqa: E501


        :return: The buyOpenQtyLot of this Open.  # noqa: E501
        :rtype: int
        """
        return self._buyOpenQtyLot

    @buyOpenQtyLot.setter
    def buyOpenQtyLot(self, buyOpenQtyLot):
        """Sets the buyOpenQtyLot of this Open.


        :param buyOpenQtyLot: The buyOpenQtyLot of this Open.  # noqa: E501
        :type buyOpenQtyLot: int
        """

        self._buyOpenQtyLot = buyOpenQtyLot

    @property
    def buyOpenValue(self):
        """Gets the buyOpenValue of this Open.  # noqa: E501


        :return: The buyOpenValue of this Open.  # noqa: E501
        :rtype: float
        """
        return self._buyOpenValue

    @buyOpenValue.setter
    def buyOpenValue(self, buyOpenValue):
        """Sets the buyOpenValue of this Open.


        :param buyOpenValue: The buyOpenValue of this Open.  # noqa: E501
        :type buyOpenValue: float
        """

        self._buyOpenValue = buyOpenValue

    @property
    def delStockPrice(self):
        """Gets the delStockPrice of this Open.  # noqa: E501


        :return: The delStockPrice of this Open.  # noqa: E501
        :rtype: float
        """
        return self._delStockPrice

    @delStockPrice.setter
    def delStockPrice(self, delStockPrice):
        """Sets the delStockPrice of this Open.


        :param delStockPrice: The delStockPrice of this Open.  # noqa: E501
        :type delStockPrice: float
        """

        self._delStockPrice = delStockPrice

    @property
    def deliveryStatus(self):
        """Gets the deliveryStatus of this Open.  # noqa: E501


        :return: The deliveryStatus of this Open.  # noqa: E501
        :rtype: int
        """
        return self._deliveryStatus

    @deliveryStatus.setter
    def deliveryStatus(self, deliveryStatus):
        """Sets the deliveryStatus of this Open.


        :param deliveryStatus: The deliveryStatus of this Open.  # noqa: E501
        :type deliveryStatus: int
        """

        self._deliveryStatus = deliveryStatus

    @property
    def denominator(self):
        """Gets the denominator of this Open.  # noqa: E501


        :return: The denominator of this Open.  # noqa: E501
        :rtype: int
        """
        return self._denominator

    @denominator.setter
    def denominator(self, denominator):
        """Sets the denominator of this Open.


        :param denominator: The denominator of this Open.  # noqa: E501
        :type denominator: int
        """

        self._denominator = denominator

    @property
    def exchange(self):
        """Gets the exchange of this Open.  # noqa: E501


        :return: The exchange of this Open.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this Open.


        :param exchange: The exchange of this Open.  # noqa: E501
        :type exchange: str
        """

        self._exchange = exchange

    @property
    def exposureMargin(self):
        """Gets the exposureMargin of this Open.  # noqa: E501


        :return: The exposureMargin of this Open.  # noqa: E501
        :rtype: int
        """
        return self._exposureMargin

    @exposureMargin.setter
    def exposureMargin(self, exposureMargin):
        """Sets the exposureMargin of this Open.


        :param exposureMargin: The exposureMargin of this Open.  # noqa: E501
        :type exposureMargin: int
        """

        self._exposureMargin = exposureMargin

    @property
    def exposureMarginTotal(self):
        """Gets the exposureMarginTotal of this Open.  # noqa: E501


        :return: The exposureMarginTotal of this Open.  # noqa: E501
        :rtype: int
        """
        return self._exposureMarginTotal

    @exposureMarginTotal.setter
    def exposureMarginTotal(self, exposureMarginTotal):
        """Sets the exposureMarginTotal of this Open.


        :param exposureMarginTotal: The exposureMarginTotal of this Open.  # noqa: E501
        :type exposureMarginTotal: int
        """

        self._exposureMarginTotal = exposureMarginTotal

    @property
    def fnoBnstCredit(self):
        """Gets the fnoBnstCredit of this Open.  # noqa: E501


        :return: The fnoBnstCredit of this Open.  # noqa: E501
        :rtype: int
        """
        return self._fnoBnstCredit

    @fnoBnstCredit.setter
    def fnoBnstCredit(self, fnoBnstCredit):
        """Sets the fnoBnstCredit of this Open.


        :param fnoBnstCredit: The fnoBnstCredit of this Open.  # noqa: E501
        :type fnoBnstCredit: int
        """

        self._fnoBnstCredit = fnoBnstCredit

    @property
    def fnoPremium(self):
        """Gets the fnoPremium of this Open.  # noqa: E501


        :return: The fnoPremium of this Open.  # noqa: E501
        :rtype: int
        """
        return self._fnoPremium

    @fnoPremium.setter
    def fnoPremium(self, fnoPremium):
        """Sets the fnoPremium of this Open.


        :param fnoPremium: The fnoPremium of this Open.  # noqa: E501
        :type fnoPremium: int
        """

        self._fnoPremium = fnoPremium

    @property
    def grossUtilization(self):
        """Gets the grossUtilization of this Open.  # noqa: E501


        :return: The grossUtilization of this Open.  # noqa: E501
        :rtype: float
        """
        return self._grossUtilization

    @grossUtilization.setter
    def grossUtilization(self, grossUtilization):
        """Sets the grossUtilization of this Open.


        :param grossUtilization: The grossUtilization of this Open.  # noqa: E501
        :type grossUtilization: float
        """

        self._grossUtilization = grossUtilization

    @property
    def hairCut(self):
        """Gets the hairCut of this Open.  # noqa: E501


        :return: The hairCut of this Open.  # noqa: E501
        :rtype: int
        """
        return self._hairCut

    @hairCut.setter
    def hairCut(self, hairCut):
        """Sets the hairCut of this Open.


        :param hairCut: The hairCut of this Open.  # noqa: E501
        :type hairCut: int
        """

        self._hairCut = hairCut

    @property
    def holdStock(self):
        """Gets the holdStock of this Open.  # noqa: E501


        :return: The holdStock of this Open.  # noqa: E501
        :rtype: int
        """
        return self._holdStock

    @holdStock.setter
    def holdStock(self, holdStock):
        """Sets the holdStock of this Open.


        :param holdStock: The holdStock of this Open.  # noqa: E501
        :type holdStock: int
        """

        self._holdStock = holdStock

    @property
    def instrumentName(self):
        """Gets the instrumentName of this Open.  # noqa: E501


        :return: The instrumentName of this Open.  # noqa: E501
        :rtype: str
        """
        return self._instrumentName

    @instrumentName.setter
    def instrumentName(self, instrumentName):
        """Sets the instrumentName of this Open.


        :param instrumentName: The instrumentName of this Open.  # noqa: E501
        :type instrumentName: str
        """

        self._instrumentName = instrumentName

    @property
    def marginType(self):
        """Gets the marginType of this Open.  # noqa: E501


        :return: The marginType of this Open.  # noqa: E501
        :rtype: str
        """
        return self._marginType

    @marginType.setter
    def marginType(self, marginType):
        """Sets the marginType of this Open.


        :param marginType: The marginType of this Open.  # noqa: E501
        :type marginType: str
        """

        self._marginType = marginType

    @property
    def maxCODQty(self):
        """Gets the maxCODQty of this Open.  # noqa: E501


        :return: The maxCODQty of this Open.  # noqa: E501
        :rtype: int
        """
        return self._maxCODQty

    @maxCODQty.setter
    def maxCODQty(self, maxCODQty):
        """Sets the maxCODQty of this Open.


        :param maxCODQty: The maxCODQty of this Open.  # noqa: E501
        :type maxCODQty: int
        """

        self._maxCODQty = maxCODQty

    @property
    def multiple(self):
        """Gets the multiple of this Open.  # noqa: E501


        :return: The multiple of this Open.  # noqa: E501
        :rtype: int
        """
        return self._multiple

    @multiple.setter
    def multiple(self, multiple):
        """Sets the multiple of this Open.


        :param multiple: The multiple of this Open.  # noqa: E501
        :type multiple: int
        """

        self._multiple = multiple

    @property
    def multipleType(self):
        """Gets the multipleType of this Open.  # noqa: E501


        :return: The multipleType of this Open.  # noqa: E501
        :rtype: int
        """
        return self._multipleType

    @multipleType.setter
    def multipleType(self, multipleType):
        """Sets the multipleType of this Open.


        :param multipleType: The multipleType of this Open.  # noqa: E501
        :type multipleType: int
        """

        self._multipleType = multipleType

    @property
    def multiplier(self):
        """Gets the multiplier of this Open.  # noqa: E501


        :return: The multiplier of this Open.  # noqa: E501
        :rtype: int
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this Open.


        :param multiplier: The multiplier of this Open.  # noqa: E501
        :type multiplier: int
        """

        self._multiplier = multiplier

    @property
    def netTrdQtyLot(self):
        """Gets the netTrdQtyLot of this Open.  # noqa: E501


        :return: The netTrdQtyLot of this Open.  # noqa: E501
        :rtype: int
        """
        return self._netTrdQtyLot

    @netTrdQtyLot.setter
    def netTrdQtyLot(self, netTrdQtyLot):
        """Sets the netTrdQtyLot of this Open.


        :param netTrdQtyLot: The netTrdQtyLot of this Open.  # noqa: E501
        :type netTrdQtyLot: int
        """

        self._netTrdQtyLot = netTrdQtyLot

    @property
    def netTrdValue(self):
        """Gets the netTrdValue of this Open.  # noqa: E501


        :return: The netTrdValue of this Open.  # noqa: E501
        :rtype: float
        """
        return self._netTrdValue

    @netTrdValue.setter
    def netTrdValue(self, netTrdValue):
        """Sets the netTrdValue of this Open.


        :param netTrdValue: The netTrdValue of this Open.  # noqa: E501
        :type netTrdValue: float
        """

        self._netTrdValue = netTrdValue

    @property
    def normalSqOffQty(self):
        """Gets the normalSqOffQty of this Open.  # noqa: E501


        :return: The normalSqOffQty of this Open.  # noqa: E501
        :rtype: float
        """
        return self._normalSqOffQty

    @normalSqOffQty.setter
    def normalSqOffQty(self, normalSqOffQty):
        """Sets the normalSqOffQty of this Open.


        :param normalSqOffQty: The normalSqOffQty of this Open.  # noqa: E501
        :type normalSqOffQty: float
        """

        self._normalSqOffQty = normalSqOffQty

    @property
    def openingStockValue(self):
        """Gets the openingStockValue of this Open.  # noqa: E501


        :return: The openingStockValue of this Open.  # noqa: E501
        :rtype: float
        """
        return self._openingStockValue

    @openingStockValue.setter
    def openingStockValue(self, openingStockValue):
        """Sets the openingStockValue of this Open.


        :param openingStockValue: The openingStockValue of this Open.  # noqa: E501
        :type openingStockValue: float
        """

        self._openingStockValue = openingStockValue

    @property
    def premium(self):
        """Gets the premium of this Open.  # noqa: E501


        :return: The premium of this Open.  # noqa: E501
        :rtype: float
        """
        return self._premium

    @premium.setter
    def premium(self, premium):
        """Sets the premium of this Open.


        :param premium: The premium of this Open.  # noqa: E501
        :type premium: float
        """

        self._premium = premium

    @property
    def previousMTMTrades(self):
        """Gets the previousMTMTrades of this Open.  # noqa: E501


        :return: The previousMTMTrades of this Open.  # noqa: E501
        :rtype: float
        """
        return self._previousMTMTrades

    @previousMTMTrades.setter
    def previousMTMTrades(self, previousMTMTrades):
        """Sets the previousMTMTrades of this Open.


        :param previousMTMTrades: The previousMTMTrades of this Open.  # noqa: E501
        :type previousMTMTrades: float
        """

        self._previousMTMTrades = previousMTMTrades

    @property
    def rbiRefRate(self):
        """Gets the rbiRefRate of this Open.  # noqa: E501


        :return: The rbiRefRate of this Open.  # noqa: E501
        :rtype: int
        """
        return self._rbiRefRate

    @rbiRefRate.setter
    def rbiRefRate(self, rbiRefRate):
        """Sets the rbiRefRate of this Open.


        :param rbiRefRate: The rbiRefRate of this Open.  # noqa: E501
        :type rbiRefRate: int
        """

        self._rbiRefRate = rbiRefRate

    @property
    def realizedPL(self):
        """Gets the realizedPL of this Open.  # noqa: E501


        :return: The realizedPL of this Open.  # noqa: E501
        :rtype: float
        """
        return self._realizedPL

    @realizedPL.setter
    def realizedPL(self, realizedPL):
        """Sets the realizedPL of this Open.


        :param realizedPL: The realizedPL of this Open.  # noqa: E501
        :type realizedPL: float
        """

        self._realizedPL = realizedPL

    @property
    def sellOpenQtyLot(self):
        """Gets the sellOpenQtyLot of this Open.  # noqa: E501


        :return: The sellOpenQtyLot of this Open.  # noqa: E501
        :rtype: int
        """
        return self._sellOpenQtyLot

    @sellOpenQtyLot.setter
    def sellOpenQtyLot(self, sellOpenQtyLot):
        """Sets the sellOpenQtyLot of this Open.


        :param sellOpenQtyLot: The sellOpenQtyLot of this Open.  # noqa: E501
        :type sellOpenQtyLot: int
        """

        self._sellOpenQtyLot = sellOpenQtyLot

    @property
    def sellOpenValue(self):
        """Gets the sellOpenValue of this Open.  # noqa: E501


        :return: The sellOpenValue of this Open.  # noqa: E501
        :rtype: int
        """
        return self._sellOpenValue

    @sellOpenValue.setter
    def sellOpenValue(self, sellOpenValue):
        """Sets the sellOpenValue of this Open.


        :param sellOpenValue: The sellOpenValue of this Open.  # noqa: E501
        :type sellOpenValue: int
        """

        self._sellOpenValue = sellOpenValue

    @property
    def spanMargin(self):
        """Gets the spanMargin of this Open.  # noqa: E501


        :return: The spanMargin of this Open.  # noqa: E501
        :rtype: int
        """
        return self._spanMargin

    @spanMargin.setter
    def spanMargin(self, spanMargin):
        """Sets the spanMargin of this Open.


        :param spanMargin: The spanMargin of this Open.  # noqa: E501
        :type spanMargin: int
        """

        self._spanMargin = spanMargin

    @property
    def spanMarginTotal(self):
        """Gets the spanMarginTotal of this Open.  # noqa: E501


        :return: The spanMarginTotal of this Open.  # noqa: E501
        :rtype: float
        """
        return self._spanMarginTotal

    @spanMarginTotal.setter
    def spanMarginTotal(self, spanMarginTotal):
        """Sets the spanMarginTotal of this Open.


        :param spanMarginTotal: The spanMarginTotal of this Open.  # noqa: E501
        :type spanMarginTotal: float
        """

        self._spanMarginTotal = spanMarginTotal

    @property
    def spreadTotal(self):
        """Gets the spreadTotal of this Open.  # noqa: E501


        :return: The spreadTotal of this Open.  # noqa: E501
        :rtype: float
        """
        return self._spreadTotal

    @spreadTotal.setter
    def spreadTotal(self, spreadTotal):
        """Sets the spreadTotal of this Open.


        :param spreadTotal: The spreadTotal of this Open.  # noqa: E501
        :type spreadTotal: float
        """

        self._spreadTotal = spreadTotal

    @property
    def stockBalance(self):
        """Gets the stockBalance of this Open.  # noqa: E501


        :return: The stockBalance of this Open.  # noqa: E501
        :rtype: int
        """
        return self._stockBalance

    @stockBalance.setter
    def stockBalance(self, stockBalance):
        """Sets the stockBalance of this Open.


        :param stockBalance: The stockBalance of this Open.  # noqa: E501
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
        if not isinstance(other, Open):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Open):
            return True

        return self.to_dict() != other.to_dict()
