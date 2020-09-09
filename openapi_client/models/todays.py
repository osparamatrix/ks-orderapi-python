# coding: utf-8

import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Todays(object):
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
        'actualNetTrdValue': 'float',
        'averageStockPrice': 'float',
        'buyOpenQtyLot': 'int',
        'buyOpenVal': 'float',
        'buyTradedQtyLot': 'int',
        'buyTradedVal': 'float',
        'buyTrdAvg': 'float',
        'deliveryStatus': 'int',
        'denominator': 'int',
        'exchange': 'str',
        'exposureMargin': 'int',
        'exposureMarginTotal': 'int',
        'grossUtilization': 'float',
        'instrumentName': 'str',
        'lastPrice': 'float',
        'marginType': 'str',
        'maxCODQty': 'int',
        'multiplier': 'int',
        'netTrdQtyLot': 'int',
        'netTrdValue': 'float',
        'normalSqOffQty': 'float',
        'premium': 'float',
        'rbiRefRate': 'int',
        'realizedPL': 'float',
        'sellOpenQtyLot': 'int',
        'sellOpenVal': 'int',
        'sellTradedQtyLot': 'int',
        'sellTradedVal': 'float',
        'sellTrdAvg': 'float',
        'spanMargin': 'int',
        'spanMarginTotal': 'float',
        'spreadTotal': 'float',
        'totalStock': 'int'
    }

    attribute_map = {
        'instrumentToken': 'instrumentToken',
        'normal': 'normal',
        'supermultiple': 'supermultiple',
        'mtf': 'mtf',
        'actualNetTrdValue': 'actualNetTrdValue',
        'averageStockPrice': 'averageStockPrice',
        'buyOpenQtyLot': 'buyOpenQtyLot',
        'buyOpenVal': 'buyOpenVal',
        'buyTradedQtyLot': 'buyTradedQtyLot',
        'buyTradedVal': 'buyTradedVal',
        'buyTrdAvg': 'buyTrdAvg',
        'deliveryStatus': 'deliveryStatus',
        'denominator': 'denominator',
        'exchange': 'exchange',
        'exposureMargin': 'exposureMargin',
        'exposureMarginTotal': 'exposureMarginTotal',
        'grossUtilization': 'grossUtilization',
        'instrumentName': 'instrumentName',
        'lastPrice': 'lastPrice',
        'marginType': 'marginType',
        'maxCODQty': 'maxCODQty',
        'multiplier': 'multiplier',
        'netTrdQtyLot': 'netTrdQtyLot',
        'netTrdValue': 'netTrdValue',
        'normalSqOffQty': 'normalSqOffQty',
        'premium': 'premium',
        'rbiRefRate': 'rbiRefRate',
        'realizedPL': 'realizedPL',
        'sellOpenQtyLot': 'sellOpenQtyLot',
        'sellOpenVal': 'sellOpenVal',
        'sellTradedQtyLot': 'sellTradedQtyLot',
        'sellTradedVal': 'sellTradedVal',
        'sellTrdAvg': 'sellTrdAvg',
        'spanMargin': 'spanMargin',
        'spanMarginTotal': 'spanMarginTotal',
        'spreadTotal': 'spreadTotal',
        'totalStock': 'totalStock'
    }

    def __init__(self, instrumentToken=None, normal=None, supermultiple=None, mtf=None, actualNetTrdValue=None, averageStockPrice=None, buyOpenQtyLot=None, buyOpenVal=None, buyTradedQtyLot=None, buyTradedVal=None, buyTrdAvg=None, deliveryStatus=None, denominator=None, exchange=None, exposureMargin=None, exposureMarginTotal=None, grossUtilization=None, instrumentName=None, lastPrice=None, marginType=None, maxCODQty=None, multiplier=None, netTrdQtyLot=None, netTrdValue=None, normalSqOffQty=None, premium=None, rbiRefRate=None, realizedPL=None, sellOpenQtyLot=None, sellOpenVal=None, sellTradedQtyLot=None, sellTradedVal=None, sellTrdAvg=None, spanMargin=None, spanMarginTotal=None, spreadTotal=None, totalStock=None, local_vars_configuration=None):  # noqa: E501
        """Todays - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrumentToken = None
        self._normal = None
        self._supermultiple = None
        self._mtf = None
        self._actualNetTrdValue = None
        self._averageStockPrice = None
        self._buyOpenQtyLot = None
        self._buyOpenVal = None
        self._buyTradedQtyLot = None
        self._buyTradedVal = None
        self._buyTrdAvg = None
        self._deliveryStatus = None
        self._denominator = None
        self._exchange = None
        self._exposureMargin = None
        self._exposureMarginTotal = None
        self._grossUtilization = None
        self._instrumentName = None
        self._lastPrice = None
        self._marginType = None
        self._maxCODQty = None
        self._multiplier = None
        self._netTrdQtyLot = None
        self._netTrdValue = None
        self._normalSqOffQty = None
        self._premium = None
        self._rbiRefRate = None
        self._realizedPL = None
        self._sellOpenQtyLot = None
        self._sellOpenVal = None
        self._sellTradedQtyLot = None
        self._sellTradedVal = None
        self._sellTrdAvg = None
        self._spanMargin = None
        self._spanMarginTotal = None
        self._spreadTotal = None
        self._totalStock = None
        self.discriminator = None

        if instrumentToken is not None:
            self.instrumentToken = instrumentToken
        if normal is not None:
            self.normal = normal
        if supermultiple is not None:
            self.supermultiple = supermultiple
        if mtf is not None:
            self.mtf = mtf
        if actualNetTrdValue is not None:
            self.actualNetTrdValue = actualNetTrdValue
        if averageStockPrice is not None:
            self.averageStockPrice = averageStockPrice
        if buyOpenQtyLot is not None:
            self.buyOpenQtyLot = buyOpenQtyLot
        if buyOpenVal is not None:
            self.buyOpenVal = buyOpenVal
        if buyTradedQtyLot is not None:
            self.buyTradedQtyLot = buyTradedQtyLot
        if buyTradedVal is not None:
            self.buyTradedVal = buyTradedVal
        if buyTrdAvg is not None:
            self.buyTrdAvg = buyTrdAvg
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
        if grossUtilization is not None:
            self.grossUtilization = grossUtilization
        if instrumentName is not None:
            self.instrumentName = instrumentName
        if lastPrice is not None:
            self.lastPrice = lastPrice
        if marginType is not None:
            self.marginType = marginType
        if maxCODQty is not None:
            self.maxCODQty = maxCODQty
        if multiplier is not None:
            self.multiplier = multiplier
        if netTrdQtyLot is not None:
            self.netTrdQtyLot = netTrdQtyLot
        if netTrdValue is not None:
            self.netTrdValue = netTrdValue
        if normalSqOffQty is not None:
            self.normalSqOffQty = normalSqOffQty
        if premium is not None:
            self.premium = premium
        if rbiRefRate is not None:
            self.rbiRefRate = rbiRefRate
        if realizedPL is not None:
            self.realizedPL = realizedPL
        if sellOpenQtyLot is not None:
            self.sellOpenQtyLot = sellOpenQtyLot
        if sellOpenVal is not None:
            self.sellOpenVal = sellOpenVal
        if sellTradedQtyLot is not None:
            self.sellTradedQtyLot = sellTradedQtyLot
        if sellTradedVal is not None:
            self.sellTradedVal = sellTradedVal
        if sellTrdAvg is not None:
            self.sellTrdAvg = sellTrdAvg
        if spanMargin is not None:
            self.spanMargin = spanMargin
        if spanMarginTotal is not None:
            self.spanMarginTotal = spanMarginTotal
        if spreadTotal is not None:
            self.spreadTotal = spreadTotal
        if totalStock is not None:
            self.totalStock = totalStock

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this Todays.  # noqa: E501


        :return: The instrumentToken of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this Todays.


        :param instrumentToken: The instrumentToken of this Todays.  # noqa: E501
        :type instrumentToken: int
        """

        self._instrumentToken = instrumentToken

    @property
    def normal(self):
        """Gets the normal of this Todays.  # noqa: E501

        Order Status  # noqa: E501

        :return: The normal of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._normal

    @normal.setter
    def normal(self, normal):
        """Sets the normal of this Todays.

        Order Status  # noqa: E501

        :param normal: The normal of this Todays.  # noqa: E501
        :type normal: float
        """

        self._normal = normal

    @property
    def supermultiple(self):
        """Gets the supermultiple of this Todays.  # noqa: E501

        Order Status  # noqa: E501

        :return: The supermultiple of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._supermultiple

    @supermultiple.setter
    def supermultiple(self, supermultiple):
        """Sets the supermultiple of this Todays.

        Order Status  # noqa: E501

        :param supermultiple: The supermultiple of this Todays.  # noqa: E501
        :type supermultiple: float
        """

        self._supermultiple = supermultiple

    @property
    def mtf(self):
        """Gets the mtf of this Todays.  # noqa: E501

        Order Status  # noqa: E501

        :return: The mtf of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._mtf

    @mtf.setter
    def mtf(self, mtf):
        """Sets the mtf of this Todays.

        Order Status  # noqa: E501

        :param mtf: The mtf of this Todays.  # noqa: E501
        :type mtf: float
        """

        self._mtf = mtf

    @property
    def actualNetTrdValue(self):
        """Gets the actualNetTrdValue of this Todays.  # noqa: E501


        :return: The actualNetTrdValue of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._actualNetTrdValue

    @actualNetTrdValue.setter
    def actualNetTrdValue(self, actualNetTrdValue):
        """Sets the actualNetTrdValue of this Todays.


        :param actualNetTrdValue: The actualNetTrdValue of this Todays.  # noqa: E501
        :type actualNetTrdValue: float
        """

        self._actualNetTrdValue = actualNetTrdValue

    @property
    def averageStockPrice(self):
        """Gets the averageStockPrice of this Todays.  # noqa: E501


        :return: The averageStockPrice of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._averageStockPrice

    @averageStockPrice.setter
    def averageStockPrice(self, averageStockPrice):
        """Sets the averageStockPrice of this Todays.


        :param averageStockPrice: The averageStockPrice of this Todays.  # noqa: E501
        :type averageStockPrice: float
        """

        self._averageStockPrice = averageStockPrice

    @property
    def buyOpenQtyLot(self):
        """Gets the buyOpenQtyLot of this Todays.  # noqa: E501


        :return: The buyOpenQtyLot of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._buyOpenQtyLot

    @buyOpenQtyLot.setter
    def buyOpenQtyLot(self, buyOpenQtyLot):
        """Sets the buyOpenQtyLot of this Todays.


        :param buyOpenQtyLot: The buyOpenQtyLot of this Todays.  # noqa: E501
        :type buyOpenQtyLot: int
        """

        self._buyOpenQtyLot = buyOpenQtyLot

    @property
    def buyOpenVal(self):
        """Gets the buyOpenVal of this Todays.  # noqa: E501


        :return: The buyOpenVal of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._buyOpenVal

    @buyOpenVal.setter
    def buyOpenVal(self, buyOpenVal):
        """Sets the buyOpenVal of this Todays.


        :param buyOpenVal: The buyOpenVal of this Todays.  # noqa: E501
        :type buyOpenVal: float
        """

        self._buyOpenVal = buyOpenVal

    @property
    def buyTradedQtyLot(self):
        """Gets the buyTradedQtyLot of this Todays.  # noqa: E501


        :return: The buyTradedQtyLot of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._buyTradedQtyLot

    @buyTradedQtyLot.setter
    def buyTradedQtyLot(self, buyTradedQtyLot):
        """Sets the buyTradedQtyLot of this Todays.


        :param buyTradedQtyLot: The buyTradedQtyLot of this Todays.  # noqa: E501
        :type buyTradedQtyLot: int
        """

        self._buyTradedQtyLot = buyTradedQtyLot

    @property
    def buyTradedVal(self):
        """Gets the buyTradedVal of this Todays.  # noqa: E501


        :return: The buyTradedVal of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._buyTradedVal

    @buyTradedVal.setter
    def buyTradedVal(self, buyTradedVal):
        """Sets the buyTradedVal of this Todays.


        :param buyTradedVal: The buyTradedVal of this Todays.  # noqa: E501
        :type buyTradedVal: float
        """

        self._buyTradedVal = buyTradedVal

    @property
    def buyTrdAvg(self):
        """Gets the buyTrdAvg of this Todays.  # noqa: E501


        :return: The buyTrdAvg of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._buyTrdAvg

    @buyTrdAvg.setter
    def buyTrdAvg(self, buyTrdAvg):
        """Sets the buyTrdAvg of this Todays.


        :param buyTrdAvg: The buyTrdAvg of this Todays.  # noqa: E501
        :type buyTrdAvg: float
        """

        self._buyTrdAvg = buyTrdAvg

    @property
    def deliveryStatus(self):
        """Gets the deliveryStatus of this Todays.  # noqa: E501


        :return: The deliveryStatus of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._deliveryStatus

    @deliveryStatus.setter
    def deliveryStatus(self, deliveryStatus):
        """Sets the deliveryStatus of this Todays.


        :param deliveryStatus: The deliveryStatus of this Todays.  # noqa: E501
        :type deliveryStatus: int
        """

        self._deliveryStatus = deliveryStatus

    @property
    def denominator(self):
        """Gets the denominator of this Todays.  # noqa: E501


        :return: The denominator of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._denominator

    @denominator.setter
    def denominator(self, denominator):
        """Sets the denominator of this Todays.


        :param denominator: The denominator of this Todays.  # noqa: E501
        :type denominator: int
        """

        self._denominator = denominator

    @property
    def exchange(self):
        """Gets the exchange of this Todays.  # noqa: E501


        :return: The exchange of this Todays.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this Todays.


        :param exchange: The exchange of this Todays.  # noqa: E501
        :type exchange: str
        """

        self._exchange = exchange

    @property
    def exposureMargin(self):
        """Gets the exposureMargin of this Todays.  # noqa: E501


        :return: The exposureMargin of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._exposureMargin

    @exposureMargin.setter
    def exposureMargin(self, exposureMargin):
        """Sets the exposureMargin of this Todays.


        :param exposureMargin: The exposureMargin of this Todays.  # noqa: E501
        :type exposureMargin: int
        """

        self._exposureMargin = exposureMargin

    @property
    def exposureMarginTotal(self):
        """Gets the exposureMarginTotal of this Todays.  # noqa: E501


        :return: The exposureMarginTotal of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._exposureMarginTotal

    @exposureMarginTotal.setter
    def exposureMarginTotal(self, exposureMarginTotal):
        """Sets the exposureMarginTotal of this Todays.


        :param exposureMarginTotal: The exposureMarginTotal of this Todays.  # noqa: E501
        :type exposureMarginTotal: int
        """

        self._exposureMarginTotal = exposureMarginTotal

    @property
    def grossUtilization(self):
        """Gets the grossUtilization of this Todays.  # noqa: E501


        :return: The grossUtilization of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._grossUtilization

    @grossUtilization.setter
    def grossUtilization(self, grossUtilization):
        """Sets the grossUtilization of this Todays.


        :param grossUtilization: The grossUtilization of this Todays.  # noqa: E501
        :type grossUtilization: float
        """

        self._grossUtilization = grossUtilization

    @property
    def instrumentName(self):
        """Gets the instrumentName of this Todays.  # noqa: E501


        :return: The instrumentName of this Todays.  # noqa: E501
        :rtype: str
        """
        return self._instrumentName

    @instrumentName.setter
    def instrumentName(self, instrumentName):
        """Sets the instrumentName of this Todays.


        :param instrumentName: The instrumentName of this Todays.  # noqa: E501
        :type instrumentName: str
        """

        self._instrumentName = instrumentName

    @property
    def lastPrice(self):
        """Gets the lastPrice of this Todays.  # noqa: E501


        :return: The lastPrice of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._lastPrice

    @lastPrice.setter
    def lastPrice(self, lastPrice):
        """Sets the lastPrice of this Todays.


        :param lastPrice: The lastPrice of this Todays.  # noqa: E501
        :type lastPrice: float
        """

        self._lastPrice = lastPrice

    @property
    def marginType(self):
        """Gets the marginType of this Todays.  # noqa: E501


        :return: The marginType of this Todays.  # noqa: E501
        :rtype: str
        """
        return self._marginType

    @marginType.setter
    def marginType(self, marginType):
        """Sets the marginType of this Todays.


        :param marginType: The marginType of this Todays.  # noqa: E501
        :type marginType: str
        """

        self._marginType = marginType

    @property
    def maxCODQty(self):
        """Gets the maxCODQty of this Todays.  # noqa: E501


        :return: The maxCODQty of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._maxCODQty

    @maxCODQty.setter
    def maxCODQty(self, maxCODQty):
        """Sets the maxCODQty of this Todays.


        :param maxCODQty: The maxCODQty of this Todays.  # noqa: E501
        :type maxCODQty: int
        """

        self._maxCODQty = maxCODQty

    @property
    def multiplier(self):
        """Gets the multiplier of this Todays.  # noqa: E501


        :return: The multiplier of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this Todays.


        :param multiplier: The multiplier of this Todays.  # noqa: E501
        :type multiplier: int
        """

        self._multiplier = multiplier

    @property
    def netTrdQtyLot(self):
        """Gets the netTrdQtyLot of this Todays.  # noqa: E501


        :return: The netTrdQtyLot of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._netTrdQtyLot

    @netTrdQtyLot.setter
    def netTrdQtyLot(self, netTrdQtyLot):
        """Sets the netTrdQtyLot of this Todays.


        :param netTrdQtyLot: The netTrdQtyLot of this Todays.  # noqa: E501
        :type netTrdQtyLot: int
        """

        self._netTrdQtyLot = netTrdQtyLot

    @property
    def netTrdValue(self):
        """Gets the netTrdValue of this Todays.  # noqa: E501


        :return: The netTrdValue of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._netTrdValue

    @netTrdValue.setter
    def netTrdValue(self, netTrdValue):
        """Sets the netTrdValue of this Todays.


        :param netTrdValue: The netTrdValue of this Todays.  # noqa: E501
        :type netTrdValue: float
        """

        self._netTrdValue = netTrdValue

    @property
    def normalSqOffQty(self):
        """Gets the normalSqOffQty of this Todays.  # noqa: E501


        :return: The normalSqOffQty of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._normalSqOffQty

    @normalSqOffQty.setter
    def normalSqOffQty(self, normalSqOffQty):
        """Sets the normalSqOffQty of this Todays.


        :param normalSqOffQty: The normalSqOffQty of this Todays.  # noqa: E501
        :type normalSqOffQty: float
        """

        self._normalSqOffQty = normalSqOffQty

    @property
    def premium(self):
        """Gets the premium of this Todays.  # noqa: E501


        :return: The premium of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._premium

    @premium.setter
    def premium(self, premium):
        """Sets the premium of this Todays.


        :param premium: The premium of this Todays.  # noqa: E501
        :type premium: float
        """

        self._premium = premium

    @property
    def rbiRefRate(self):
        """Gets the rbiRefRate of this Todays.  # noqa: E501


        :return: The rbiRefRate of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._rbiRefRate

    @rbiRefRate.setter
    def rbiRefRate(self, rbiRefRate):
        """Sets the rbiRefRate of this Todays.


        :param rbiRefRate: The rbiRefRate of this Todays.  # noqa: E501
        :type rbiRefRate: int
        """

        self._rbiRefRate = rbiRefRate

    @property
    def realizedPL(self):
        """Gets the realizedPL of this Todays.  # noqa: E501


        :return: The realizedPL of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._realizedPL

    @realizedPL.setter
    def realizedPL(self, realizedPL):
        """Sets the realizedPL of this Todays.


        :param realizedPL: The realizedPL of this Todays.  # noqa: E501
        :type realizedPL: float
        """

        self._realizedPL = realizedPL

    @property
    def sellOpenQtyLot(self):
        """Gets the sellOpenQtyLot of this Todays.  # noqa: E501


        :return: The sellOpenQtyLot of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._sellOpenQtyLot

    @sellOpenQtyLot.setter
    def sellOpenQtyLot(self, sellOpenQtyLot):
        """Sets the sellOpenQtyLot of this Todays.


        :param sellOpenQtyLot: The sellOpenQtyLot of this Todays.  # noqa: E501
        :type sellOpenQtyLot: int
        """

        self._sellOpenQtyLot = sellOpenQtyLot

    @property
    def sellOpenVal(self):
        """Gets the sellOpenVal of this Todays.  # noqa: E501


        :return: The sellOpenVal of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._sellOpenVal

    @sellOpenVal.setter
    def sellOpenVal(self, sellOpenVal):
        """Sets the sellOpenVal of this Todays.


        :param sellOpenVal: The sellOpenVal of this Todays.  # noqa: E501
        :type sellOpenVal: int
        """

        self._sellOpenVal = sellOpenVal

    @property
    def sellTradedQtyLot(self):
        """Gets the sellTradedQtyLot of this Todays.  # noqa: E501


        :return: The sellTradedQtyLot of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._sellTradedQtyLot

    @sellTradedQtyLot.setter
    def sellTradedQtyLot(self, sellTradedQtyLot):
        """Sets the sellTradedQtyLot of this Todays.


        :param sellTradedQtyLot: The sellTradedQtyLot of this Todays.  # noqa: E501
        :type sellTradedQtyLot: int
        """

        self._sellTradedQtyLot = sellTradedQtyLot

    @property
    def sellTradedVal(self):
        """Gets the sellTradedVal of this Todays.  # noqa: E501


        :return: The sellTradedVal of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._sellTradedVal

    @sellTradedVal.setter
    def sellTradedVal(self, sellTradedVal):
        """Sets the sellTradedVal of this Todays.


        :param sellTradedVal: The sellTradedVal of this Todays.  # noqa: E501
        :type sellTradedVal: float
        """

        self._sellTradedVal = sellTradedVal

    @property
    def sellTrdAvg(self):
        """Gets the sellTrdAvg of this Todays.  # noqa: E501


        :return: The sellTrdAvg of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._sellTrdAvg

    @sellTrdAvg.setter
    def sellTrdAvg(self, sellTrdAvg):
        """Sets the sellTrdAvg of this Todays.


        :param sellTrdAvg: The sellTrdAvg of this Todays.  # noqa: E501
        :type sellTrdAvg: float
        """

        self._sellTrdAvg = sellTrdAvg

    @property
    def spanMargin(self):
        """Gets the spanMargin of this Todays.  # noqa: E501


        :return: The spanMargin of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._spanMargin

    @spanMargin.setter
    def spanMargin(self, spanMargin):
        """Sets the spanMargin of this Todays.


        :param spanMargin: The spanMargin of this Todays.  # noqa: E501
        :type spanMargin: int
        """

        self._spanMargin = spanMargin

    @property
    def spanMarginTotal(self):
        """Gets the spanMarginTotal of this Todays.  # noqa: E501


        :return: The spanMarginTotal of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._spanMarginTotal

    @spanMarginTotal.setter
    def spanMarginTotal(self, spanMarginTotal):
        """Sets the spanMarginTotal of this Todays.


        :param spanMarginTotal: The spanMarginTotal of this Todays.  # noqa: E501
        :type spanMarginTotal: float
        """

        self._spanMarginTotal = spanMarginTotal

    @property
    def spreadTotal(self):
        """Gets the spreadTotal of this Todays.  # noqa: E501


        :return: The spreadTotal of this Todays.  # noqa: E501
        :rtype: float
        """
        return self._spreadTotal

    @spreadTotal.setter
    def spreadTotal(self, spreadTotal):
        """Sets the spreadTotal of this Todays.


        :param spreadTotal: The spreadTotal of this Todays.  # noqa: E501
        :type spreadTotal: float
        """

        self._spreadTotal = spreadTotal

    @property
    def totalStock(self):
        """Gets the totalStock of this Todays.  # noqa: E501


        :return: The totalStock of this Todays.  # noqa: E501
        :rtype: int
        """
        return self._totalStock

    @totalStock.setter
    def totalStock(self, totalStock):
        """Sets the totalStock of this Todays.


        :param totalStock: The totalStock of this Todays.  # noqa: E501
        :type totalStock: int
        """

        self._totalStock = totalStock

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
        if not isinstance(other, Todays):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Todays):
            return True

        return self.to_dict() != other.to_dict()
