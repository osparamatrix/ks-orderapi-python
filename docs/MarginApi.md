# ks_api_client.MarginApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | Description
------------- | -------------
[**margin_required**](MarginApi.md#margin_required) | Get Margin Required for an order by amount or quantity.


# **margin_required**
> object margin_required(transaction_type, order_info)

Get Margin Required for an order by amount or quantity.

Returns margin required for Equity, Super Multiple & MTF Order.

### Example


```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                 consumer_key = "consumer_key", ip = "IP", app_id = "app_id", host = "host",\
                 proxy_url = "proxy_url", proxy_user = "proxy_user", proxy_pass = "proxy_pass")

#First initialize session and generate session token

try:
    # Get Margin Required for an order by amount or quantity.
        order_info = [
            {"instrument_token": 727, "quantity": 1, "price": 1300, "amount": 0, "trigger_price": 1190},
            {"instrument_token": 1374, "quantity": 1, "price": 1200, "amount": 0, "trigger_price": 1150}
        ]
    client.margin_required(transaction_type="BUY",order_info=order_info)
except Exception as e:
    print("Exception when calling MarginApi->margin_required: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**transaction_type** | **str** | Transaction Type - BUY or SELL | 
**order_info** | [**list[OrderInfo]**](OrderInfo.md) |  | 

### Return type

**object**


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the Margin required by client for order. |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

