# openapi_client.MarginTradingApi


All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**place_new_mtf_order**](MarginTradingApi.md#place_new_mtf_order) | **POST** /orders/1.0/order/mtf | Place a New MTF order
[**modify_mtf_order**](MarginTradingApi.md#modify_mtf_order) | **PUT** /orders/1.0/order/mtf | Modify an existing MTF order
[**cancel_mtf_order**](MarginTradingApi.md#cancel_mtf_order) | **DELETE** /orders/1.0/order/mtf/{orderId} | Cancel an order



# **place_new_mtf_order**
> ResNewMTFOrder place_new_mtf_order(consumerKey, sessionToken, NewMTFOrder)

Place a New MTF order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from openapi_client.rest import ApiException
from openapi_client.models import NewMTFOrder

# Place a New MTF order
try:
    order = NewMTFOrder(tag="string", transactionType="BUY", instrumentToken=127,\
            variety="REGULAR", quantity=11, price=100, disclosedQuantity=1, \
            validity="GFD", triggerPrice=98)
    api_response = openapi_client.placeorder(order)
    print(api_response)
except ApiException as e:
    print("Exception when calling MarginTradingApi->place_new_mtf_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**| Unique ID for your application |
 **sessionToken** | **str**| Session ID Generated with successful login. |
 **NewMTFOrder** | [**NewMTFOrder**](NewMTFOrder.md)|  |

### Return type

[**ResNewMTFOrder**](ResNewMTFOrder.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MTF  Order placed successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_mtf_order**
> ResMTFMod modify_mtf_order(consumerKey, sessionToken, ExistingMTFOrder)

Modify an existing MTF order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException
from openapi_client.models import ExistingMTFOrder

# Modify an existing MTF order
try:
    existing_order = ExistingMTFOrder(order_id, disclosedQuantity=1,\
                        price=0, quantity=1, triggerPrice=0)
    api_response = openapi_client.modifyOrder(existing_order)
    print(api_response)
except ApiException as e:
    print("Exception when calling MarginTradingApi->modify_mtf_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**| Unique ID for your application |
 **sessionToken** | **str**| Session ID for your application |
 **ExistingMTFOrder** | [**ExistingMTFOrder**](ExistingMTFOrder.md)|  |

### Return type

[**ResMTFMod**](ResMTFMod.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **cancel_mtf_order**
> ResMTFOrderCancel cancel_mtf_order(consumerKey, sessionToken, orderId)

Cancel an order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException

try:
    api_response = openapi_client.cancel_order(orderId, 'MTFO')
    print(api_response)
except ApiException as e:
    print("Exception when calling MarginTradingApi->cancelOrder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |
 **sessionToken** | **str**|  |
 **orderId** | **str**| Order ID to cancel. |

### Return type

[**ResMTFOrderCancel**](ResMTFOrderCancel.md)

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
