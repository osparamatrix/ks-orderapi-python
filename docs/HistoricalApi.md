# ks_api_client.HistoricalApi

All URIs are relative to *https://tradeapi.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resource**](HistoricalApi.md#get_resource) | **GET** /trade/1.0.0/equity/{resource}/i/{input} | Get historical data


# **get_resource**
> object get_resource(resource, input)

Get historical data

Get Historical data

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import ks_api_client
from ks_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://tradeapi.kotaksecurities.com/apim
# See configuration.py for a list of all supported configuration parameters.
configuration = ks_api_client.Configuration(
    host = "https://tradeapi.kotaksecurities.com/apim"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = ks_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ks_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ks_api_client.HistoricalApi(api_client)
    resource = 'resource_example' # str | 
input = 'input_example' # str | 

    try:
        # Get historical data
        api_response = api_instance.get_resource(resource, input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HistoricalApi->get_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **input** | **str**|  | 

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
**200** | Historicl Details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

