# openapi_client.SessionApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**session_init**](SessionApi.md#session_init) | **GET** /session/1.0/session/init | Initialise Session
[**login_with_user_id**](SessionApi.md#login_with_user_id) | **POST** /session/1.0/session/login/userid | Login using Userid
[**generate_session2_fa**](SessionApi.md#generate_session2_fa) | **POST** /session/1.0/session/2FA/accesscode | Generate final Session Token
[**session_logout**](SessionApi.md#session_logout) | **DELETE** /session/1.0/session/logout | Invalidate Session Token


# **session_init**
> ResSessionInit session_init(userid, consumerKey, ip, appId)

Initialise Session

API to initiate trading session for a UserId

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from openapi_client.api.api import KSTradeApi as TradingApi
from openapi_client.settings import host, access_token, userid, \
                        consumer_key, app_id, access_code
# Defining the host is optional and defaults to https://sbx.kotaksecurities.com/apim
# See configuration.py for a list of all supported configuration parameters.
openapi_client = TradingApi(host, access_token, userid, consumer_key, app_id)
# Enter a context with an instance of the API client
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  |
 **consumerKey** | **str**|  |
 **ip** | **str**|  |
 **appId** | **str**|  |

### Return type

[**ResSessionInit**](ResSessionInit.md)

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
> ResLogin login_with_user_id(consumerKey, ip, appId, UserCredentials=UserCredentials)

Login using Userid

Authenticate userid and password to gnerrated one time token

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from openapi_client.rest import ApiException

try:
    # Login using password
    api_response = openapi_client.session_login_user(password)
    print(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->login_with_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |
 **ip** | **str**|  |
 **appId** | **str**|  |
 **UserCredentials** | [**UserCredentials**](UserCredentials.md)|  | [optional]

### Return type

[**ResLogin**](ResLogin.md)

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
> ResSession2FA generate_session2_fa(oneTimeToken, consumerKey, ip, appId, UserDetails=UserDetails)

Generate final Session Token

API to generate final session for user based on one time token

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from openapi_client.rest import ApiException


try:
    # Generate final Session Token
    api_response = openapi_client.generate_session2_fa(access_code)
    print(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->generate_session2_fa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oneTimeToken** | **str**|  |
 **consumerKey** | **str**|  |
 **ip** | **str**|  |
 **appId** | **str**|  |
 **UserDetails** | [**UserDetails**](UserDetails.md)|  | [optional]

### Return type

[**ResSession2FA**](ResSession2FA.md)

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
> ResLogout session_logout(sessionToken, consumerKey, ip, appId, userid)

Invalidate Session Token

API to invalidate final session for user.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python

from openapi_client.rest import ApiException

try:
    # Invalidate Session Tsoken
    api_response = openapi_client.session_logout()
    print(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->session_logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sessionToken** | **str**|  |
 **consumerKey** | **str**|  |
 **ip** | **str**|  |
 **appId** | **str**|  |
 **userid** | **str**|  |

### Return type

[**ResLogout**](ResLogout.md)

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
