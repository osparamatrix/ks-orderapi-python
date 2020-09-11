import ks_api_client
from ks_api_client.exceptions import ApiException, ApiValueError
from ks_api_client.models import NewMTFOrder, NewNormalOrder, NewOrder, \
                NewSMOrder, NewSOROrder, ExistingMTFOrder, ExistingNormalOrder, \
                ExistingOrder, ExistingSMOrder, ExistingSOROrder, ReqMargin, \
                UserCredentials, UserDetails

from urllib3 import make_headers

class KSTradeApi():
    def __init__(self, access_token, userid, consumer_key, ip, app_id, host = "https://sbx.kotaksecurities.com/apim", proxy_url = '',\
                proxy_user = '', proxy_pass = ''):
        self.host  =  host
        self.userid  =  userid
        self.consumer_key  =  consumer_key
        self.ip  =  ip
        self.app_id  =  app_id
        self.access_token  =  access_token
        configuration  =  self.get_config(proxy_url, proxy_user, proxy_pass)
        self.api_client  =  ks_api_client.ApiClient(configuration)
        session_init_res  =  ks_api_client.SessionApi(self.api_client).session_init(self.userid, \
                              self.consumer_key, self.ip, self.app_id)
        session_init = ''				  
        if(session_init_res.get("Success")):
            session_init = session_init_res.get("Success")
        elif(session_init_res.get("success")):
            session_init = session_init_res.get("success")
        if self.host !=  session_init['redirect']['host']:
            self.host  =  session_init['redirect']['host']
            configuration  =  self.get_config(proxy_url, proxy_user, proxy_pass)
            self.api_client  =  ks_api_client.ApiClient(configuration)
            session_init  =  ks_api_client.SessionApi(self.api_client).session_init(self.userid, \
                              self.consumer_key, self.ip, self.app_id)

    def get_config(self, proxy_url = '', proxy_user = '', proxy_pass = ''):
        configuration  =  ks_api_client.Configuration(self.host)
        configuration.access_token  =  self.access_token
        if proxy_url:
            configuration.proxy = proxy_url
            if proxy_user:
                configuration.proxy_headers = make_headers(proxy_basic_auth = ':'.join((proxy_user,proxy_pass)))
        return configuration

    def login(self, password):
        user_credentials  =  UserCredentials(userid = self.userid, password = password)
        login_response_res  =  ks_api_client.SessionApi(self.api_client).login_with_user_id(self.consumer_key, \
                self.ip, self.app_id, UserCredentials = user_credentials)
        login_response = ''				  
        if(login_response_res.get("Success")):
            login_response = login_response_res.get("Success")
        elif(login_response_res.get("success")):
            login_response = login_response_res.get("success")
        self.one_time_token  =  login_response['oneTimeToken']
        return login_response_res
		
    def generate_session2_fa(self, access_code):
        user_details  =  UserDetails(userid = self.userid, accessCode = access_code)
        if self.one_time_token:
            generate_session_res  =  ks_api_client.SessionApi(self.api_client).generate_session2_fa(self.one_time_token, \
                    self.consumer_key, self.ip, self.app_id, UserDetails = user_details)
            generate_session = ''				  
            if(generate_session_res.get("Success")):
                generate_session = generate_session_res.get("Success")
            elif(generate_session_res.get("success")):
                generate_session = generate_session_res.get("success")
            self.session_token  =  generate_session['sessionToken']
            return generate_session
        else:
            raise ApiValueError("Please invoke 'session_login_api' function first")

    def logout(self):
        logout  =  ks_api_client.SessionApi(self.api_client).session_logout(self.session_token,self.consumer_key,\
						self.ip, self.app_id, self.userid)
        return logout

#-------------------------------------------------------------------------------
# Common methods for placing order

    def place_order(self, order_type, instrument_token, transaction_type,  \
                                quantity, price,  tag = "string", validity ="GFD", variety = "REGULAR",\
                                product = None, disclosed_quantity = None,\
                                trigger_price = None ,smart_order_routing = None):
        """
        Method executes placing_orders according to it's order type.
        return response.
        """
        place_order  =  None
        if not 'session_token'  in self.__dict__:
            raise ApiValueError("Please invoke 'generate_session2_fa' function first")
        if order_type == "O":
            order  =  NewOrder(instrumentToken  =  instrument_token, tag = tag, transactionType = transaction_type,\
                                    variety = variety, quantity = quantity, price = price, disclosedQuantity = disclosed_quantity,\
                                    validity = validity, triggerPrice = trigger_price, product = product,smartOrderRouting = smart_order_routing)
            place_order  =  ks_api_client.OrderApi(self.api_client).place_new_order(self.consumer_key,
                            self.session_token, order)
        elif order_type  ==  'NO':
            order  =  NewNormalOrder(instrumentToken = instrument_token, tag = tag, transactionType = transaction_type,\
                        variety = variety, quantity = quantity, price = price, disclosedQuantity = disclosed_quantity,\
                        validity = validity, triggerPrice = trigger_price)
            place_order  =  ks_api_client.NormalOrderApi(self.api_client).place_new_normal_order(self.consumer_key,
                            self.session_token, order)
        elif order_type  ==  'SMO':
            order  =  NewSMOrder( instrumentToken = instrument_token, tag = tag, transactionType = transaction_type,\
                    variety = variety, quantity = quantity, price = price, disclosedQuantity = disclosed_quantity, \
                    validity = validity, triggerPrice = trigger_price)
            place_order  =  ks_api_client.SuperMultipleOrderApi(self.api_client).place_new_sm_order(self.consumer_key,\
                            self.session_token, order)
        elif order_type  ==  'SORO':
            order  =  NewSOROrder( instrumentToken = instrument_token, tag = tag, transactionType = transaction_type,\
                    variety = variety, quantity = quantity, price = price, validity = validity)
            place_order  =  ks_api_client.SmartOrderRoutingApi(self.api_client).place_new_sor_order(self.consumer_key,\
                            self.session_token, order)
        elif order_type  ==  'MTFO':
            order  =  NewMTFOrder(instrumentToken = instrument_token, tag = tag, transactionType = transaction_type,\
                variety = variety, quantity = quantity, price = price, disclosedQuantity = disclosed_quantity, \
                validity = validity, triggerPrice = trigger_price)
            place_order  =  ks_api_client.MarginTradingApi(self.api_client).place_new_mtf_order(self.consumer_key, \
                            self.session_token, order)
        else:
            raise TypeError("Provided order type is invalid.")

        return place_order

# Common methods for modifiying order

		
    def modify_order(self, order_id, disclosed_quantity = 0, price = 0,\
                    quantity = 1, trigger_price = 0,order_type = None):
        """
        Method executes modifying_orders according to it's order type.
        return response.
        """				
        if not 'session_token' in self.__dict__:
            raise ApiValueError("Please invoke 'generate_session2_fa' function first")
        if order_type is None or order_type  ==  'O':
            modify_order = ExistingOrder(orderId = order_id, disclosedQuantity = disclosed_quantity, price = price,\
                  quantity = quantity, triggerPrice = trigger_price)
            modified_order_res  =  ks_api_client.OrderApi(self.api_client).modify_order(self.consumer_key,
                            self.session_token, modify_order)
        elif order_type  ==  'NO':
            modify_order = ExistingNormalOrder(orderId = order_id, disclosedQuantity = disclosed_quantity, price = price,\
                  quantity = quantity, triggerPrice = trigger_price)
            modified_order_res  =  ks_api_client.NormalOrderApi(self.api_client).modify_normal_order(self.consumer_key,
                            self.session_token, modify_order)
        elif order_type  ==  'SMO':
            modify_order = ExistingSMOrder(orderId = order_id, disclosedQuantity = disclosed_quantity, price = price,\
                  quantity = quantity, triggerPrice = trigger_price)
            modified_order_res  =  ks_api_client.SuperMultipleOrderApi(self.api_client).modify_sm_order(self.consumer_key,
                            self.session_token, modify_order)
        elif order_type  ==  'SORO':
            modify_order = ExistingSOROrder(orderId = order_id, disclosedQuantity = disclosed_quantity, price = price,\
                  quantity = quantity, triggerPrice = trigger_price)
            modified_order_res  =  ks_api_client.SmartOrderRoutingApi(self.api_client).modify_sor_order(self.consumer_key,\
                            self.session_token, modify_order)
        elif order_type  ==  'MTFO':
            modify_order = ExistingMTFOrder(orderId = order_id, disclosedQuantity = disclosed_quantity, price = price,\
                  quantity = quantity, triggerPrice = trigger_price)
            modified_order_res  =  ks_api_client.MarginTradingApi(self.api_client).modify_mtf_order(self.consumer_key, \
                            self.session_token, modify_order)
        else:
            raise TypeError("Provided order type is invalid.")

        return modified_order_res

# Common methods for cancelling order		
		
    def cancel_order(self, order_id, order_type = None):
        """
        Method executes cancelling_order according to it's order type.
        return response.
        """
        order  =  False

        if not 'session_token' in self.__dict__:
            raise ApiValueError("Please invoke 'generate_session2_fa' function first")
        if order_type is None or order_type == 'O':
            order  =  ks_api_client.OrderApi(self.api_client).cancel_order(self.consumer_key,
                            self.session_token, order_id)
        elif order_type == 'NO':
            order  =  ks_api_client.NormalOrderApi(self.api_client).cancel_normal_order(self.consumer_key,
                            self.session_token, order_id)
        elif order_type == 'SMO':
            order  =  ks_api_client.SuperMultipleOrderApi(self.api_client).cancel_sm_order(self.consumer_key,
                            self.session_token, order_id)
        elif order_type == 'SORO':
            order  =  ks_api_client.SmartOrderRoutingApi(self.api_client).cancel_sor_order(self.consumer_key,\
                            self.session_token, order)
        elif order_type == 'MTFO':
            order  =  ks_api_client.MarginTradingApi(self.api_client).cancel_mtf_order(self.consumer_key, \
                            self.session_token, order)
        else:
            raise TypeError("Provided order type is invalid.")

        return order

#-------------------POSITIONS---------------------

    def get_positions(self, position_type):
        if position_type  ==  'TODAYS':
            positions_res  =  ks_api_client.PositionsApi(self.api_client).positions_today(self.consumer_key,self.session_token)
        elif position_type  ==  'OPEN':
            positions_res = ks_api_client.PositionsApi(self.api_client).positions_open(self.consumer_key,self.session_token)
        elif position_type  ==  'STOCKS':
            positions_res = ks_api_client.PositionsApi(self.api_client).positions_stocks(self.consumer_key,self.session_token)
        else:
            raise TypeError("Provided position type is invalid.")
        return positions_res

#---------------------ORDERS REPORTS----------------------------

    def get_order_report(self, order_id  = None):
        if order_id is None:
            order_report  =  ks_api_client.ReportsApi(self.api_client).get_order_reports(self.consumer_key, \
                    self.session_token)
        else:
            order_report  =  ks_api_client.ReportsApi(self.api_client).get_order_report_by_order_id(order_id,self.consumer_key, \
                self.session_token)
        return order_report

#--------------------------TRADES REPORTS---------------------------------

    def get_trade_report(self, order_id  = None):
        if order_id is None:
            trade_report  =  ks_api_client.ReportsApi(self.api_client).get_trade_report(consumerKey = self.consumer_key,
                sessionToken = self.session_token)
        else:
            trade_report  =  ks_api_client.ReportsApi(self.api_client).get_trade_report_by_order_id(order_id,self.consumer_key, \
                self.session_token)
        return trade_report        

#-----------------------Margins------------------------

    def margin_required(self, transaction_type, order_info):
        req_margin  =  ReqMargin(transactionType = transaction_type, orderInfo = self.convertArray(order_info))
        if not isinstance(req_margin, ReqMargin):
            raise ApiValueError("ReqMargin with type ",type(req_margin)," is not valid.")
        margin_required  =  ks_api_client.MarginApi(self.api_client).margin_required(self.consumer_key,self.session_token,
                ReqMargin = req_margin)
        return margin_required
		
#-----------------------Quote Api------------------------	

    def get_quote(self, instrument_token, quote_type = None):
        if quote_type is None:
            quote  =  ks_api_client.QuoteApi(self.api_client).get_instruments_details(self.consumer_key, \
                self.session_token, instrument_token)
        elif quote_type  ==  'LTP':
             quote  =  ks_api_client.QuoteApi(self.api_client).get_ltp_quote(self.consumer_key, \
                self.session_token, instrument_token)
        elif quote_type  ==  'DEPTH':
            quote  =  ks_api_client.QuoteApi(self.api_client).get_market_details_quote(self.consumer_key, \
                self.session_token, instrument_token)
        elif quote_type  ==  'OHLC':
            quote  =  ks_api_client.QuoteApi(self.api_client).get_ohlc_quote(self.consumer_key, \
                self.session_token, instrument_token)
        else:
            raise TypeError("Provided quote type is invalid.")
        return quote

#-----------------------Get Order Id-------------
    def get_order_id(self, order_res):
        if(order_res.get("Success")):
            order = order_res.get("Success");
        elif(order_res.get("success")):
            order = order_res.get("success");
        if (order.get("NSE") and order.get("BSE")):
            if(order.get("NSE").get("orderId")):
                order = order.get("NSE")
            elif(order.get("BSE").get("orderId")):
                order = order.get("BSE")
        else:
            if(order.get("NSE")):
                order = order.get("NSE")
            elif(order.get("BSE")):
                order = order.get("BSE")
        return str(order['orderId'])

#-------- Convert Array and object snake_case keys to camelCase -----------
    def convertObject(self, object):  
        newObj={}
        for key in object .keys():
            new_key='';
            for idx , word in enumerate(key.split('_')): 
                if(idx==0):
                    new_key = ''+str(word)
                else:
                    new_key=new_key+(word.title())
            newObj[new_key] = object[key]
            
        return newObj
 
    def convertArray(self, array): 
        new_array = []
        for obj in array:
            new_array.append(self.convertObject(obj))
        return new_array
