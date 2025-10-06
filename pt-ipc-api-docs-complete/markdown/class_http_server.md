# Cisco Packet Tracer Extensions API: HttpServer Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_http_server.html

---

[HttpServer](class_http_server.html "HttpServer handles and manipulates the HTTP server on devices.") handles and manipulates the HTTP server on devices. [More...](class_http_server.html#details)

##  Public Member Functions  
  
---  
void | [setPortNumber](class_http_server.html#a570a767e4f1cefb19e8ac875ad7a6f56) (short)  
| Sets the port number of the HTTP service. [More...](class_http_server.html#a570a767e4f1cefb19e8ac875ad7a6f56)  
  
short | [getPortNumber](class_http_server.html#a9bf97ddc1429f00b624d7393202d2148) ()  
| Returns the port number of the HTTP service. [More...](class_http_server.html#a9bf97ddc1429f00b624d7393202d2148)  
  
void | [setEnable](class_http_server.html#a508402a99a3069e3f6a1eaaff9edfc9a) (bool)  
| Enables or disables the HTTP service. [More...](class_http_server.html#a508402a99a3069e3f6a1eaaff9edfc9a)  
  
bool | [isEnabled](class_http_server.html#a18837146283d847cb0ed337d7d09373c) ()  
| Returns true if the HTTP service is enabled, otherwise false. [More...](class_http_server.html#a18837146283d847cb0ed337d7d09373c)  
  
string | [getPage](class_http_server.html#afad0f3c6c161aaf3741abfa8ff5778cc) (string)  
| Returns the page contents at the specified URL. [More...](class_http_server.html#afad0f3c6c161aaf3741abfa8ff5778cc)  
  
void | [setPageContents](class_http_server.html#a6858cfab98790a21be7afc575343507c) (string, string)  
| Sets the page contents at the specified URL. [More...](class_http_server.html#a6858cfab98790a21be7afc575343507c)  
  
string | [getUsername](class_http_server.html#ace36c7d20c054f3f93cb2422755b50d0) ()  
| Returns the htaccess username for the HTTP server. [More...](class_http_server.html#ace36c7d20c054f3f93cb2422755b50d0)  
  
string | [getPassword](class_http_server.html#a4ba5bfece059737792e7f11918bb6b5e) ()  
| Returns the htaccess password for the HTTP server. [More...](class_http_server.html#a4ba5bfece059737792e7f11918bb6b5e)  
  
void | [setUsername](class_http_server.html#a20aaebae649e79ebd93032d68b43f0c1) (string)  
| Sets the htaccess username for the HTTP server. [More...](class_http_server.html#a20aaebae649e79ebd93032d68b43f0c1)  
  
void | [setPassword](class_http_server.html#a27fd2377a406e679524629db8f687d55) (string)  
| Sets the htaccess password for the HTTP server. [More...](class_http_server.html#a27fd2377a406e679524629db8f687d55)  
  
void | [sendResponse](class_http_server.html#a86db0546aab65daf1f6003621b30baf2) ([TcpConnection](class_tcp_connection.html), string)  
| send the HTTP response back to client with given content. [More...](class_http_server.html#a86db0546aab65daf1f6003621b30baf2)  
  
void | [sendTypedResponse](class_http_server.html#a801438218dabd07532755e11fb3fba80) ([TcpConnection](class_tcp_connection.html), string, string)  
| send the HTTP response back to client with given content and content type. [More...](class_http_server.html#a801438218dabd07532755e11fb3fba80)  
  
void | [sendFileResponse](class_http_server.html#adbb5e07da4f73bdc7ee54b34927b7dd6) ([TcpConnection](class_tcp_connection.html), string)  
| send the HTTP response back to client with given file. [More...](class_http_server.html#adbb5e07da4f73bdc7ee54b34927b7dd6)  
  
void | [sendNotFoundResponse](class_http_server.html#a1a37f3bdea8a072b76777138808fd2d1) ([TcpConnection](class_tcp_connection.html))  
| send the 404 not found HTTP response back to client with given file. [More...](class_http_server.html#a1a37f3bdea8a072b76777138808fd2d1)  
  
bool | [onRequest](class_http_server.html#a9ba822591d38f35e8aa4b92499bad38b) (string, [TcpConnection](class_tcp_connection.html))  
| This delegate pass the url and tcp connection on HTTP request and returns true if successful, otherwise false. [More...](class_http_server.html#a9ba822591d38f35e8aa4b92499bad38b)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[HttpServer](class_http_server.html "HttpServer handles and manipulates the HTTP server on devices.") handles and manipulates the HTTP server on devices. 

## Member Function Documentation

## ◆ getPage()

string HttpServer::getPage  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the page contents at the specified URL. 

Parameters
     url,the| URL of the page of interest.  
---|---  
  
Returns
    string, the page contents at the specified URL. 

## ◆ getPassword()

string HttpServer::getPassword  | ( | | ) |   
---|---|---|---|---  
  
Returns the htaccess password for the HTTP server. 

Returns
    string, the htaccess password for the HTTP server. 

## ◆ getPortNumber()

short HttpServer::getPortNumber  | ( | | ) |   
---|---|---|---|---  
  
Returns the port number of the HTTP service. 

Returns
    int, the port number of the HTTP service. 

## ◆ getUsername()

string HttpServer::getUsername  | ( | | ) |   
---|---|---|---|---  
  
Returns the htaccess username for the HTTP server. 

Returns
    string, the htaccess username for the HTTP server. 

## ◆ isEnabled()

bool HttpServer::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the HTTP service is enabled, otherwise false. 

Returns
    bool, true if the HTTP service is enabled, otherwise false. 

## ◆ onRequest()

bool HttpServer::onRequest  | ( | string  | ,   
---|---|---|---  
|  | [TcpConnection](class_tcp_connection.html) |   
| ) | |   
  
This delegate pass the url and tcp connection on HTTP request and returns true if successful, otherwise false. 

  * url, the url of the HTTP connection. 
  * connection, connection, the Tcp connection of the HTTP connection.



Returns
    bool, true if successful, otherwise false. 

## ◆ sendFileResponse()

void HttpServer::sendFileResponse  | ( | [TcpConnection](class_tcp_connection.html) | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
send the HTTP response back to client with given file. 

Parameters
     connection,the| Tcp connection of the HTTP response.   
---|---  
filePath,the| file get send in the HTTP response.   
  
  
## ◆ sendNotFoundResponse()

void HttpServer::sendNotFoundResponse  | ( | [TcpConnection](class_tcp_connection.html) | | ) |   
---|---|---|---|---|---  
  
send the 404 not found HTTP response back to client with given file. 

Parameters
     connection,the| Tcp connection of the HTTP response.   
---|---  
  
## ◆ sendResponse()

void HttpServer::sendResponse  | ( | [TcpConnection](class_tcp_connection.html) | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
send the HTTP response back to client with given content. 

Parameters
     connection,the| Tcp connection of the HTTP response.   
---|---  
content,the| content of the HTTP response.   
  
## ◆ sendTypedResponse()

void HttpServer::sendTypedResponse  | ( | [TcpConnection](class_tcp_connection.html) | ,   
---|---|---|---  
|  | string  | ,   
|  | string  |   
| ) | |   
  
send the HTTP response back to client with given content and content type. 

Parameters
     connection,the| Tcp connection of the HTTP response.   
---|---  
content,the| content of the HTTP response.   
  
contentType,the| contentType of the HTTP response.   
  
  
## ◆ setEnable()

void HttpServer::setEnable  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the HTTP service. 

Parameters
     bEnable,true| to enable the HTTP service, false to disable it.   
---|---  
  
## ◆ setPageContents()

void HttpServer::setPageContents  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Sets the page contents at the specified URL. 

Parameters
     url,the| URL of the page of interest.   
---|---  
contents,the| contents of the page of interest.   
  
## ◆ setPassword()

void HttpServer::setPassword  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the htaccess password for the HTTP server. 

Parameters
     password,the| htaccess password for the HTTP server.   
---|---  
  
## ◆ setPortNumber()

void HttpServer::setPortNumber  | ( | short  | | ) |   
---|---|---|---|---|---  
  
Sets the port number of the HTTP service. 

Parameters
     num,the| port number to set the HTTP service to.   
---|---  
  
## ◆ setUsername()

void HttpServer::setUsername  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the htaccess username for the HTTP server. 

Parameters
     username,the| htaccess username for the HTTP server.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CHttpServer.pki](_c_http_server_8pki.html)


