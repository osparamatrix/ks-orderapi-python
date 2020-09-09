# openapi_client.MarginApi

All URIs are relative to *https://sbx.kotaksecurities.com/apim*

Method | HTTP request | Description
------------- | ------------- | -------------
[**margin_required**](MarginApi.md#margin_required) | **POST** /margin/1.0/margin/required | Get Margin Required for an order by amount or quantity.


# **margin_required**
> list[MarginDet] margin_required(consumerKey, sessionToken, ReqMargin=ReqMargin)

Get Margin Required for an order by amount or quantity.

Returns margin required for Equity, Super Multiple & MTF Order.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from openapi_client.rest import ApiException
from openapi_client.models import  ReqMargin

try:
    # Get Margin Required for an order by amount or quantity.
    orderInfo = [
        {"instrumentToken": 771, "quantity": 1, "price": 1300, "amount": 0, "triggerPrice": 1190},
        {"instrumentToken": 374, "quantity": 1, "price": 1200, "amount": 0, "triggerPrice": 1150}
        ]
    margin_request = ReqMargin(transactionType="BUY",orderInfo=orderInfo)
    api_response = openapi_client.margin_required(margin_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->margin_required: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumerKey** | **str**|  |
 **sessionToken** | **str**|  |
 **ReqMargin** | [**ReqMargin**](ReqMargin.md)|  | [optional]

### Return type

[**list[MarginDet]**](MarginDet.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the Margin required by client for order. |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
