# ks_api_client.QuoteApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quote**](QuoteApi.md#get_instruments_details) | **GET** /quotes/v1.0/instruments/{instrumentTokens} | Get full details
[**get_quote**](QuoteApi.md#get_ltp_quote) | **GET** /quotes/v1.0/ltp/instruments/{instrumentTokens} | Get LTP quote
[**get_quote**](QuoteApi.md#get_market_details_quote) | **GET** /quotes/v1.0/depth/instruments/{instrumentTokens} | Get market details quote
[**get_quote**](QuoteApi.md#get_ohlc_quote) | **GET** /quotes/v1.0/ohlc/instruments/{instrumentTokens} | Get OHLC quote


# **get_instruments_details**
> object get_quote(instrument_token)

Get full details

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")

#First initialize session and generate session token

try:
    # Get instrument details
    client.get_quote(instrument_token=110)
except Exception as e:
	print("Exception when calling QuoteApi->get_instruments_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_token** | **str**|  | 

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
**200** | Instrument Details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ltp_quote**
> object get_quote(instrument_token, quote_type)

Get LTP quote

Returns the LTP for an array of scrips

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")
				
#First initialize session and generate session token

try:
	# Get LTP quote details
    client.get_quote(instrument_token=110, quote_type = "LTP")
except Exception as e:
	print("Exception when calling QuoteApi->get_ltp_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_token** | **str**| Instrument token of the scrip for which quote | 
 **quote_type** | **str** |  quote_type is "LTP" if not provided it will call instrument details of QuoteAPI | [optional]

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
**200** | LTP Quote fetched successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_details_quote**
> object get_quote(instrument_token, quote_type)

Get market details quote

Returns market depth details for an array of scrips

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")
				
#First initialize session and generate session token
try:
	# Get market details of quote
    client.get_quote(instrument_token=110, quote_type = "DEPTH")
except Exception as e:
	print("Exception when calling QuoteApi->get_market_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_token** | **str**| Instrument token of the scrip for which quote | 
 **quote_type** | **str** |  quote_type is "DEPTH" if not provided it will call instrument details of QuoteAPI | [optional]
 
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
**200** | Full Quote fetched successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ohlc_quote**
> object get_ohlc_quote(instrument_token, quote_type)

Get OHLC quote

Returns the OHLC quote details for an array of scrips

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")
				
#First initialize session and generate session token
try:
	# Get OHLC details
    client.get_quote(instrument_token=110, quote_type = "OHLC")
except Exception as e:
	print("Exception when calling QuoteApi->get_ohlc_quote: %s\n" % e)```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_token** | **str**| Instrument token of the scrip for which quote | 
 **quote_type** | **str** |  quote_type is "OHLC" if not provided it will call instrument details of QuoteAPI | [optional]
  

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
**200** | OHLC Quote fetched successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

