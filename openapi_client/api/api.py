import openapi_client
from openapi_client.exceptions import ApiException, ApiValueError
from openapi_client.models import NewMTFOrder, NewNormalOrder, NewOrder, \
                NewSMOrder, NewSOROrder, ExistingMTFOrder, ExistingNormalOrder, \
                ExistingOrder, ExistingSMOrder, ExistingSOROrder, ReqMargin, \
                UserCredentials, UserDetails

from urllib3 import make_headers

class KSTradeApi():
    def __init__(self, host, access_token, userid, consumer_key, ip, app_id, proxy_url='',\
                proxy_user='', proxy_pass=''):
        self.host = host
        self.userid = userid
        self.consumer_key = consumer_key
        self.ip = ip
        self.app_id = app_id
        self.access_token = access_token
        configuration = self.get_config(proxy_url, proxy_user, proxy_pass)
        self.api_client = openapi_client.ApiClient(configuration)
        session_init = openapi_client.SessionApi(self.api_client).session_init(self.userid, \
                              self.consumer_key, self.ip, self.app_id)
        if self.host != session_init.redirect.host:
            self.host = session_init.redirect.host
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
        login_response = openapi_client.SessionApi(self.api_client).login_with_user_id(self.consumer_key, \
                self.ip, self.app_id, UserCredentials=user_credentials)
        self.one_time_token = login_response.oneTimeToken
        return login_response

    def generate_session2_fa(self, access_code):
        user_details = UserDetails(userid=self.userid, accessCode=access_code)
        if self.one_time_token:
            generate_session = openapi_client.SessionApi(self.api_client).generate_session2_fa(self.one_time_token, \
                    self.consumer_key, self.ip, self.app_id, UserDetails=user_details)
            self.session_token = generate_session.sessionToken
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
# Common methods for placing/ modifying/ cancelling order

    def place_order(self, order):
        """
        Method executes placing_orders according to it's order type.
        return response.
        """
        place_order = None
        if not 'session_token'  in self.__dict__:
            raise ApiValueError("Please invoke 'generate_session2_fa' function first")
        if isinstance(order, NewOrder):
            place_order = openapi_client.OrderApi(self.api_client).place_new_order(self.consumer_key,
                            self.session_token, order)
        elif isinstance(order, NewNormalOrder):
            place_order = openapi_client.NormalOrderApi(self.api_client).place_new_normal_order(self.consumer_key,
                            self.session_token, order)
        elif isinstance(order, NewSMOrder):
            place_order = openapi_client.SuperMultipleOrderApi(self.api_client).place_new_sm_order(self.consumer_key,
                            self.session_token, order)
        elif isinstance(order, NewSOROrder):
            place_order = openapi_client.SmartOrderRoutingApi(self.api_client).place_new_sor_order(self.consumer_key,\
                            self.session_token, order)
            return place_order

        elif isinstance(order, NewMTFOrder):
            place_order = openapi_client.MarginTradingApi(self.api_client).place_new_mtf_order(self.consumer_key, \
                            self.session_token, order)
        else:
            raise TypeError("Provided order type is invalid.")

        return place_order.orderId

    def modify_order(self, order):
        """
        Method executes modifying_orders according to it's order type.
        return response.
        """
        if not 'session_token' in self.__dict__:
            raise ApiValueError("Please invoke 'generate_session2_fa' function first")
        if isinstance(order, ExistingOrder):
            order = openapi_client.OrderApi(self.api_client).modify_order(self.consumer_key,
                            self.session_token, order)
        elif isinstance(order, ExistingNormalOrder):
            order = openapi_client.NormalOrderApi(self.api_client).modify_normal_order(self.consumer_key,
                            self.session_token, order)
        elif isinstance(order, ExistingSMOrder):
            order = openapi_client.SuperMultipleOrderApi(self.api_client).modify_sm_order(self.consumer_key,
                            self.session_token, order)
        elif isinstance(order, ExistingSOROrder):
            order = openapi_client.SmartOrderRoutingApi(self.api_client).modify_sor_order(self.consumer_key,\
                            self.session_token, order)
        elif isinstance(order, ExistingMTFOrder):
            order = openapi_client.MarginTradingApi(self.api_client).modify_mtf_order(self.consumer_key, \
                            self.session_token, order)
        else:
            raise TypeError("Provided order type is invalid.")

        return order.orderId

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

    def positions_today(self):
        positionstoday = openapi_client.PositionsApi(self.api_client).positions_today(self.consumer_key,self.session_token)
        return positionstoday

    def positions_open(self):
        positionsopen=openapi_client.PositionsApi(self.api_client).positions_open(self.consumer_key,self.session_token)
        return positionsopen

    def positions_stocks(self):
        positionsstocks=openapi_client.PositionsApi(self.api_client).positions_stocks(self.consumer_key,self.session_token)
        return positionsstocks

#---------------------REPORTS----------------------------

    def get_order_report(self):
        order_report = openapi_client.ReportsApi(self.api_client).get_order_reports(self.consumer_key, \
                    self.session_token)
        return order_report

    def get_order_report_by_order_id(self, order_id):
        order_report = openapi_client.ReportsApi(self.api_client).get_order_report_by_order_id(order_id,self.consumer_key, \
                self.session_token)
        return order_report

#--------------------------TRADES---------------------------------

    def get_trade_report(self):
        trade_report = openapi_client.ReportsApi(self.api_client).get_trade_report(consumerKey=self.consumer_key,
             sessionToken=self.session_token)
        return trade_report


    def get_trade_report_by_order_id(self, order_id):
        trade_report = openapi_client.ReportsApi(self.api_client).get_trade_report_by_order_id(order_id,self.consumer_key, \
                self.session_token)
        return trade_report

#-----------------------Margins------------------------

    def margin_required(self, req_margin):
        if not isinstance(req_margin, ReqMargin):
            raise ApiValueError("ReqMargin with type ",type(req_margin)," is not valid.")
        margin_required = openapi_client.MarginApi(self.api_client).margin_required(self.consumer_key,self.session_token,
                ReqMargin=req_margin)
        return margin_required
