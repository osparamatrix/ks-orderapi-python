# openapi_client.SuperMultipleOrderApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**place_order**](SuperMultipleOrderApi.md#place_new_sm_order) | **POST** /orders/1.0/order/supermultiple | Place a New Super Multiple order
[**modify_order**](SuperMultipleOrderApi.md#modify_sm_order) | **PUT** /orders/1.0/order/supermultiple | Modify an existing super multiple order
[**cancel_order**](SuperMultipleOrderApi.md#cancel_sm_order) | **DELETE** /orders/1.0/order/supermultiple/{orderId} | Cancel an Super Multiple order

# **place_new_sm_order**
> object place_order(instrument_token , tag, transaction_type, variety, quantity, price, disclosed_quantity,\
>                                 validity, trigger_price, order_type)

Place a New Super Multiple order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")

#First initialize session and generate session token


try:
    # Place a New order
    client.place_order(instrument_token = "instrument_token", tag = "tag", transaction_type = "transaction_type",\
                        variety = "variety", quantity = "quantity", price = "price", disclosed_quantity = "disclosed_quantity",\
                        validity = "validity", trigger_price = "trigger_price", order_type = "SMO")
except ApiException as e:
    print("Exception when calling SuperMultipleOrderApi->place_new_sm_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**instrument_token** | **int** | Instrument token of the scrip to be traded |
**transaction_type** | **str** | Transaction Type - BUY or SELL |
**quantity** | **int** | Order quantity - specified in same unit as quoted in market depth |
**price** | **float** | Order Price, non zero positive for limit order and zero for market order |
**validity** | **str** | Validity of the order - GFD, IOC etc | [optional] 
**variety** | **str** | Variety of the order - REGULAR, AMO, SQUAREOFF - for Super Multiple Orders etc | [optional] 
**disclosed_quantity** | **int** | Quantity to be disclosed in order | 
**trigger_price** | **float** | Trigger price, required for stoploss or supermultiple order | 
**tag** | **str** | Tag for this order | [optional] 
**order_type** | **str**|  | For NormalOrderApi, order_type is "SMO"

### Return type

object

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_sm_order**
> object modify_order(order_id, disclosed_quantity, price, quantity, trigger_price, order_type)

Modify an existing super multiple order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")

#First initialize session and generate session token

try:
    # Modify an existing order
    client.modify_order(order_id="order_id", disclosed_quantity="disclosed_quantity", price="price",\
                                  quantity="quantity", trigger_price="trigger_price", order_type="SMO")
except Exception as e:
    print("Exception when calling SuperMultipleOrderApi->modify_sm_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**order_id** | **str** | Order ID of the order to be modified | 
**quantity** | **int** | Order quantity - specified in same unit as quoted in market depth |
**price** | **float** | Order Price, non zero positive for limit order and zero for market order | 
**disclosed_quantity** | **int** | Quantity to be disclosed in order |
**trigger_price** | **float** | Trigger price, required for stoploss or supermultiple order |
**order_type** | **str**| For SuperMultipleOrderApi, order_type is "SMO" if not provided it will call modify order of OrderApi | [optional ]

### Return type

object

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Super MultipleOrder modified successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_sm_order**
> object cancel_order(order_id , order_type)

Cancel an Super Multiple order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")

#First initialize session and generate session token

try:
   # Cancel an order
    client.cancel_order(order_id = "order_id", order_type = "SMO")
except Exception as e:
    print("Exception when calling SuperMultipleOrderApi->cancel_sm_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID to cancel. | 
 **order_type** | **str** | For SuperMultipleOrderApi, order_type is "SMO" if not provided it will call cancel order of OrderApi | [optional]

### Return type

object

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
