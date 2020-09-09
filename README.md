# openapi-client
No description provided

- API version: 1.0.0
- Package version: 1.0.0
- Build package: com.paramatrix.ks.codegen.PythonKsGenerator

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/osparamatrix/ks-orderapi-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/osparamatrix/ks-orderapi-python.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from openapi_client.api.api import KSTradeApi as TradingApi
from openapi_client.models import NewNormalOrder, ExistingOrder, ReqMargin
from openapi_client.exceptions import ApiException

# Defining the host is optional and defaults to https://sbx.kotaksecurities.com/apim
# See configuration.py for a list of all supported configuration parameters.
openapi_client = TradingApi(host, access_token, userid, consumer_key, app_id, ip)

order_id=""

try:
    # Login using password
    api_response = openapi_client.session_login_user(password)
    print(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->login_with_user_id: %s\n" % e)

try:
    # Generate final Session Token
    api_response = openapi_client.generate_session2_fa(access_code)
    print(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->generate_session2_fa: %s\n" % e)

# Placing Normal order
try:
    # Place a New normal order
    order = NewNormalOrder(instrumentToken=727, tag="string", transactionType="SELL",\
                        variety="REGULAR", quantity=1, price=1440, disclosedQuantity=0,\
                        validity="GFD", triggerPrice=1560)
    api_response = openapi_client.place_order(order)
    order_id=api_response
    print(api_response)
except ApiException as e:
    print("Exception when calling NormalOrderApi->place_new_normal_order: %s\n" % e)

try:
    # Modify an existing normal order
    existing_oder = ExistingOrder(order_id, disclosedQuantity=0, price=0,\
            quantity=1, triggerPrice=0)
    api_response = openapi_client.modify_order(existing_oder)
    order_id=api_response
    print(api_response)
except ApiException as e:
    print("Exception when calling NormalOrderApi->modify_normal_order: %s\n" % e)

try:
    # Cancel an Normal order
    # OrderId will be available if order is placed
    api_response = openapi_client.cancel_order(order_id, 'NO')
    print(api_response)
except ApiException as e:
    print("Exception when calling NormalOrderApi->cancel_normal_order: %s\n" % e)

try:
    # To get todays position 
    api_response=openapi_client.positions_today()
    print(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_today: %s\n" % e)

try:
    # Get Margin Required for an order by amount or quantity.
    orderInfo = [
        {"instrumentToken": 771, "quantity": 1, "price": 1300, "amount": 0, "triggerPrice": 1190},
        {"instrumentToken": 374, "quantity": 1, "price": 1200, "amount": 0, "triggerPrice": 1150}
        ]
    margin_request = ReqMargin(transactionType="BUY",orderInfo=orderInfo)
    api_response = openapi_client.margin_required(margin_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->margin_required: %s\n" % e)

try:
    # Get order report
    api_response = openapi_client.get_order_report()
    print(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_order_reports: %s\n" % e)

try:
    # Get order report by orderId
    api_response = openapi_client.get_order_report_by_order_id(order_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_order_report_by_order_id: %s\n" % e)


try:
    # Get instrument details
    instrumentTokens=110
    api_response=openapi_client.get_instruments_details(instrumentTokens)
    print(api_response)
except ApiException as e:
    print("Exception when calling QuoteApi->get_instruments_details: %s\n" % e)

try:
    # Invalidate Session Tsoken
    api_response = openapi_client.logout(userid)
    print(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->session_logout: %s\n" % e)


```
## Documentation for API Endpoints

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*MarginApi* | [**margin_required**](docs/MarginApi.md#margin_required) | **POST** /margin/1.0/margin/required | Get Margin Required for an order by amount or quantity.
*MarginTradingApi* | [**cancel_mtf_order**](docs/MarginTradingApi.md#cancel_mtf_order) | **DELETE** /orders/1.0/order/mtf/{orderId} | Cancel an order
*MarginTradingApi* | [**modify_mtf_order**](docs/MarginTradingApi.md#modify_mtf_order) | **PUT** /orders/1.0/order/mtf | Modify an existing MTF order
*MarginTradingApi* | [**place_new_mtf_order**](docs/MarginTradingApi.md#place_new_mtf_order) | **POST** /orders/1.0/order/mtf | Place a New MTF order
*NormalOrderApi* | [**cancel_normal_order**](docs/NormalOrderApi.md#cancel_normal_order) | **DELETE** /orders/1.0/order/normal/{orderId} | Cancel a Normal order
*NormalOrderApi* | [**modify_normal_order**](docs/NormalOrderApi.md#modify_normal_order) | **PUT** /orders/1.0/order/normal | Modify an existing normal order
*NormalOrderApi* | [**place_new_normal_order**](docs/NormalOrderApi.md#place_new_normal_order) | **POST** /orders/1.0/order/normal | Place a New normal order
*OrderApi* | [**cancel_order**](docs/OrderApi.md#cancel_order) | **DELETE** /orders/1.0/orders/{orderId} | Cancel an order
*OrderApi* | [**modify_order**](docs/OrderApi.md#modify_order) | **PUT** /orders/1.0/orders | Modify an existing order
*OrderApi* | [**place_new_order**](docs/OrderApi.md#place_new_order) | **POST** /orders/1.0/orders | Place a New order
*PositionsApi* | [**positions**](docs/PositionsApi.md#positions) | **GET** /positions/1.0/positions | Get&#39;s raw position from Trading Engine.
*PositionsApi* | [**positions_open**](docs/PositionsApi.md#positions_open) | **GET** /positions/1.0/positions/open | Get&#39;s Open position.
*PositionsApi* | [**positions_stocks**](docs/PositionsApi.md#positions_stocks) | **GET** /positions/1.0/positions/stocks | Get&#39;s Sell from Existing stocks.
*PositionsApi* | [**positions_today**](docs/PositionsApi.md#positions_today) | **GET** /positions/1.0/positions/todays | Get&#39;s Todays position.
*QuoteApi* | [**get_instruments_details**](docs/QuoteApi.md#get_instruments_details) | **GET** /quotes/v1.0/instruments/{instrumentTokens} | Get full details
*QuoteApi* | [**get_ltp_quote**](docs/QuoteApi.md#get_ltp_quote) | **GET** /quotes/v1.0/ltp/instruments/{instrumentTokens} | Get LTP quote
*QuoteApi* | [**get_market_details_quote**](docs/QuoteApi.md#get_market_details_quote) | **GET** /quotes/v1.0/depth/instruments/{instrumentTokens} | Get market details quote
*QuoteApi* | [**get_ohlc_quote**](docs/QuoteApi.md#get_ohlc_quote) | **GET** /quotes/v1.0/ohlc/instruments/{instrumentTokens} | Get OHLC quote
*ReportsApi* | [**get_order_report_by_order_id**](docs/ReportsApi.md#get_order_report_by_order_id) | **GET** /reports/1.0/orders/{orderId} | Get order report by orderId
*ReportsApi* | [**get_order_reports**](docs/ReportsApi.md#get_order_reports) | **GET** /reports/1.0/orders | Get order report
*ReportsApi* | [**get_trade_report**](docs/ReportsApi.md#get_trade_report) | **GET** /reports/1.0/trades | Get trade report
*ReportsApi* | [**get_trade_report_by_order_id**](docs/ReportsApi.md#get_trade_report_by_order_id) | **GET** /reports/1.0/trades/{orderId} | Get trade report by orderId
*SessionApi* | [**generate_session2_fa**](docs/SessionApi.md#generate_session2_fa) | **POST** /session/1.0/session/2FA/accesscode | Generate final Session Token
*SessionApi* | [**login_with_user_id**](docs/SessionApi.md#login_with_user_id) | **POST** /session/1.0/session/login/userid | Login using Userid
*SessionApi* | [**session_init**](docs/SessionApi.md#session_init) | **GET** /session/1.0/session/init | Initialise Session
*SessionApi* | [**session_logout**](docs/SessionApi.md#session_logout) | **DELETE** /session/1.0/session/logout | Invalidate Session Token
*SmartOrderRoutingApi* | [**cancel_sor_order**](docs/SmartOrderRoutingApi.md#cancel_sor_order) | **DELETE** /orders/1.0/order/sor/{orderId} | Cancel an SORorder
*SmartOrderRoutingApi* | [**modify_sor_order**](docs/SmartOrderRoutingApi.md#modify_sor_order) | **PUT** /orders/1.0/order/sor | Modify an existing SOR order
*SmartOrderRoutingApi* | [**place_new_sor_order**](docs/SmartOrderRoutingApi.md#place_new_sor_order) | **POST** /orders/1.0/order/sor | Place a New SOR order
*SuperMultipleOrderApi* | [**cancel_sm_order**](docs/SuperMultipleOrderApi.md#cancel_sm_order) | **DELETE** /orders/1.0/order/supermultiple/{orderId} | Cancel an Super Multiple order
*SuperMultipleOrderApi* | [**modify_sm_order**](docs/SuperMultipleOrderApi.md#modify_sm_order) | **PUT** /orders/1.0/order/supermultiple | Modify an existing super multiple order
*SuperMultipleOrderApi* | [**place_new_sm_order**](docs/SuperMultipleOrderApi.md#place_new_sm_order) | **POST** /orders/1.0/order/supermultiple | Place a New Super Multiple order


## Documentation For Models

 - [Bracketcancel](docs/Bracketcancel.md)
 - [Bracketmodify](docs/Bracketmodify.md)
 - [Bracketplace](docs/Bracketplace.md)
 - [Buy](docs/Buy.md)
 - [Codcancel](docs/Codcancel.md)
 - [Codmodify](docs/Codmodify.md)
 - [Codplace](docs/Codplace.md)
 - [Ctdmodify](docs/Ctdmodify.md)
 - [Ctdplace](docs/Ctdplace.md)
 - [Depth](docs/Depth.md)
 - [ExistingMTFOrder](docs/ExistingMTFOrder.md)
 - [ExistingNormalOrder](docs/ExistingNormalOrder.md)
 - [ExistingOrder](docs/ExistingOrder.md)
 - [ExistingSMOrder](docs/ExistingSMOrder.md)
 - [ExistingSOROrder](docs/ExistingSOROrder.md)
 - [Fault](docs/Fault.md)
 - [Gtccancel](docs/Gtccancel.md)
 - [Gtcmodify](docs/Gtcmodify.md)
 - [Gtcplace](docs/Gtcplace.md)
 - [History](docs/History.md)
 - [Instrument](docs/Instrument.md)
 - [LTPQuote](docs/LTPQuote.md)
 - [MarginDet](docs/MarginDet.md)
 - [MarketDetailsQuote](docs/MarketDetailsQuote.md)
 - [NewMTFOrder](docs/NewMTFOrder.md)
 - [NewNormalOrder](docs/NewNormalOrder.md)
 - [NewOrder](docs/NewOrder.md)
 - [NewSMOrder](docs/NewSMOrder.md)
 - [NewSOROrder](docs/NewSOROrder.md)
 - [OHLCQuote](docs/OHLCQuote.md)
 - [Open](docs/Open.md)
 - [OrderInfo](docs/OrderInfo.md)
 - [Orders](docs/Orders.md)
 - [Positions](docs/Positions.md)
 - [ReqMargin](docs/ReqMargin.md)
 - [ResLogin](docs/ResLogin.md)
 - [ResLogout](docs/ResLogout.md)
 - [ResMTFMod](docs/ResMTFMod.md)
 - [ResMTFOrderCancel](docs/ResMTFOrderCancel.md)
 - [ResNewMTFOrder](docs/ResNewMTFOrder.md)
 - [ResNewNormalOrder](docs/ResNewNormalOrder.md)
 - [ResNewOrder](docs/ResNewOrder.md)
 - [ResNewSMOrder](docs/ResNewSMOrder.md)
 - [ResNewSOROrder](docs/ResNewSOROrder.md)
 - [ResNormalOrderCancel](docs/ResNormalOrderCancel.md)
 - [ResNormalOrderMod](docs/ResNormalOrderMod.md)
 - [ResOrderCancel](docs/ResOrderCancel.md)
 - [ResOrderMod](docs/ResOrderMod.md)
 - [ResSMOrderCancel](docs/ResSMOrderCancel.md)
 - [ResSMOrderMod](docs/ResSMOrderMod.md)
 - [ResSOROrderCancel](docs/ResSOROrderCancel.md)
 - [ResSOROrderMod](docs/ResSOROrderMod.md)
 - [ResSession2FA](docs/ResSession2FA.md)
 - [ResSessionInit](docs/ResSessionInit.md)
 - [ResSessionInitEncryption](docs/ResSessionInitEncryption.md)
 - [ResSessionInitRedirect](docs/ResSessionInitRedirect.md)
 - [ResSessionInitWeblink](docs/ResSessionInitWeblink.md)
 - [Sell](docs/Sell.md)
 - [Sor](docs/Sor.md)
 - [Stocks](docs/Stocks.md)
 - [Todays](docs/Todays.md)
 - [Trades](docs/Trades.md)
 - [Tslocancel](docs/Tslocancel.md)
 - [Tslomodify](docs/Tslomodify.md)
 - [Tsloplace](docs/Tsloplace.md)
 - [UserCredentials](docs/UserCredentials.md)
 - [UserDetails](docs/UserDetails.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication (JWT)


## Author




