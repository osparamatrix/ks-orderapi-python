# ks_api_client.SessionApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ks_api.KSTradeApi**](SessionApi.md#session_init) | **GET** /session/1.0/session/init | Initialise Session
[**login**](SessionApi.md#login_with_user_id) | **POST** /session/1.0/session/login/userid | Login using Userid
[**generate_session2_fa**](SessionApi.md#generate_session2_fa) | **POST** /session/1.0/session/2FA/accesscode | Generate final Session Token
[**logout**](SessionApi.md#session_logout) | **DELETE** /session/1.0/session/logout | Invalidate Session Token


# **session_init**
> ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")

Initialise Session

API to initiate trading session for a UserId

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from ks_api_client import ks_api

#the session initializes when following constructor is called
client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  |
 **consumer_key** | **str**|  |
 **ip** | **str**|  |
 **app_id** | **str**|  |
 **access_token** | **str**|  |


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_with_user_id**
> object login(password)

Login using Userid

Authenticate userid and password to gnerrated one time token

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")

try:
    # Login using password
    client.login(password)
except Exception as e:
    print("Exception when calling SessionApi->login_with_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**|  |

### Return type

object

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **generate_session2_fa**
> object generate_session2_fa(access_code)

Generate final Session Token

API to generate final session for user based on one time token

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")
				
try:
    # Generate final Session Token
    client.generate_session2_fa(access_code)
except Exception as e:
    print("Exception when calling SessionApi->generate_session2_fa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_code** | **str**|  |

### Return type

object

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_logout**
> object logout()

Invalidate Session Token

API to invalidate final session for user.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token="access_token", userid="userid", \
                consumer_key="consumer_key", app_id="app_id", ip="IP")

#First initialize session and generate session token

try:
    # Invalidate Session Tsoken
    client.logout()
except Exception as e:
    print("Exception when calling SessionApi->session_logout: %s\n" % e)
```


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
**200** | User session invalidated  successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
