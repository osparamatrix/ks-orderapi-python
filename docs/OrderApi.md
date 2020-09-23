# ks_api_client.OrderApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | Description
------------- | -------------
[**place_order**](OrderApi.md#place_new_order) | Place a New order
[**modify_order**](OrderApi.md#modify_order) | Modify an existing order
[**cancel_order**](OrderApi.md#cancel_order) | Cancel an order

# **place_new_order**
> object place_order(order_type, instrument_token, transaction_type, quantity, price, disclosed_quantity , trigger_price, tag , validity , variety , product , smart_order_routing )

Place a New order

### Example


```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                         consumer_key = "consumer_key", ip = "IP", app_id = "app_id")

#First initialize session and generate session token

try:
    # Place a Order
    client.place_order(order_type = "N", instrument_token = 727,  \
                   transaction_type = "BUY", quantity = 1, price = 0,\
                   disclosed_quantity = 0, trigger_price = 0, tag = "string",\
                   validity = "GFD", variety = "REGULAR")
except Exception as e:
    print("Exception when calling OrderApi->place_order: %s\n" % e)
``` 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**order_type** | **str**| Type of the order - O(Order), N(NormalOrder), SM(Super Multiple Order), SOR(Smart Order Routing Order), MTF(Margin Trading Facility Order)|
**instrument_token** | **int** | Instrument token of the scrip to be traded |
**transaction_type** | **str** | Transaction Type - BUY or SELL |
**quantity** | **int** | Order quantity - specified in same unit as quoted in market depth |
**price** | **float** | Order Price, non zero positive for limit order and zero for market order |
**disclosed_quantity** | **int** | Quantity to be disclosed in order | [optional] 
**trigger_price** | **float** | Trigger price, required for stoploss or supermultiple order | [optional] 
**tag** | **str** | Tag for this order | [optional] 
**validity** | **str** | Validity of the order - GFD, IOC etc | [optional] 
**variety** | **str** | Variety of the order - REGULAR, AMO, SQUAREOFF - for Super Multiple Orders etc | [optional] 
**product** | **str** | Product type for this order - NORMAL, SUPERMULTIPLE, SUPERMULTIPLEOPTION, MTF | [optional]
**smart_order_routing** | **str** | smart Order Routing for this order | [optional]

### Return type

**object**


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order placed successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)

# **modify_order**
> object modify_order(order_id, price , quantity , disclosed_quantity, trigger_price)

Modify an existing order

### Example


```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                         consumer_key = "consumer_key", ip = "IP", app_id = "app_id")

#First initialize session and generate session token

try:
    # Modify an existing order
    client.modify_order(order_id = "2200922000576", price = 0, quantity = 1, \
                 disclosed_quantity = 0, trigger_price = 0)
								  
except Exception as e:
    print("Exception when calling OrderApi->modify_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**order_id** | **str** | Order ID of the order to be modified | 
**price** | **float** | Order Price, non zero positive for limit order and zero for market order | 
**quantity** | **int** | Order quantity - specified in same unit as quoted in market depth |
**disclosed_quantity** | **int** | Quantity to be disclosed in order | 
**trigger_price** | **float** | Trigger price, required for stoploss or supermultiple order |

### Return type

**object**


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order modified successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)


# **cancel_order**
> object cancel_order(order_id)

Cancel an order

### Example


```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                         consumer_key = "consumer_key", ip = "IP", app_id = "app_id")

#First initialize session and generate session token

try:
    # Cancel an order
    client.cancel_order(order_id = "2200922000576")
except Exception as e:
    print("Exception when calling OrderApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID to cancel. | 

### Return type

**object**


### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order cancelled successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)


