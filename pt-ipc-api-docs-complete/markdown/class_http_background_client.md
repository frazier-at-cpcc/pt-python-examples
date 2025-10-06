# Cisco Packet Tracer Extensions API: HttpBackgroundClient Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_http_background_client.html

---

##  Additional Inherited Members  
  
---  
Public Member Functions inherited from [HttpClient](class_http_client.html)  
bool | [go](class_http_client.html#a1f5c6ab60321ac684b0d6a42a5f645bb) (string)  
| Creates an HTTP request to the specified URL. [More...](class_http_client.html#a1f5c6ab60321ac684b0d6a42a5f645bb)  
  
bool | [http_get](class_http_client.html#a510b69c8e816089e496f744d0318cc28) (string, string)  
bool | [http_post](class_http_client.html#af72aeb30c51fe625cd3ffe69c523f2f9) (string, string, string)  
bool | [http_delete](class_http_client.html#a5961dffd7fe9d5e5d27ed3da8e385661) (string, string, string)  
bool | [http_put](class_http_client.html#a5e833b04d3523f57d741ed95e607e79f) (string, string, string)  
bool | [cancel](class_http_client.html#a60b2e6c0c510b2b5a679683f9052b80e) ()  
| cancel HTTP request and close tcp connection. [More...](class_http_client.html#a60b2e6c0c510b2b5a679683f9052b80e)  
  
string | [getLastPageContent](class_http_client.html#a1e7ff870c6e039570a073ae10050516c) ()  
| Returns the last page content retrived from an HTTP response. [More...](class_http_client.html#a1e7ff870c6e039570a073ae10050516c)  
  
void | [setHttps](class_http_client.html#abbd89723467a7f39e7260e5250ff661e) (bool)  
| Sets the [HttpClient](class_http_client.html "HttpClient handles and manipulates the HTTP client on devices.") process to use HTTPS if status is true, otherwise HTTP. [More...](class_http_client.html#abbd89723467a7f39e7260e5250ff661e)  
  
bool | [isHttps](class_http_client.html#a80d1df84580ff50648b7aadb0a73cad1) ()  
| Returns true if the [HttpClient](class_http_client.html "HttpClient handles and manipulates the HTTP client on devices.") process is set to HTTPS, false if HTTP. [More...](class_http_client.html#a80d1df84580ff50648b7aadb0a73cad1)  
  
void | [onStart](class_http_client.html#a9f11bbcfa51d6ad5e9b2a54239d40c3c) (string)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_http_client.html#a9f11bbcfa51d6ad5e9b2a54239d40c3c)  
  
void | [onDone](class_http_client.html#a56ee96458f4ca83a762f03eca0596c8d) (string, ip, HttpResponseType, string)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_http_client.html#a56ee96458f4ca83a762f03eca0596c8d)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
* * *

The documentation for this class was generated from the following file:

  * [CHttpBackgroundClient.pki](_c_http_background_client_8pki.html)


