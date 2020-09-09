# openapi_client.SmartOrderRoutingApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**place_new_sor_order**](SmartOrderRoutingApi.md#place_new_sor_order) | **POST** /orders/1.0/order/sor | Place a New SOR order
[**modify_sor_order**](SmartOrderRoutingApi.md#modify_sor_order) | **PUT** /orders/1.0/order/sor | Modify an existing SOR order
[**cancel_sor_order**](SmartOrderRoutingApi.md#cancel_sor_order) | **DELETE** /orders/1.0/order/sor/{orderId} | Cancel an SORorder


# **place_new_sor_order**
> ResNewSOROrder place_new_sor_order(consumerKey, sessionToken, NewSOROrder)

Place a New SOR order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException
from openapi_client.models import NewSOROrder

try:
    order = NewSOROrder(tag="string", transactionType="BUY", instrumentToken=727,\
                variety="REGULAR", quantity=1, price=0, validity="GFD")
    api_response = openapi_client.place_order(order)
    print(api_response)
except ApiException as e:
    print("Exception when calling SmartOrderRoutingApi->place_new_sor_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**| Unique ID for your application |
 **sessionToken** | **str**| Session ID Generated with successful login. |
 **NewSOROrder** | [**NewSOROrder**](NewSOROrder.md)|  |

### Return type

[**ResNewSOROrder**](ResNewSOROrder.md)

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

# **modify_sor_order**
> ResSOROrderMod modify_sor_order(consumerKey, sessionToken, ExistingSOROrder)

Modify an existing SOR order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time

from openapi_client.rest import ApiException
from openapi_client.models import ExistingSOROrder

try:
    # Modify an existing SOR order
    existing_oder = ExistingSOROrder(order_id, price=0, quantity=1)
    api_response = openapi_client.modify_order(existing_oder)
    print(api_response)
except ApiException as e:
    print("Exception when calling SmartOrderRoutingApi->modify_sor_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**| Unique ID for your application |
 **sessionToken** | **str**| Session ID for your application |
 **ExistingSOROrder** | [**ExistingSOROrder**](ExistingSOROrder.md)|  |

### Return type

[**ResSOROrderMod**](ResSOROrderMod.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SOR Order modified successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_sor_order**
> ResSOROrderCancel cancel_sor_order(consumerKey, sessionToken, orderId)

Cancel an SORorder

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from openapi_client.rest import ApiException

try:
    # Cancel an SORorder
    # OrderId will be available if order is placed
    api_response = openapi_client.cancel_order(orderId, 'SORO')
    print(api_response)
except ApiException as e:
    print("Exception when calling SmartOrderRoutingApi->cancel_sor_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |
 **sessionToken** | **str**|  |
 **orderId** | **str**| Order ID to cancel. |

### Return type

[**ResSOROrderCancel**](ResSOROrderCancel.md)

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
