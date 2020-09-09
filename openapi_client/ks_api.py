import openapi_client
from openapi_client.exceptions import ApiException, ApiValueError
from openapi_client.models import NewMTFOrder, NewNormalOrder, NewOrder, \
                NewSMOrder, NewSOROrder, ExistingMTFOrder, ExistingNormalOrder, \
                ExistingOrder, ExistingSMOrder, ExistingSOROrder, ReqMargin, \
                UserCredentials, UserDetails

from urllib3 import make_headers

class KSTradeApi():
    def __init__(self, access_token, userid, consumer_key, ip, app_id, host="https://sbx.kotaksecurities.com/apim", proxy_url='',\
                proxy_user='', proxy_pass=''):
        self.host = host
        self.userid = userid
        self.consumer_key = consumer_key
        self.ip = ip
        self.app_id = app_id
        self.access_token = access_token
        configuration = self.get_config(proxy_url, proxy_user, proxy_pass)
        self.api_client = openapi_client.ApiClient(configuration)
        session_init_res = openapi_client.SessionApi(self.api_client).session_init(self.userid, \
                              self.consumer_key, self.ip, self.app_id)
        session_init=''				  
        if(session_init_res.get("Success")):
            session_init=session_init_res.get("Success")
        elif(session_init_res.get("success")):
            session_init=session_init_res.get("success")
        if self.host != session_init['redirect']['host']:
            self.host = session_init['redirect']['host']
            configuration = self.get_config(proxy_url, proxy_user, proxy_pass)
            self.api_client = openapi_client.ApiClient(configuration)
            session_init = openapi_client.SessionApi(self.api_client).session_init(self.userid, \
                              self.consumer_key, self.ip, self.app_id)

    def get_config(self, proxy_url='', proxy_user='', proxy_pass=''):
        configuration = openapi_client.Configuration(self.host)
        configuration.access_token = self.access_token
        if proxy_url:
            configuration.proxy=proxy_url
            if proxy_user:
                configuration.proxy_headers=make_headers(proxy_basic_auth=':'.join((proxy_user,proxy_pass)))
        return configuration

    def session_login_user(self, password):
        user_credentials = UserCredentials(userid=self.userid, password=password)
        login_response_res = openapi_client.SessionApi(self.api_client).login_with_user_id(self.consumer_key, \
                self.ip, self.app_id, UserCredentials=user_credentials)
        login_response=''				  
        if(login_response_res.get("Success")):
            login_response=login_response_res.get("Success")
        elif(login_response_res.get("success")):
            login_response=login_response_res.get("success")
        self.one_time_token = login_response['oneTimeToken']
        return login_response_res
		
    def generate_session2_fa(self, access_code):
        user_details = UserDetails(userid=self.userid, accessCode=access_code)
        if self.one_time_token:
            generate_session_res = openapi_client.SessionApi(self.api_client).generate_session2_fa(self.one_time_token, \
                    self.consumer_key, self.ip, self.app_id, UserDetails=user_details)
            generate_session=''				  
            if(generate_session_res.get("Success")):
                generate_session=generate_session_res.get("Success")
            elif(generate_session_res.get("success")):
                generate_session=generate_session_res.get("success")
            self.session_token = generate_session['sessionToken']
            return generate_session
        else:
            raise ApiValueError("Please invoke 'session_login_api' function first")

    def logout(self, userid):
        if userid:
            logout = openapi_client.SessionApi(self.api_client).session_logout(self.session_token,self.consumer_key,
                            self.ip, self.app_id, self.userid)
            return logout
        else:
            raise ApiValueError("Invalid user id supplied")

#-------------------------------------------------------------------------------
# Common methods for placing order

    def place_order(self, order_type, instrumentToken, transactionType,  validity, variety,\
                                quantity, price,  tag="string", product=None, disclosedQuantity=None,\
                                 triggerPrice=None ,smartOrderRouting=None):
        """
        Method executes placing_orders according to it's order type.
        return response.
        """
        place_order = None
        if not 'session_token'  in self.__dict__:
            raise ApiValueError("Please invoke 'generate_session2_fa' function first")
        if order_type=="O":
            order = NewOrder(instrumentToken = instrumentToken, tag=tag, transactionType=transactionType,\
                                    variety=variety, quantity=quantity, price=price, disclosedQuantity=disclosedQuantity,\
                                    validity=validity, triggerPrice=triggerPrice, product=product,smartOrderRouting=smartOrderRouting)
            place_order = openapi_client.OrderApi(self.api_client).place_new_order(self.consumer_key,
                            self.session_token, order)
        elif order_type == 'NO':
            order = NewNormalOrder(instrumentToken=instrumentToken, tag=tag, transactionType=transactionType,\
                        variety=variety, quantity=quantity, price=price, disclosedQuantity=disclosedQuantity,\
                        validity=validity, triggerPrice=triggerPrice)
            place_order = openapi_client.NormalOrderApi(self.api_client).place_new_normal_order(self.consumer_key,
                            self.session_token, order)
        elif order_type == 'SMO':
            order = NewSMOrder( instrumentToken=instrumentToken, tag=tag, transactionType=transactionType,\
                    variety=variety, quantity=quantity, price=price, disclosedQuantity=disclosedQuantity, \
                    validity=validity, triggerPrice=triggerPrice)
            place_order = openapi_client.SuperMultipleOrderApi(self.api_client).place_new_sm_order(self.consumer_key,\
                            self.session_token, order)
        elif order_type == 'SORO':
            order = NewSOROrder( instrumentToken=instrumentToken, tag=tag, transactionType=transactionType,\
                    variety=variety, quantity=quantity, price=price, validity="GFD")
            place_order = openapi_client.SmartOrderRoutingApi(self.api_client).place_new_sor_order(self.consumer_key,\
                            self.session_token, order)
        elif order_type == 'MTFO':
            order = NewMTFOrder(instrumentToken=instrumentToken, tag=tag, transactionType=transactionType,\
                variety=variety, quantity=quantity, price=price, disclosedQuantity=disclosedQuantity, \
                validity=validity, triggerPrice=triggerPrice)
            place_order = openapi_client.MarginTradingApi(self.api_client).place_new_mtf_order(self.consumer_key, \
                            self.session_token, order)
        else:
            raise TypeError("Provided order type is invalid.")

        return place_order

# Common methods for modifiying order

		
    def modify_order(self, order_type, orderId, disclosedQuantity=0, price=0,\
                    quantity=1, triggerPrice=0):
        """
        Method executes modifying_orders according to it's order type.
        return response.
        """
        modify_order=ExistingOrder(orderId=orderId, disclosedQuantity=disclosedQuantity, price=price,\
                  quantity=quantity, triggerPrice=triggerPrice)
					
        if not 'session_token' in self.__dict__:
            raise ApiValueError("Please invoke 'generate_session2_fa' function first")
        if order_type == 'O':
            modified_order_res = openapi_client.OrderApi(self.api_client).modify_order(self.consumer_key,
                            self.session_token, modify_order)
        elif order_type == 'NO':
            modified_order_res = openapi_client.NormalOrderApi(self.api_client).modify_normal_order(self.consumer_key,
                            self.session_token, modify_order)
        elif order_type == 'SMO':
            modified_order_res = openapi_client.SuperMultipleOrderApi(self.api_client).modify_sm_order(self.consumer_key,
                            self.session_token, modify_order)
        elif order_type == 'SORO':
            modified_order_res = openapi_client.SmartOrderRoutingApi(self.api_client).modify_sor_order(self.consumer_key,\
                            self.session_token, modify_order)
        elif order_type == 'MTFO':
            modified_order_res = openapi_client.MarginTradingApi(self.api_client).modify_mtf_order(self.consumer_key, \
                            self.session_token, modify_order)
        else:
            raise TypeError("Provided order type is invalid.")

        return modified_order_res

# Common methods for cancelling order		
		
    def cancel_order(self, order_id, type):
        """
        Method executes cancelling_order according to it's order type.
        return response.
        """
        order = False

        if not 'session_token' in self.__dict__:
            raise ApiValueError("Please invoke 'generate_session2_fa' function first")

        if type=='O':
            order = openapi_client.OrderApi(self.api_client).cancel_order(self.consumer_key,
                            self.session_token, order_id)
        elif type=='NO':
            order = openapi_client.NormalOrderApi(self.api_client).cancel_normal_order(self.consumer_key,
                            self.session_token, order_id)
        elif type=='SMO':
            order = openapi_client.SuperMultipleOrderApi(self.api_client).cancel_sm_order(self.consumer_key,
                            self.session_token, order_id)
        elif type=='SORO':
            order = openapi_client.SmartOrderRoutingApi(self.api_client).cancel_sor_order(self.consumer_key,\
                            self.session_token, order)
        elif type=='MTFO':
            order = openapi_client.MarginTradingApi(self.api_client).cancel_mtf_order(self.consumer_key, \
                            self.session_token, order)
        else:
            raise TypeError("Provided order type is invalid.")

        return order.orderId

#-------------------POSITIONS---------------------

    def get_positions(self, positionType =None):
        if positionType == 'TODAY':
            positions_res = openapi_client.PositionsApi(self.api_client).positions_today(self.consumer_key,self.session_token)
        elif positionType == 'OPEN':
            positions_res=openapi_client.PositionsApi(self.api_client).positions_open(self.consumer_key,self.session_token)
        elif positionType == 'STOCKS':
            positions_res=openapi_client.PositionsApi(self.api_client).positions_stocks(self.consumer_key,self.session_token)
        else:
            raise TypeError("Provided position type is invalid.")
        return positions_res

#---------------------ORDERS REPORTS----------------------------

    def get_order_report(self, order_id =None):
        if order_id is None:
            order_report = openapi_client.ReportsApi(self.api_client).get_order_reports(self.consumer_key, \
                    self.session_token)
        else:
            order_report = openapi_client.ReportsApi(self.api_client).get_order_report_by_order_id(order_id,self.consumer_key, \
                self.session_token)
        return order_report

#--------------------------TRADES REPORTS---------------------------------

    def get_trade_report(self, order_id =None):
        if order_id is None:
            trade_report = openapi_client.ReportsApi(self.api_client).get_trade_report(consumerKey=self.consumer_key,
                sessionToken=self.session_token)
        else:
            trade_report = openapi_client.ReportsApi(self.api_client).get_trade_report_by_order_id(order_id,self.consumer_key, \
                self.session_token)
        return trade_report        

#-----------------------Margins------------------------

    def margin_required(self, transactionType, orderInfo):
        req_margin = ReqMargin(transactionType, orderInfo)
        if not isinstance(req_margin, ReqMargin):
            raise ApiValueError("ReqMargin with type ",type(req_margin)," is not valid.")
        margin_required = openapi_client.MarginApi(self.api_client).margin_required(self.consumer_key,self.session_token,
                ReqMargin=req_margin)
        return margin_required
		
#-----------------------Quote Api------------------------	

    def get_quote(self, instrument_token, quoteType=None):
        if quoteType is None:
            quote = openapi_client.QuoteApi(self.api_client).get_instruments_details(self.consumer_key, \
                self.session_token, instrument_token)
        elif quoteType == 'LTP':
             quote = openapi_client.QuoteApi(self.api_client).get_ltp_quote(self.consumer_key, \
                self.session_token, instrument_token)
        elif quoteType == 'MARKET':
            quote = openapi_client.QuoteApi(self.api_client).get_market_details_quote(self.consumer_key, \
                self.session_token, instrument_token)
        elif quoteType == 'OHLC':
            quote = openapi_client.QuoteApi(self.api_client).get_ohlc_quote(self.consumer_key, \
                self.session_token, instrument_token)
        else:
            raise TypeError("Provided quote type is invalid.")
        return quote

#-----------------------Get Order Id-------------
    def get_order_id(self, order_res):
        if(order_res.get("Success")):
            order=order_res.get("Success");
        elif(order_res.get("success")):
            order=order_res.get("success");
        if (order.get("NSE") and order.get("BSE")):
            if(order.get("NSE").get("orderId")):
                order=order.get("NSE")
            elif(order.get("BSE").get("orderId")):
                order=order.get("BSE")
        else:
            if(order.get("NSE")):
                order=order.get("NSE")
            elif(order.get("BSE")):
                order=order.get("BSE")
        return str(order['orderId'])