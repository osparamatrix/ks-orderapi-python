import unittest
import time

from openapi_client.api.api import KSTradeApi as TradingApi
from openapi_client.rest import ApiValueError

from openapi_client.settings import host, access_token, userid, \
    consumer_key, app_id, password, access_code


class TestKSTradeApi(unittest.TestCase):

    ks_trade_api = TradingApi(host, access_token, userid, consumer_key, app_id)

    def test_a_session_login_api(self):
        login_response = self.ks_trade_api.session_login_user(userid, password)
        print("Your login is successful. One time token is ", login_response.oneTimeToken)

    def test_b_generate_session2_fa(self):
        time.sleep(1)
        session_response = self.ks_trade_api.generate_session2_fa(access_code, userid)
        print("Your session is generated. Session token is ", session_response.sessionToken)
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
 #NORMAL
    def test_c_place_order(self):
        time.sleep(1)
        place_new_order = self.ks_trade_api.place_new_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        if place_new_order.orderId:
            print("Your Normal Order Id ", place_new_order.orderId, "is been successfully placed")
        else:
            raise ApiValueError("Normal Order Could not be placed")

    def test_d_modify_order(self):
        time.sleep(1)
        new_order_modify = self.ks_trade_api.place_new_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        if new_order_modify.orderId :
            print("Your Normal Order Id ", new_order_modify.orderId, "is been modified ")
            modify_order = self.ks_trade_api.modify_order(new_order_modify.orderId, disclosed_quantity = 0,\
                    price = 0, quantity = 1, trigger_price = 0)
            if modify_order.orderId :
                print("Your Normal Order Id ", modify_order.orderId, "is not Modified")

    def test_e_cancel_order(self):
        time.sleep(1)
        new_order_cancel = self.ks_trade_api.place_new_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        if new_order_cancel.orderId :
            print("Your Normal Order Id", new_order_cancel.orderId, "is been cancelled ")
            cancel_order = self.ks_trade_api.cancel_order(int(new_order_cancel.orderId))
            if cancel_order.orderId:
                print("Your Normal Order Id ", cancel_order.orderId, "is not cancelled")
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# # #ORDERS
    def test_f_place_order(self):
        time.sleep(1)
        place_new_order = self.ks_trade_api.place_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0, product = "NORMAL" ,smartOrderRouting="string")
        if place_new_order.orderId :
            print("Your Order Id ", place_new_order.orderId, "is been successfully placed")
        else:
            raise ApiValueError("Order Could not be placed")

    def test_g_modify_order(self):
        time.sleep(1)
        new_order_modify = self.ks_trade_api.place_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0,product = "NORMAL" ,smartOrderRouting="string")
        if new_order_modify.orderId :
            print("Your Order Id ", new_order_modify.orderId, "is been successfully modified")
            modify_order = self.ks_trade_api.modify_order(new_order_modify.orderId, disclosed_quantity = 0,\
                    price = 0, quantity = 1, trigger_price = 0)
            if modify_order.orderId :
                print("Your Order Id ", modify_order.orderId, "is not Modified")


    def test_h_cancel_order(self):
        time.sleep(1)
        new_order_cancel = self.ks_trade_api.place_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0, product = "NORMAL" ,smartOrderRouting="string")
        if new_order_cancel.orderId :
            print("Your Order Id", new_order_cancel.orderId, "is been cancelled")
            cancel_order = self.ks_trade_api.cancel_order(int(new_order_cancel.orderId))
            if cancel_order.orderId :
                print("Your Order Id ", cancel_order.orderId, "is not cancelled")
#----------------------------------------------------------------------------------------------------------------------------



# #----------------------------------------------------------------------------------------------------------------------------
# #MULTIPLE ORDER

    def test_c_place_new_sm_order(self):
        time.sleep(1)
        place_new_sm_order = self.ks_trade_api.place_new_sm_order(tag="string", transaction_type="BUY",
                    instrument_token=727, variety="REGULAR", quantity=0, price=0, \
                    disclosed_quantity=1, validity="GFD", trigger_price=15)
        if place_new_sm_order.orderId :
            print("Your Multiple Order Id ", place_new_sm_order.orderId, "is been successfully placed")
        else:
            raise ApiValueError("Multiple Order Could not be placed")

    def test_d_modify_sm_order(self):
        time.sleep(1)
        new_order_modify = self.ks_trade_api.place_new_sm_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 0, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 1005)
        if new_order_modify.orderId :
            print("Your Multiple Order Id ", new_order_modify.orderId, "is  Modified")
            modify_sm_order = self.ks_trade_api.modify_sm_order(new_order_modify.orderId, disclosed_quantity = 0,\
                    price = 0, quantity = 0, trigger_price = 1005)
            if modify_sm_order.orderId :
                print("Your Multiple Order Id ", modify_sm_order.orderId, "is not Modified")


    def test_e_cancel_sm_order(self):
        time.sleep(1)
        cancel_sm_order = self.ks_trade_api.place_new_sm_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 0, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 1005)
        if cancel_sm_order.orderId :
            print("Your Multiple Order Id", cancel_sm_order.orderId, "is  cancelled")
            cancel_sm_order = self.ks_trade_api.cancel_sm_order(int(cancel_sm_order.orderId))
            if cancel_sm_order.orderId :
                print("Your Multiple  Order Id ", cancel_sm_order.orderId, "is not cancelled")


# #----------------------------------------------------------------------------------------------------------------------------
#SOR
    def test_s_place_new_sor_order(self):
        time.sleep(1)
        place_new_sor_order = self.ks_trade_api.place_new_sor_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, validity = "GFD")

        if place_new_sor_order.orderId:
            print("Your SOR Order ", place_new_sor_order.orderId, "is been successfully placed")
        else:
            raise ApiValueError("Order Could not be placed")

    def test_t_modify_sor_order(self):
        time.sleep(1)
        new_order_modify = self.ks_trade_api.place_new_sor_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                validity = "GFD")
        if new_order_modify.orderId:
            print("Your Order ", new_order_modify.orderId, "is been successfully placed")
            modify_order = self.ks_trade_api.modify_sor_order(new_order_modify.orderId, \
                    price = 0, quantity = 1)
            if modify_order.orderId :
                print("Your SOR Order ", modify_order.orderId, "is been successfully Modified")


    def test_u_cancel_sor_order(self):
        time.sleep(1)
        new_order_cancel = self.ks_trade_api.place_new_sor_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                validity = "GFD")
        if new_order_cancel.orderId:
            print("Your Order ", new_order_cancel.orderId, "is been successfully placed")
            cancel_order = self.ks_trade_api.cancel_sor_order(int(new_order_cancel.orderId))
            if cancel_order.orderId :
                print("Your SOR Order  ", cancel_order.orderId, "is been successfully cancelled")

#----------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------
#MTF
    def test_f_place_new_mtf_order(self):
        time.sleep(1)
        place_new_order = self.ks_trade_api.place_new_mtf_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        if place_new_order.orderId :
            print("Your MTF Order Id ", place_new_order.orderId, "is been successfully placed")
        else:
            raise ApiValueError("MTF Order Couldnot be placed")

    def test_g_modify_mtf_order(self):
        time.sleep(1)
        new_order_modify = self.ks_trade_api.place_new_mtf_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        if new_order_modify.orderId:
            print("Your MTF Order Id ", new_order_modify.orderId, "is been modified ")
            modify_mtf_order = self.ks_trade_api.modify_mtf_order(new_order_modify.orderId, disclosed_quantity = 1,\
                    price = 0, quantity = 1, trigger_price = 0)
            if modify_mtf_order.orderId :
                print("Your MTF Order Id ", modify_mtf_order.orderId, "is not Modified")

    def test_h_cancel_mtf_order(self):
        time.sleep(1)
        new_order_cancel = self.ks_trade_api.place_new_mtf_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0)
        if new_order_cancel.orderId :
            print("Your MTF Order Id", new_order_cancel.orderId, "is cancelled")
            cancel_mtf_order = self.ks_trade_api.cancel_mtf_order(int(new_order_cancel.orderId))
            if cancel_mtf_order.orderId :
                print("Your MTF Order Id ", cancel_mtf_order.orderId, "is not cancelled")
#----------------------------------------------------------------------------------------------------------------------------
# POSITION

    def test_c_positions_today(self):
        positions_today=self.ks_trade_api.positions_today()
        print(positions_today,"Position today")

    def test_d_positions_open(self):
        positions_open=self.ks_trade_api.positions_open()
        print(positions_open," Position open ")

    def test_e_positions_stocks(self):
        positions_stocks=self.ks_trade_api.positions_stocks()
        print(positions_stocks,"Position stock")

# #----------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------
 #REPORTS
    def test_o_get_order_report(self):

        time.sleep(1)
        get_order_report = self.ks_trade_api.place_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0, product = "NORMAL" ,smartOrderRouting="string")
        if get_order_report.orderId :
            print("Your Report has been succesfully generated")
            get_order_report = self.ks_trade_api.get_order_report(get_order_report.orderId)


    def test_p_get_order_report_by_order_id(self):

        time.sleep(1)
        get_order_report_by_order_id = self.ks_trade_api.place_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0, product = "NORMAL" ,smartOrderRouting="string")
        if get_order_report_by_order_id.orderId :
            print("Your get order report by order id is: ", get_order_report_by_order_id.orderId ,"has been succesfully genrated")
            get_order_report_by_order_id = self.ks_trade_api.get_order_report_by_order_id(get_order_report_by_order_id.orderId)
# #----------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------
 #TRADS
    def test_q_get_trade_report(self):

        time.sleep(1)
        get_trade_report = self.ks_trade_api.place_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0, product = "NORMAL" ,smartOrderRouting="string")
        if get_trade_report.orderId:
            print("Your tread Report for get order  : ", get_trade_report.orderId ,"has been succesfully genrated")
            get_trade_report = self.ks_trade_api.get_trade_report()


    def test_r_get_trade_report_by_order_id(self):

        time.sleep(1)
        get_trade_report_by_order_id = self.ks_trade_api.place_order(tag = "string", transaction_type = "BUY", \
                instrument_token = 727, variety = "REGULAR", quantity = 1, price = 0, \
                disclosed_quantity = 0, validity = "GFD", trigger_price = 0, product = "NORMAL" ,smartOrderRouting="string")
        if get_trade_report_by_order_id.orderId is not None:
            print("Your trade order report by order id is: ", get_trade_report_by_order_id.orderId ,"has been succesfully genrated")
            get_trade_report_by_order_id = self.ks_trade_api.get_trade_report_by_order_id(get_trade_report_by_order_id.orderId)

#-----------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------
#MARGIN
    # def test_i_margin_required(self):
    #     margin_required=self.ks_trade_api.margin_required(consumer_key)
    #     print(margin_required,"Margin required ")

#----------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main
