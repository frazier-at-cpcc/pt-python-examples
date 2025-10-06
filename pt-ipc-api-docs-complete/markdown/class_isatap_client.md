# Cisco Packet Tracer Extensions API: IsatapClient Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_isatap_client.html

---

[IsatapClient](class_isatap_client.html "IsatapClient is the class that handles the ISATAP client.") is the class that handles the ISATAP client. [More...](class_isatap_client.html#details)

##  Public Member Functions  
  
---  
bool | [setIsatapRouter](class_isatap_client.html#a4aac91ef6fa5fdf27a49e3eac3e06e63) (ip)  
| Sets the ISATAP router IP address. [More...](class_isatap_client.html#a4aac91ef6fa5fdf27a49e3eac3e06e63)  
  
ip | [getIsatapRouter](class_isatap_client.html#a659cd40c3c7b43bd8315b4f82ff0eb99) ()  
| Returns the IP address of the ISATAP router. [More...](class_isatap_client.html#a659cd40c3c7b43bd8315b4f82ff0eb99)  
  
ip | [getPrefix](class_isatap_client.html#a16f313905844daa8ce9d4dde7fd06f96) ()  
| Returns the subnet prefix. [More...](class_isatap_client.html#a16f313905844daa8ce9d4dde7fd06f96)  
  
void | [setPrefix](class_isatap_client.html#a4b951befbb8f47b5087c84c1a344b1e6) (ip)  
| Sets the subnet prefix. [More...](class_isatap_client.html#a4b951befbb8f47b5087c84c1a344b1e6)  
  
bool | [isEnabled](class_isatap_client.html#a5f01796ca316650b21fe9cb9f78d1c7f) ()  
| Returns true if the ISATAP client is enabled, otherwise false. [More...](class_isatap_client.html#a5f01796ca316650b21fe9cb9f78d1c7f)  
  
void | [setEnabled](class_isatap_client.html#a85fd940afd9af7dbf87cb31e28ef9e2d) (bool)  
| Enables or disables the ISATAP client. [More...](class_isatap_client.html#a85fd940afd9af7dbf87cb31e28ef9e2d)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[IsatapClient](class_isatap_client.html "IsatapClient is the class that handles the ISATAP client.") is the class that handles the ISATAP client. 

## Member Function Documentation

## ◆ getIsatapRouter()

ip IsatapClient::getIsatapRouter  | ( | | ) |   
---|---|---|---|---  
  
Returns the IP address of the ISATAP router. 

Returns
    ip, the IP address of the ISATAP router. 

## ◆ getPrefix()

ip IsatapClient::getPrefix  | ( | | ) |   
---|---|---|---|---  
  
Returns the subnet prefix. 

Returns
    ip, the the subnet prefix. 

## ◆ isEnabled()

bool IsatapClient::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the ISATAP client is enabled, otherwise false. 

Returns
    bool, true if the ISATAP client is enabled, otherwise false. 

## ◆ setEnabled()

void IsatapClient::setEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the ISATAP client. 

Parameters
     flag,true| to enable the ISATAP client, false to disable it.   
---|---  
  
## ◆ setIsatapRouter()

bool IsatapClient::setIsatapRouter  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the ISATAP router IP address. 

Parameters
     ip,the| IP address of the ISATAP router.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ setPrefix()

void IsatapClient::setPrefix  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the subnet prefix. 

Parameters
     ip,the| subnet prefix.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CIsatapClient.pki](_c_isatap_client_8pki.html)


