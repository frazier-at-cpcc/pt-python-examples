# Cisco Packet Tracer Extensions API: HttpBackgroundClientManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_http_background_client_manager.html

---

##  Public Member Functions  
  
---  
[HttpClient](class_http_client.html) | [createClient](class_http_background_client_manager.html#a1d3fba5e08ffe13b74b046fec0ed5fb7) ()  
| Returns the HTTPClient object. [More...](class_http_background_client_manager.html#a1d3fba5e08ffe13b74b046fec0ed5fb7)  
  
void | [deleteClient](class_http_background_client_manager.html#af2276b8b717e513c60646dad5e39bbf7) ([HttpClient](class_http_client.html))  
| destroy the HTTPCLient object. [More...](class_http_background_client_manager.html#af2276b8b717e513c60646dad5e39bbf7)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Member Function Documentation

## ◆ createClient()

[HttpClient](class_http_client.html) HttpBackgroundClientManager::createClient  | ( | | ) |   
---|---|---|---|---  
  
Returns the HTTPClient object. 

Returns
    [HttpClient](class_http_client.html "HttpClient handles and manipulates the HTTP client on devices."), the HTTPClient object. 

## ◆ deleteClient()

void HttpBackgroundClientManager::deleteClient  | ( | [HttpClient](class_http_client.html) | | ) |   
---|---|---|---|---|---  
  
destroy the HTTPCLient object. 

Parameters
     [HttpClient](class_http_client.html "HttpClient handles and manipulates the HTTP client on devices."),the| HTTPCLient to destroy.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CHttpBackgroundClientManager.pki](_c_http_background_client_manager_8pki.html)


