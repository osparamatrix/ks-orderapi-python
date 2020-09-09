# openapi_client.SuperMultipleOrderApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**place_new_sm_order**](SuperMultipleOrderApi.md#place_new_sm_order) | **POST** /orders/1.0/order/supermultiple | Place a New Super Multiple order
[**modify_sm_order**](SuperMultipleOrderApi.md#modify_sm_order) | **PUT** /orders/1.0/order/supermultiple | Modify an existing super multiple order
[**cancel_sm_order**](SuperMultipleOrderApi.md#cancel_sm_order) | **DELETE** /orders/1.0/order/supermultiple/{orderId} | Cancel an Super Multiple order

# **place_new_sm_order**
> ResNewSMOrder place_new_sm_order(consumerKey, sessionToken, NewSMOrder)

Place a New Super Multiple order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from openapi_client.rest import ApiValueError
from openapi_client.models import NewSMOrder


try:
    # Place a New Super Multiple order
    order = NewSMOrder(tag="string", transactionType="BUY", instrumentToken=727,\
            variety="REGULAR", quantity=1, price=0, disclosedQuantity=0, \
            validity="GFD", triggerPrice=1005)
    api_response = openapi_client.place_order(order)
    print(api_response)
except ApiException as e:
    print("Exception when calling SuperMultipleOrderApi->place_new_sm_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**| Unique ID for your application |
 **sessionToken** | **str**| Session ID Generated with successful login. |
 **NewSMOrder** | [**NewSMOrder**](NewSMOrder.md)|  |

### Return type

[**ResNewSMOrder**](ResNewSMOrder.md)

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
> ResSMOrderMod modify_sm_order(consumerKey, sessionToken, ExistingSMOrder)

Modify an existing super multiple order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException
from openapi_client.models import  ExistingSMOrder

try:
    # Modify an existing super multiple order
    existing_oder = ExistingSMOrder(order_id, disclosedQuantity=0,\
                    price=0, quantity=11, triggerPrice=1000)
    api_response = openapi_client.modify_order(existing_oder)
    print(api_response)
except ApiException as e:
    print("Exception when calling SuperMultipleOrderApi->modify_sm_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**| Unique ID for your application |
 **sessionToken** | **str**| Session ID for your application |
 **ExistingSMOrder** | [**ExistingSMOrder**](ExistingSMOrder.md)|  |

### Return type

[**ResSMOrderMod**](ResSMOrderMod.md)

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
> ResSMOrderCancel cancel_sm_order(consumerKey, sessionToken, orderId)

Cancel an Super Multiple order

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException

try:
    # Cancel an Super Multiple order
    # OrderId will be available if order is placed
    api_response = openapi_client.cancel_order(orderId, 'SMO')
    print(api_response)
except ApiException as e:
    print("Exception when calling SuperMultipleOrderApi->cancel_sm_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |
 **sessionToken** | **str**|  |
 **orderId** | **str**| Order ID to cancel. |

### Return type

[**ResSMOrderCancel**](ResSMOrderCancel.md)

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
