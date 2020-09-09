# openapi_client.NormalOrderApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**place_new_normal_order**](NormalOrderApi.md#place_new_normal_order) | **POST** /orders/1.0/order/normal | Place a New normal order
[**modify_normal_order**](NormalOrderApi.md#modify_normal_order) | **PUT** /orders/1.0/order/normal | Modify an existing normal order
[**cancel_normal_order**](NormalOrderApi.md#cancel_normal_order) | **DELETE** /orders/1.0/order/normal/{orderId} | Cancel a Normal order

# **place_new_normal_order**
> ResNewNormalOrder place_new_normal_order(consumerKey, sessionToken, NewNormalOrder)

Place a New normal order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException
from openapi_client.models import NewNormalOrder

try:
    # Place a New normal order
    order = NewNormalOrder(instrumentToken=727, tag="string", transactionType="BUY",\
                        variety="REGULAR", quantity=12, price=10, disclosedQuantity=10,\
                        validity="GFD", triggerPrice=10)
    api_response = openapi_client.place_order(order)

    print(api_response)
except ApiException as e:
    print("Exception when calling NormalOrderApi->place_new_normal_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**| Unique ID for your application |
 **sessionToken** | **str**| Session ID Generated with successful login. |
 **NewNormalOrder** | [**NewNormalOrder**](NewNormalOrder.md)|  |

### Return type

[**ResNewNormalOrder**](ResNewNormalOrder.md)

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


# **modify_normal_order**
> ResNormalOrderMod modify_normal_order(consumerKey, sessionToken, ExistingNormalOrder)

Modify an existing normal order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException
from openapi_client.models import ExistingOrder

try:
    # Modify an existing normal order
    existing_order = ExistingOrder(order_id, disclosedQuantity=0, price=0,\
            quantity=1, triggerPrice=0)
    api_response = openapi_client.modify_order(existing_order)

    print(api_response)
except ApiException as e:
    print("Exception when calling NormalOrderApi->modify_normal_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**| Unique ID for your application |
 **sessionToken** | **str**| Session ID for your application |
 **ExistingNormalOrder** | [**ExistingNormalOrder**](ExistingNormalOrder.md)|  |

### Return type

[**ResNormalOrderMod**](ResNormalOrderMod.md)

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


# **cancel_normal_order**
> ResNormalOrderCancel cancel_normal_order(consumerKey, sessionToken, orderId)

Cancel a Normal order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException

try:
    # Cancel an Normal order
    # OrderId will be available if order is placed
    api_response = openapi_client.cancel_order(orderId, 'NO')
    print(api_response)
except ApiException as e:
    print("Exception when calling NormalOrderApi->cancel_normal_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |
 **sessionToken** | **str**|  |
 **orderId** | **str**| Order ID to cancel. |

### Return type

[**ResNormalOrderCancel**](ResNormalOrderCancel.md)

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
