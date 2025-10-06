# Cisco Packet Tracer Extensions API: SmtpServer Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_smtp_server.html

---

[SmtpServer](class_smtp_server.html "SmtpServer handles and manipulates the SMTP service.") handles and manipulates the SMTP service. [More...](class_smtp_server.html#details)

##  Public Member Functions  
  
---  
void | [setEnable](class_smtp_server.html#aa29987812b11e33d1aaf43d0a4171253) (bool)  
| Enables or disables the SMTP service. [More...](class_smtp_server.html#aa29987812b11e33d1aaf43d0a4171253)  
  
bool | [isEnabled](class_smtp_server.html#a98564579a5173ae8f7dfcc7289f6a39e) ()  
| Returns true if the SMTP service is enabled, otherwise false. [More...](class_smtp_server.html#a98564579a5173ae8f7dfcc7289f6a39e)  
  
string | [getServerDomainName](class_smtp_server.html#ad33ae4d8a650167b16aebe274fef0333) ()  
| Returns the domain name of the SMTP server. [More...](class_smtp_server.html#ad33ae4d8a650167b16aebe274fef0333)  
  
void | [setServerDomainName](class_smtp_server.html#a06c93db0d2a50c2cf893c838ae9245e7) (string)  
| Sets the domain name for the SMTP server. [More...](class_smtp_server.html#a06c93db0d2a50c2cf893c838ae9245e7)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[SmtpServer](class_smtp_server.html "SmtpServer handles and manipulates the SMTP service.") handles and manipulates the SMTP service. 

## Member Function Documentation

## ◆ getServerDomainName()

string SmtpServer::getServerDomainName  | ( | | ) |   
---|---|---|---|---  
  
Returns the domain name of the SMTP server. 

Returns
    string, the domain name of the SMTP server. 

## ◆ isEnabled()

bool SmtpServer::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the SMTP service is enabled, otherwise false. 

Parameters
     bool,true| if the SMTP service is enabled, otherwise false.   
---|---  
  
## ◆ setEnable()

void SmtpServer::setEnable  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the SMTP service. 

Parameters
     bEnable,true| to enable the SMTP service, false to disable it.   
---|---  
  
## ◆ setServerDomainName()

void SmtpServer::setServerDomainName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the domain name for the SMTP server. 

Parameters
     name,the| domain name for the SMTP server.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CSmtpServer.pki](_c_smtp_server_8pki.html)


