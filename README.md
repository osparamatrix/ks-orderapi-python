# openapi-client
No description provided

- API version: 1.0.1
- Package version: 1.0.10

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
import ks_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ks_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from ks_api_client import ks_api
# Defining the host is optional and defaults to https://sbx.kotaksecurities.com/apim
# See configuration.py for a list of all supported configuration parameters.
client = ks_api.KSTradeApi(access_token = "", userid = "", \
                              consumer_key = "", app_id = "", ip = "127.0.0.1")
# Get session for user
client.login(password = "")
#Generated session token
client.generate_session2_fa(access_code = "")
# Place an order
client.place_order(order_type = "NO", instrument_token = 727, transaction_type = "BUY",\
                        quantity = 1, price = 0, tag = "string", validity = "GFD", variety = "REGULAR",\
						disclosed_quantity = 0, trigger_price = 0)
# Modify an order
client.modify_order(order_id = "", price = 0, quantity=1, disclosed_quantity = 0, trigger_price=0)
# Cancel an order
client.cancel_order(order_id = "")
# Get Positions
client.get_positions(position_type = "TODAYS")
# Get Margin required
order_info = [
    {"instrument_token": 727, "quantity": 1, "price": 1300, "amount": 0, "trigger_price": 1190},
    {"instrument_token": 1374, "quantity": 1, "price": 1200, "amount": 0, "trigger_price": 1150}
]
client.margin_required(transaction_type="BUY",order_info=order_info)

# Get Report Orders for order id
client.get_order_report(order_id="")

# Get Report Orders
client.get_order_report()

# Get Quote details
client.get_quote(instrument_token=110)

#Terminate user's Session
client.logout()
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




