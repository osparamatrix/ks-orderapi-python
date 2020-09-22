# ks_api_client.PositionsApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method  | Description
------------- | -------------
[**positions**](PositionsApi.md#positions) | Get&#39;s positions.

# **positions**
> object positions(position_type)

Get's positions.

Return positions of provided position type.

### Example


```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                 consumer_key = "consumer_key", ip = "IP", app_id = "app_id", host = "host",\
                 proxy_url = "proxy_url", proxy_user = "proxy_user", proxy_pass = "proxy_pass")

#First initialize session and generate session token

try:
    # Get's position by position_type.
    client.positions(position_type = "TODAYS")
except Exception as e:
    print("Exception when calling PositionsApi->positions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_type** | **str**| Type of position - TODAYS, STOCKS, OPEN | 

### Return type

**object**


### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the Positoin data for a client account. |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
