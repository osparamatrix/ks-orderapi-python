# ks_api_client.PositionsApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**positions_open**](PositionsApi.md#positions_open) | **GET** /positions/1.0/positions/open | Get&#39;s Open position.
[**positions_stocks**](PositionsApi.md#positions_stocks) | **GET** /positions/1.0/positions/stocks | Get&#39;s Sell from Existing stocks.
[**positions_today**](PositionsApi.md#positions_today) | **GET** /positions/1.0/positions/todays | Get&#39;s Todays position.

# **positions_open**
> object get_positions(position_type)
>Note : 
>		position_type are as follows :
>			"OPEN" : To get open position
>			"STOCKS" : To get stocks position
>			"TODAYS" : To get Todays position

Get's Open position.

Gets Open Position of a client.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")

#First initialize session and generate session token

try:
    # Get's Open position.
    client.get_positions(position_type = "OPEN")
except Exception as e:
    print("Exception when calling PositionsApi->positions_open: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_type** | **str**|  | 

### Return type

**object**

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
> object get_positions(position_type)
>Note : 
>		position_type are as follows :
>			"OPEN" : To get open position
>			"STOCKS" : To get stocks position
>			"TODAYS" : To get Todays position

Get's Sell from Existing stocks.

Gets Stocks position eligible for sell from existing for a client.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")

#First initialize session and generate session token

try:
    # Get's Sell from Existing stocks.
    client.get_positions(position_type = "STOCKS")
except Exception as e:
    print("Exception when calling PositionsApi->positions_stocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |

### Return type

**object**

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
> object get_positions(position_type)
>Note : 
>		position_type are as follows :
>			"OPEN" : To get open position
>			"STOCKS" : To get stocks position
>			"TODAYS" : To get Todays position

Get's Todays position.

Gets Today's Position of a client.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")

#First initialize session and generate session token
try:
    # Get's Todays position.
    client.get_positions(position_type = "TODAYS")
except Exception as e:
    print("Exception when calling PositionsApi->positions_today: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_type** | **str**|  | 

### Return type

**object**

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
