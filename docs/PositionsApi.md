# openapi_client.PositionsApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**positions**](PositionsApi.md#positions) | **GET** /positions/1.0/positions | Get&#39;s raw position from Trading Engine.
[**positions_open**](PositionsApi.md#positions_open) | **GET** /positions/1.0/positions/open | Get&#39;s Open position.
[**positions_stocks**](PositionsApi.md#positions_stocks) | **GET** /positions/1.0/positions/stocks | Get&#39;s Sell from Existing stocks.
[**positions_today**](PositionsApi.md#positions_today) | **GET** /positions/1.0/positions/todays | Get&#39;s Todays position.


# **positions**
> list[Positions] positions(consumerKey, sessionToken)

Get's raw position from Trading Engine.

Snapshot of Position data for a client available in System.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from openapi_client.rest import ApiException

try:
    # Get's raw position from Trading Engine.
    api_response = openapi_client.positions()
    print(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |
 **sessionToken** | **str**|  |

### Return type

[**list[Positions]**](Positions.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the Raw Positoin data for a client account. |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_open**
> list[Open] positions_open(consumerKey, sessionToken)

Get's Open position.

Gets Open Position of a client.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python


from openapi_client.rest import ApiException

try:
    # Get's Open position.
    api_response = openapi_client.positions_open()
    print(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_open: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |
 **sessionToken** | **str**|  |

### Return type

[**list[Open]**](Open.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the Raw Positoin data for a client account. |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_stocks**
> list[Stocks] positions_stocks(consumerKey, sessionToken)

Get's Sell from Existing stocks.

Gets Stocks position eligible for sell from existing for a client.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python


from openapi_client.rest import ApiException

try:
    # Get's Sell from Existing stocks.
    api_response = openapi_client.positions_stocks()
    print(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_stocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |
 **sessionToken** | **str**|  |

### Return type

[**list[Stocks]**](Stocks.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets Stocks client account. |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_today**
> list[Todays] positions_today(consumerKey, sessionToken)

Get's Todays position.

Gets Today's Position of a client.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python


from openapi_client.rest import ApiException

try:
    # Get's Todays position.
    api_response = openapi_client.positions_today()
    print(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_today: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |
 **sessionToken** | **str**|  |

### Return type

[**list[Todays]**](Todays.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the Raw Positoin data for a client account. |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
