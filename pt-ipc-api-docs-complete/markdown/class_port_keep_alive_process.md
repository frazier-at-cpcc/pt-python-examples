# Cisco Packet Tracer Extensions API: PortKeepAliveProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_port_keep_alive_process.html

---

[PortKeepAliveProcess](class_port_keep_alive_process.html "PortKeepAliveProcess handles the keepalive process on a device port.") handles the keepalive process on a device port. [More...](class_port_keep_alive_process.html#details)

##  Public Member Functions  
  
---  
void | [setKeepAliveOn](class_port_keep_alive_process.html#a35bfb062718b7507ec3f1fd71c62d4f1) (bool)  
bool | [isKeepAliveOn](class_port_keep_alive_process.html#aa9fe1c119e9f3365c4dec1cb65b13752) ()  
| Returns true if keepalive is enabled, otherwise false. [More...](class_port_keep_alive_process.html#aa9fe1c119e9f3365c4dec1cb65b13752)  
  
void | [setKeepAliveInterval](class_port_keep_alive_process.html#a2e003c5aa950a4a7c1548fcee456e667) (int)  
| Sets the keepalive interval. [More...](class_port_keep_alive_process.html#a2e003c5aa950a4a7c1548fcee456e667)  
  
int | [getKeepAliveInterval](class_port_keep_alive_process.html#adb100ad4b49d7678a1dd4059552f9ee1) ()  
| Returns the keepalive interval. [More...](class_port_keep_alive_process.html#adb100ad4b49d7678a1dd4059552f9ee1)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[PortKeepAliveProcess](class_port_keep_alive_process.html "PortKeepAliveProcess handles the keepalive process on a device port.") handles the keepalive process on a device port. 

## Member Function Documentation

## ◆ getKeepAliveInterval()

int PortKeepAliveProcess::getKeepAliveInterval  | ( | | ) |   
---|---|---|---|---  
  
Returns the keepalive interval. 

Returns
    int, the keepalive interval. 

## ◆ isKeepAliveOn()

bool PortKeepAliveProcess::isKeepAliveOn  | ( | | ) |   
---|---|---|---|---  
  
Returns true if keepalive is enabled, otherwise false. 

Returns
    bool, true if keepalive is enabled, otherwise false. 

## ◆ setKeepAliveInterval()

void PortKeepAliveProcess::setKeepAliveInterval  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the keepalive interval. 

Parameters
     interval,the| interval for keepalive.   
---|---  
  
## ◆ setKeepAliveOn()

void PortKeepAliveProcess::setKeepAliveOn  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
\Enables or disables keepalive.

Parameters
     bOn,true| to enable keepalive, false to disable it.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CPortKeepAliveProcess.pki](_c_port_keep_alive_process_8pki.html)


