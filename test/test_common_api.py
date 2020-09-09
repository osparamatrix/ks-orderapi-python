import unittest
import time

import api
from openapi_client.exceptions import ApiException, ApiValueError
from openapi_client.models import NewMTFOrder, NewNormalOrder, NewOrder, \
                        NewSMOrder, NewSOROrder, ExistingMTFOrder, ExistingNormalOrder, \
                        ExistingOrder, ExistingSMOrder, ExistingSOROrder, ReqMargin
from openapi_client.settings import host, access_token, userid, \
                        consumer_key, app_id, password, access_code, ip

class TestKSTradeApi(unittest.TestCase):
    ks_trade_api = api.KSTradeApi(host=host, access_token=access_token, userid=userid, \
                consumer_key=consumer_key, app_id=app_id, ip="127.0.0.1", \
                proxy_url="", proxy_user="", proxy_pass="")

    def test_00_session_login_api(self):
        print(self.ks_trade_api.session_login_user(password=password))

    def test_01_generate_session2_fa(self):
        time.sleep(1)
        print(self.ks_trade_api.generate_session2_fa(access_code=access_code))

# ----------------Order--------------------

    def test_02_place_order(self, instrumentToken=727, tag="string", transactionType="BUY",\
                                variety="REGULAR", quantity=1, price=0, disclosedQuantity=0,\
                                validity="GFD", triggerPrice=0, product="NORMAL",smartOrderRouting="string", order_type="O"):
        print("\nPlacing order with ORDER type.")
        time.sleep(1)
        try:
            placed_order = self.ks_trade_api.place_order(instrumentToken = instrumentToken, tag=tag, transactionType=transactionType,\
                                    variety=variety, quantity=quantity, price=price, disclosedQuantity=disclosedQuantity,\
                                    validity=validity, triggerPrice=triggerPrice, product=product,smartOrderRouting=smartOrderRouting, order_type="O")
            print("\tOrder placed successfully. \n: "+ str(placed_order))
			
            orderId=self.ks_trade_api.get_order_id(placed_order)
            modified_order = self.ks_trade_api.modify_order(orderId=orderId, disclosedQuantity=0, price=0,\
                                  quantity=1, triggerPrice=0, order_type="O")
            print("\tOrder modified successfully. \n: "+ str(modified_order))
            cancelled_order= self.ks_trade_api.cancel_order(orderId, 'O')
            print("\tOrder cancelled successfully.\n" + str(cancelled_order))
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e


# ----------------Normal Order--------------------

    def test_03_place_normal_order(self, instrumentToken=727, tag="string", transactionType="BUY",\
                        variety="REGULAR", quantity=1, price=0, disclosedQuantity=0,\
                        validity="GFD", triggerPrice=0,  order_type="NO"):
        print("\nPlacing order with NORAML ORDER type.")
        time.sleep(1)
        try:
            placed_order = self.ks_trade_api.place_order(instrumentToken=instrumentToken, tag=tag, transactionType=transactionType,\
                        variety=variety, quantity=quantity, price=price, disclosedQuantity=disclosedQuantity,\
                        validity=validity, triggerPrice=triggerPrice,  order_type="NO")
            print("\tOrder placed successfully. \n: "+ str(placed_order))
			
            orderId=self.ks_trade_api.get_order_id(placed_order)
            modified_order = self.ks_trade_api.modify_order(orderId=orderId, disclosedQuantity=0, price=0,\
            quantity=1, triggerPrice=0, order_type="NO")
            print("\tOrder modified successfully.\n: "+ str(modified_order))
            cancelled_order= self.ks_trade_api.cancel_order(orderId, 'NO')
            print("\tOrder cancelled successfully.\n"+ str(cancelled_order))
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e

# ----------------Multiple Order--------------------

    def test_04_place_multiple_order(self, instrumentToken=727, tag="string", transactionType="BUY",\
                    variety="REGULAR", quantity=3, price=0, disclosedQuantity=0, \
                    validity="GFD", triggerPrice=1201, order_type="SMO"):
        print("\nPlacing order with MULTIPLE ORDER type.")
        time.sleep(1)
        try:
            placed_order = self.ks_trade_api.place_order(instrumentToken=instrumentToken, tag=tag, transactionType=transactionType,\
                    variety=variety, quantity=quantity, price=price, disclosedQuantity=disclosedQuantity, \
                    validity=validity, triggerPrice=triggerPrice, order_type="SMO")
            print("\tOrder placed successfully. \n: "+str(placed_order))
			
            orderId=self.ks_trade_api.get_order_id(placed_order)
            modified_order = self.ks_trade_api.modify_order(orderId=orderId, disclosedQuantity=0,\
            price=0, quantity=1, triggerPrice=1000, order_type="SMO")
            print("\tOrder modified successfully.\n: "+str(modified_order))
            cancelled_order= self.ks_trade_api.cancel_order(orderId, 'SMO')
            print("\tOrder cancelled successfully.\n"+ str(cancelled_order))
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e


# ----------------SOR Order--------------------

    def test_05_place_sor_order(self, instrumentToken=727, tag="string", transactionType="BUY",\
                    variety="REGULAR", quantity=1, price=0, validity="GFD", order_type="SORO"):
        print("\nPlacing order with SOR ORDER type")
        time.sleep(1)
        try:
            placed_order = self.ks_trade_api.place_order(instrumentToken=instrumentToken, tag=tag, transactionType=transactionType,\
                    variety=variety, quantity=quantity, price=price, validity=validity, order_type="SORO")
            print("\tOrder placed successfully.\n: "+ str(placed_order))
			
            orderId=self.ks_trade_api.get_order_id(placed_order)
            modified_order = self.ks_trade_api.modify_order(orderId=orderId, quantity=12, price=1400, \
                                            disclosedQuantity=10, triggerPrice=1280, order_type="SORO")
            print("\tOrder modified successfully.\n: "+ str(modified_order))
            cancelled_order= self.ks_trade_api.cancel_order(orderId, 'SORO')
            print("\tOrder cancelled successfully.\n"+ str(cancelled_order))
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e


# ----------------MTF Order--------------------

    def test_06_place_mtf_order(self, instrumentToken=727, tag="string", transactionType="BUY",\
                variety="REGULAR", quantity=1, price=0, disclosedQuantity=0, \
                validity="GFD", triggerPrice=0, order_type="MTFO"):
        print("\nPlacing order with MTF ORDER type.")
        time.sleep(1)
        try:
            placed_order = self.ks_trade_api.place_order( instrumentToken=instrumentToken, tag=tag, transactionType=transactionType,\
                variety=variety, quantity=quantity, price=price, disclosedQuantity=disclosedQuantity, \
                validity=validity, triggerPrice=triggerPrice, order_type="MTFO")
            print("\tOrder placed successfully. \n: "+ str(placed_order))
			
            orderId=self.ks_trade_api.get_order_id(placed_order)
            modified_order = self.ks_trade_api.modify_order(orderId=orderId, disclosedQuantity=1,\
            price=0, quantity=1, triggerPrice=0, order_type="MTFO")
            print("\tOrder modified successfully. \n: "+ str(modified_order))
            cancelled_order= self.ks_trade_api.cancel_order(orderId, 'MTFO')
            print("\tOrder cancelled successfully.\n"+ str(cancelled_order))
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e

#----------------------- POSITION ------------------------

    def test_07_positions_today(self):
        positions_today=self.ks_trade_api.get_positions('TODAY')
        print("\nPosition Today",positions_today)

    def test_08_positions_open(self):
        positions_open=self.ks_trade_api.get_positions('OPEN')
        print("Position Open", positions_open)

    def test_09_positions_stocks(self):
        positions_stocks=self.ks_trade_api.get_positions('STOCKS')
        print("Position Stock", positions_stocks)

#--------------------------------ORDER REPORT-------------------------------------------------------------------------------------------
    def test_10_get_order_report(self):
        print("\nGenerating ORDER Report")
        time.sleep(1)
        get_order_report = self.ks_trade_api.get_order_report()
        print("\tOrder report generated successfully.\n")


    def test_11_get_order_report_by_order_id(self):
        print("\nGenerating ORDER Report by orderId")
        time.sleep(1)
        placed_order = self.ks_trade_api.place_order(instrumentToken=727, tag="string", transactionType="BUY",\
                                variety="REGULAR", quantity=1, price=0, disclosedQuantity=0,\
                                validity="GFD", triggerPrice=0, product="NORMAL",order_type="NO")
        print("\tOrder placed "+ str(placed_order))
        orderId=self.ks_trade_api.get_order_id(placed_order)
        get_order_report_by_order_id = self.ks_trade_api.get_order_report(orderId)
        if get_order_report_by_order_id:
            print("\tOrder report generated succesfully.\n")

#-------------------------------TRADE REPORT---------------------------------
    def test_12_get_trade_report(self):
        print("\nGenerating TRADE Report")
        time.sleep(1)
        get_trade_report = self.ks_trade_api.get_trade_report()
        if get_trade_report:
            print("\tTrade report genrated succesfully.\n")

    def test_13_get_trade_report_by_order_id(self):
        print("\nGenerating TRADE Report by orderId")
        time.sleep(1)
        placed_order = self.ks_trade_api.place_order(instrumentToken=727, tag="string", transactionType="BUY",\
                                variety="REGULAR", quantity=1, price=0, disclosedQuantity=0,\
                                validity="GFD", triggerPrice=0, product="NORMAL",order_type="NO")
        print("\tOrder placed "+ str(placed_order))
        orderId=self.ks_trade_api.get_order_id(placed_order)
        get_trade_report_by_order_id = self.ks_trade_api.get_trade_report(orderId)
        if get_trade_report_by_order_id:
            print("\tTrade report received succesfully.\n")

#----------------------- Margin Required ------------------------

    def test_14_margin_required(self):
        orderInfo = [
            {"instrumentToken": 727, "quantity": 1, "price": 1300, "amount": 0, "triggerPrice": 1190},
            {"instrumentToken": 1374, "quantity": 1, "price": 1200, "amount": 0, "triggerPrice": 1150}
        ]
        margin_required=self.ks_trade_api.margin_required(transactionType="BUY",orderInfo=orderInfo)
        print("\nMargin required tested.")

#----------------------- Quotes ------------------------

    def test_15_get_ltp_quote(self):
        instrumentToken=110
        quote=self.ks_trade_api.get_quote(instrumentToken, 'LTP')
        print("Tested get_ltp_quote with ", quote)

    def test_16_get_market_details_quote(self):
        instrumentToken=110
        quote=self.ks_trade_api.get_quote(instrumentToken, 'MARKET')
        print("Tested get_market_details_quote with ", quote)

    def test_17_get_ohlc_quote(self):
        instrumentToken=110
        quote=self.ks_trade_api.get_quote(instrumentToken, 'OHLC')
        print("Tested get_ohlc_quote with ", quote)

    def test_18_get_instruments_details(self):
        instrumentToken=110
        quote=self.ks_trade_api.get_quote(instrumentToken)
        print("Tested get_instruments_details with ", quote)

#----------------------- LOGOUT ------------------------

    def test_19_logout(self):
        logout=self.ks_trade_api.logout(userid)
        print("\nLogout successful")


if __name__ == '__main__':
    unittest.main
