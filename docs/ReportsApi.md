# ks_api_client.ReportsApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order_report**](ReportsApi.md#get_order_report_by_order_id) | **GET** /reports/1.0/orders/{orderId} | Get order report by orderId
[**get_order_report**](ReportsApi.md#get_order_reports) | **GET** /reports/1.0/orders | Get order report
[**get_trade_report**](ReportsApi.md#get_trade_report) | **GET** /reports/1.0/trades | Get trade report
[**get_trade_report**](ReportsApi.md#get_trade_report_by_order_id) | **GET** /reports/1.0/trades/{orderId} | Get trade report by orderId


# **get_order_report_by_order_id**
> object get_order_report(order_id)

Get order report by orderId

Returns the specific order report

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")

#First initialize session and generate session token
try:
    # Get order report by orderId
    client.get_order_report(order_id="order_id")
except Exception as e:
    print("Exception when calling ReportsApi->get_order_report_by_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | order_id if not provided it will call order reports of ReportsApi | [optional]

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
> object get_order_report()

Get order report

Returns the full order report for a client.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")

#First initialize session and generate session token
try:
    # Get order report
    client.get_order_report()
except Exception as e:
    print("Exception when calling ReportsApi->get_order_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


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
> object get_trade_report(order_id="order_id")

Get trade report

Returns the full trade report

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")
				
#First initialize session and generate session token

try:
    # Get trade report
    client.get_trade_report()
except ApiException as e:
    print("Exception when calling ReportsApi->get_trade_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


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
> object get_trade_report(order_id)

Get trade report by orderId

Returns the trade report for a orderId

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")
				
#First initialize session and generate session token

try:
    # Get trade report by orderId
    client.get_trade_report(order_id="order_id")
except ApiException as e:
    print("Exception when calling ReportsApi->get_trade_report_by_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | order_id if not provided it will call trade reports of ReportsApi | [optional]

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
**200** | Trade Report of a client |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
