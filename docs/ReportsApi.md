# openapi_client.ReportsApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order_report_by_order_id**](ReportsApi.md#get_order_report_by_order_id) | **GET** /reports/1.0/orders/{orderId} | Get order report by orderId
[**get_order_reports**](ReportsApi.md#get_order_reports) | **GET** /reports/1.0/orders | Get order report
[**get_trade_report**](ReportsApi.md#get_trade_report) | **GET** /reports/1.0/trades | Get trade report
[**get_trade_report_by_order_id**](ReportsApi.md#get_trade_report_by_order_id) | **GET** /reports/1.0/trades/{orderId} | Get trade report by orderId


# **get_order_report_by_order_id**
> list[Orders] get_order_report_by_order_id(orderId, consumerKey, sessionToken)

Get order report by orderId

Returns the specific order report

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException

try:
    # Get order report by orderId
    api_response = openapi_client.get_order_report_by_order_id(orderId)
    print(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_order_report_by_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderId** | **str**|  |
 **consumerKey** | **str**|  |
 **sessionToken** | **str**|  |

### Return type

[**list[Orders]**](Orders.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order Report of a client |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_reports**
> list[Orders] get_order_reports(consumerKey, sessionToken)

Get order report

Returns the full order report for a client.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time

from openapi_client.rest import ApiException

try:
    # Get order report
    api_response = openapi_client.get_order_reports()
    print(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_order_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |
 **sessionToken** | **str**|  |

### Return type

[**list[Orders]**](Orders.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order Report of a client |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trade_report**
> list[Trades] get_trade_report(consumerKey=consumerKey, sessionToken=sessionToken)

Get trade report

Returns the full trade report

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException

try:
    # Get trade report
    api_response = openapi_client.get_trade_report()
    print(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_trade_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**| Unique ID for your application | [optional]
 **sessionToken** | **str**| Session ID for your application | [optional]

### Return type

[**list[Trades]**](Trades.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Trade Report of a client |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trade_report_by_order_id**
> list[Trades] get_trade_report_by_order_id(orderId, consumerKey, sessionToken)

Get trade report by orderId

Returns the trade report for a orderId

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException

try:
    # Get trade report by orderId
    api_response = openapi_client.get_trade_report_by_order_id(orderId)
    print(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_trade_report_by_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderId** | **str**|  |
 **consumerKey** | **str**| Unique ID for your application |
 **sessionToken** | **str**| Session ID for your application |

### Return type

[**list[Trades]**](Trades.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Trade Report of a client |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
