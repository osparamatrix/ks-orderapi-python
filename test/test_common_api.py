import unittest
import time

from ks_api_client import ks_api
from ks_api_client.exceptions import ApiException, ApiValueError
from ks_api_client.models import NewMTFOrder, NewNormalOrder, NewOrder, \
                        NewSMOrder, NewSOROrder, ExistingMTFOrder, ExistingNormalOrder, \
                        ExistingOrder, ExistingSMOrder, ExistingSOROrder, ReqMargin
from ks_api_client.settings import host, access_token, userid, \
                        consumer_key, app_id, password, access_code, ip

class TestKSTradeApi(unittest.TestCase):
    ks_trade_api = ks_api.KSTradeApi(host=host, access_token=access_token, userid=userid, \
                consumer_key=consumer_key, app_id=app_id, ip="127.0.0.1", \
                proxy_url="", proxy_user="", proxy_pass="")

    def test_00_session_login_api(self):
        print(self.ks_trade_api.login(password=password))

    def test_01_generate_session2_fa(self):
        time.sleep(1)
        print(self.ks_trade_api.generate_session2_fa(access_code=access_code))

# ----------------Order--------------------

    def test_02_place_order(self, instrument_token=727, tag="string", transaction_type="BUY",\
                                variety="REGULAR", quantity=1, price=0, disclosed_quantity=0,\
                                validity="GFD", trigger_price=0, product="NORMAL",smart_order_routing="string", order_type="O"):
        print("\nPlacing order with ORDER type.")
        time.sleep(1)
        try:
            placed_order = self.ks_trade_api.place_order("O", instrument_token, transaction_type,\
                 quantity, price, tag, validity, variety, disclosed_quantity=disclosed_quantity, \
                 trigger_price=trigger_price, product=product,smart_order_routing=smart_order_routing)
            print("\tOrder placed successfully. \n: "+ str(placed_order))
			
            order_id=self.ks_trade_api.get_order_id(placed_order)
            modified_order = self.ks_trade_api.modify_order(order_id, 0, 1,0, 0, "O")
            print("\tOrder modified successfully. \n: "+ str(modified_order))
            cancelled_order= self.ks_trade_api.cancel_order(order_id, 'O')
            print("\tOrder cancelled successfully.\n" + str(cancelled_order))
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e


# ----------------Normal Order--------------------

    def test_03_place_normal_order(self, instrument_token=727, tag="string", transaction_type="BUY",\
                        variety="REGULAR", quantity=1, price=0, disclosed_quantity=0,\
                        validity="GFD", trigger_price=0,  order_type="NO"):
        print("\nPlacing order with NORAML ORDER type.")
        time.sleep(1)
        try:
            placed_order = self.ks_trade_api.place_order("NO", instrument_token, transaction_type,\
                quantity, price, tag, validity, variety, disclosed_quantity=disclosed_quantity, \
                 trigger_price=trigger_price)
            print("\tOrder placed successfully. \n: "+ str(placed_order))
			
            order_id=self.ks_trade_api.get_order_id(placed_order)
            modified_order = self.ks_trade_api.modify_order(order_id, 0, 1,0, 0,"NO")
            print("\tOrder modified successfully.\n: "+ str(modified_order))
            cancelled_order= self.ks_trade_api.cancel_order(order_id, 'NO')
            print("\tOrder cancelled successfully.\n"+ str(cancelled_order))
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e

# ----------------Multiple Order--------------------

    def test_04_place_multiple_order(self, instrument_token=727, tag="string", transaction_type="BUY",\
                    variety="REGULAR", quantity=3, price=0, disclosed_quantity=0, \
                    validity="GFD", trigger_price=1201, order_type="SMO"):
        print("\nPlacing order with MULTIPLE ORDER type.")
        time.sleep(1)
        try:
            placed_order = self.ks_trade_api.place_order("SMO", instrument_token, transaction_type,\
                quantity, price, tag, validity, variety, disclosed_quantity=disclosed_quantity, \
                 trigger_price=trigger_price)
            print("\tOrder placed successfully. \n: "+str(placed_order))
			
            order_id=self.ks_trade_api.get_order_id(placed_order)
            modified_order = self.ks_trade_api.modify_order(order_id, 0, 1,0, 0,"SMO")
            print("\tOrder modified successfully.\n: "+str(modified_order))
            cancelled_order= self.ks_trade_api.cancel_order(order_id, 'SMO')
            print("\tOrder cancelled successfully.\n"+ str(cancelled_order))
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e


# ----------------SOR Order--------------------

    def test_05_place_sor_order(self, instrument_token=727, tag="string", transaction_type="BUY",\
                    variety="REGULAR", quantity=1, price=0, validity="GFD", order_type="SORO"):
        print("\nPlacing order with SOR ORDER type")
        time.sleep(1)
        try:
            placed_order = self.ks_trade_api.place_order("SORO", instrument_token, transaction_type,\
                quantity, price, tag, validity, variety)
            print("\tOrder placed successfully.\n: "+ str(placed_order))
			
            order_id=self.ks_trade_api.get_order_id(placed_order)
            modified_order = self.ks_trade_api.modify_order(order_id, 0, 1,0, 0,"SORO")
            print("\tOrder modified successfully.\n: "+ str(modified_order))
            cancelled_order= self.ks_trade_api.cancel_order(order_id, 'SORO')
            print("\tOrder cancelled successfully.\n"+ str(cancelled_order))
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e


# ----------------MTF Order--------------------

    def test_06_place_mtf_order(self, instrument_token=727, tag="string", transaction_type="BUY",\
                variety="REGULAR", quantity=1, price=0, disclosed_quantity=0, \
                validity="GFD", trigger_price=0, order_type="MTFO"):
        print("\nPlacing order with MTF ORDER type.")
        time.sleep(1)
        try:
            placed_order = self.ks_trade_api.place_order( "MTFO", instrument_token, transaction_type,\
                quantity, price, tag, validity, variety, disclosed_quantity=disclosed_quantity, \
                 trigger_price=trigger_price)
            print("\tOrder placed successfully. \n: "+ str(placed_order))
			
            order_id=self.ks_trade_api.get_order_id(placed_order)
            modified_order = self.ks_trade_api.modify_order(order_id, 0, 1,0, 0,"MTFO")
            print("\tOrder modified successfully. \n: "+ str(modified_order))
            cancelled_order= self.ks_trade_api.cancel_order(order_id, 'MTFO')
            print("\tOrder cancelled successfully.\n"+ str(cancelled_order))
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e

#----------------------- POSITION ------------------------

    def test_07_positions_today(self):
        positions_today=self.ks_trade_api.get_positions('TODAYS')
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
        print("\nGenerating ORDER Report by order_id")
        time.sleep(1)
        placed_order = self.ks_trade_api.place_order(instrument_token=727, tag="string", transaction_type="BUY",\
                                variety="REGULAR", quantity=1, price=0, disclosed_quantity=0,\
                                validity="GFD", trigger_price=0, product="NORMAL",order_type="NO")
        print("\tOrder placed "+ str(placed_order))
        order_id=self.ks_trade_api.get_order_id(placed_order)
        get_order_report_by_order_id = self.ks_trade_api.get_order_report(order_id)
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
        print("\nGenerating TRADE Report by order_id")
        time.sleep(1)
        placed_order = self.ks_trade_api.place_order(instrument_token=727, tag="string", transaction_type="BUY",\
                                variety="REGULAR", quantity=1, price=0, disclosed_quantity=0,\
                                validity="GFD", trigger_price=0, product="NORMAL",order_type="NO")
        print("\tOrder placed "+ str(placed_order))
        order_id=self.ks_trade_api.get_order_id(placed_order)
        get_trade_report_by_order_id = self.ks_trade_api.get_trade_report(order_id)
        if get_trade_report_by_order_id:
            print("\tTrade report received succesfully.\n")

#----------------------- Margin Required ------------------------

    def test_14_margin_required(self):
        order_info = [
            {"instrument_token": 727, "quantity": 1, "price": 1300, "amount": 0, "trigger_price": 1190},
            {"instrument_token": 1374, "quantity": 1, "price": 1200, "amount": 0, "trigger_price": 1150}
        ]
        margin_required=self.ks_trade_api.margin_required("BUY",order_info)
        print("\nMargin required tested.")

#----------------------- Quotes ------------------------

    def test_15_get_ltp_quote(self):
        quote=self.ks_trade_api.get_quote(110, 'LTP')
        print("\nTested get_ltp_quote with ", quote)

    def test_16_get_market_details_quote(self):
        quote=self.ks_trade_api.get_quote(110, 'DEPTH')
        print("\nTested get_market_details_quote with ", quote)

    def test_17_get_ohlc_quote(self):
        quote=self.ks_trade_api.get_quote(110, 'OHLC')
        print("\nTested get_ohlc_quote with ", quote)

    def test_18_get_instruments_details(self):
        quote=self.ks_trade_api.get_quote(110)
        print("\nTested get_instruments_details with ", quote)

#----------------------- LOGOUT ------------------------

    def test_19_logout(self):
        logout=self.ks_trade_api.logout()
        print("\nLogout successful")


if __name__ == '__main__':
    unittest.main
