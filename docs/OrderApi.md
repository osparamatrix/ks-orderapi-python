# openapi_client.OrderApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**place_new_order**](OrderApi.md#place_new_order) | **POST** /orders/1.0/orders | Place a New order
[**modify_order**](OrderApi.md#modify_order) | **PUT** /orders/1.0/orders | Modify an existing order
[**cancel_order**](OrderApi.md#cancel_order) | **DELETE** /orders/1.0/orders/{orderId} | Cancel an order

# **place_new_order**
> ResNewOrder place_new_order(consumerKey, sessionToken, NewOrder)

Place a New order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python


from openapi_client.rest import ApiException
from openapi_client.models import NewOrder

try:
    # Place a New order
    order = NewOrder(instrumentToken=727, tag="string", transactionType="BUY",\
                                variety="REGULAR", quantity=12, price=10, disclosedQuantity=0,\
                                validity="GFD", triggerPrice=0, product="NORMAL")
    api_response = api_instance.place_order(order)
    print(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->place_new_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**| Unique ID for your application |
 **sessionToken** | **str**| Session ID Generated with successful login. |
 **NewOrder** | [**NewOrder**](NewOrder.md)|  |

### Return type

[**ResNewOrder**](ResNewOrder.md)

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

# **modify_order**
> ResOrderMod modify_order(consumerKey, sessionToken, ExistingOrder)

Modify an existing order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from openapi_client.rest import ApiException
from openapi_client.models import ExistingOrder


try:
    # Modify an existing order
    existing_order = ExistingOrder(order_id, disclosedQuantity=10, price=0,\
                                quantity=100, triggerPrice=10)
    api_response = api_instance.modify_order(existing)
    print(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->modify_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**| Unique ID for your application |
 **sessionToken** | **str**| Session ID for your application |
 **ExistingOrder** | [**ExistingOrder**](ExistingOrder.md)|  |

### Return type

[**ResOrderMod**](ResOrderMod.md)

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

# **cancel_order**
> ResOrderCancel cancel_order(consumerKey, sessionToken, orderId)

Cancel an order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python


from openapi_client.rest import ApiException

try:
    # Cancel order
    # OrderId will be available if order is placed
    api_response = openapi_client.cancel_order(orderId, 'O')

    print(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |
 **sessionToken** | **str**|  |
 **orderId** | **str**| Order ID to cancel. |

### Return type

[**ResOrderCancel**](ResOrderCancel.md)

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
