# openapi_client.QuoteApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_instruments_details**](QuoteApi.md#get_instruments_details) | **GET** /quotes/v1.0/instruments/{instrumentTokens} | Get full details
[**get_ltp_quote**](QuoteApi.md#get_ltp_quote) | **GET** /quotes/v1.0/ltp/instruments/{instrumentTokens} | Get LTP quote
[**get_market_details_quote**](QuoteApi.md#get_market_details_quote) | **GET** /quotes/v1.0/depth/instruments/{instrumentTokens} | Get market details quote
[**get_ohlc_quote**](QuoteApi.md#get_ohlc_quote) | **GET** /quotes/v1.0/ohlc/instruments/{instrumentTokens} | Get OHLC quote


# **get_instruments_details**
> list[Instrument] get_instruments_details(consumerKey, sessionToken, instrumentTokens)

Get full details

Get full details

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException

try:
    # Get instrument details
    instrumentTokens=110
    api_response=openapi_client.get_instruments_details(instrumentTokens)
	print(api_response)
except ApiException as e:
	print("Exception when calling QuoteApi->get_instruments_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  | 
 **sessionToken** | **str**|  | 
 **instrumentTokens** | **str**|  | 

### Return type

[**list[Instrument]**](Instrument.md)

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
> list[LTPQuote] get_ltp_quote(consumerKey, sessionToken, instrumentTokens)

Get LTP quote

Returns the LTP for an array of scrips

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException
try:
	# Get LTP quote details
	instrumentTokens=110
    api_response=openapi_client.get_ltp_quote(instrumentTokens)
	print(api_response)
except ApiException as e:
	print("Exception when calling QuoteApi->get_ltp_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  | 
 **sessionToken** | **str**|  | 
 **instrumentTokens** | **str**| Instrument token of the scrip for which quote | 

### Return type

[**list[LTPQuote]**](LTPQuote.md)

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
> MarketDetailsQuote get_market_details_quote(consumerKey, sessionToken, instrumentTokens)

Get market details quote

Returns market depth details for an array of scrips

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException
try:
	# Get market details of quote
	instrumentTokens=110
    api_response=openapi_client.get_market_details(instrumentTokens)
	print(api_response)
except ApiException as e:
	print("Exception when calling QuoteApi->get_market_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  | 
 **sessionToken** | **str**|  | 
 **instrumentTokens** | **str**| Instrument token of the scrip for which quote | 

### Return type

[**MarketDetailsQuote**](MarketDetailsQuote.md)

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
> list[OHLCQuote] get_ohlc_quote(consumerKey, sessionToken, instrumentTokens)

Get OHLC quote

Returns the OHLC quote details for an array of scrips

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException
try:
	# Get OHLC details
	instrumentTokens=110
    api_response=openapi_client.get_ohlc_quote(instrumentTokens)
	print(api_response)
except ApiException as e:
	print("Exception when calling QuoteApi->get_ohlc_quote: %s\n" % e)```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  | 
 **sessionToken** | **str**|  | 
 **instrumentTokens** | **str**| Instrument token of the scrip for which quote | 

### Return type

[**list[OHLCQuote]**](OHLCQuote.md)

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

