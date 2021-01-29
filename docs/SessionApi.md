# ks_api_client.SessionApi

All URIs are relative to *https://tradeapi.kotaksecurities.com/apim*

Method | Description
------------- | -------------
[**ks_api.KSTradeApi**](SessionApi.md#session_init) | Initialise Session
[**login**](SessionApi.md#login) | Login using Userid
[**session_2fa**](SessionApi.md#session_2fa) | Generate final Session Token
[**logout**](SessionApi.md#logout) | Invalidate Session Token


# **session_init**
> ks_api.KSTradeApi(access_token, userid, consumer_key, ip, app_id, host, proxy_url, proxy_user, proxy_pass )

Initialise Session

API to initiate trading session for a User.

### Example


```python
from ks_api_client import ks_api

#the session initializes when following constructor is called
client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                         consumer_key = "consumer_key", ip = "IP", app_id = "app_id")
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **userid** | **str**|  |
 **consumer_key** | **str**|  |
 **ip** | **str**|  |
 **app_id** | **str**|  |
 **host** | **str**| Trade Api Host URL | [optional]
 **proxy_url** | **str**| Proxy url  |  [optional]
 **proxy_user** | **str**| Proxy user's Username | [optional]
 **proxy_pass** | **str**| Proxy user's Password | [optional]
  



### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**400** | Invalid or missing input parameters |  -  |
**401** | Verify resource and path of the request |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **login**
> object login(password)

Login using Userid

Authenticate userid and password to generate one time token.

### Example


```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                         consumer_key = "consumer_key", ip = "IP", app_id = "app_id")

try:
    # Login using password
    client.login(password = "password")
except Exception as e:
    print("Exception when calling SessionApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**|  |

### Return type

object


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User session validated successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**401** | Verify resource and path of the request |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# **session_2fa**
> object session_2fa(access_code)

Generate final Session Token

API to generate final session for user based on one time token.

### Example


```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                         consumer_key = "consumer_key", ip = "IP", app_id = "app_id")
				
try:
    # Login using password
    client.login(password = "password")
    
    # Generate final Session Token
    client.session_2fa(access_code = "access_code")
except Exception as e:
    print("Exception when calling SessionApi->session_2fa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_code** | **str**|  |

### Return type

object


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User session validated successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**401** | Verify resource and path of the request |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **logout**
> object logout()

Invalidate Session Token

API to invalidate final session for user.

### Example


```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = "access_token", userid = "userid", \
                         consumer_key = "consumer_key", ip = "IP", app_id = "app_id")

#First initialize session and generate session token

try:
    # Invalidate Session Tsoken
    client.logout()
except Exception as e:
    print("Exception when calling SessionApi->logout: %s\n" % e)
```


### Return type

object


### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User session invalidated  successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
