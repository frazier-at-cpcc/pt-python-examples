# Cisco Packet Tracer Extensions API: UdpProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_udp_process.html

---

[UdpProcess](class_udp_process.html "UdpProcess handles and manipulates the UDP process.") handles and manipulates the UDP process. [More...](class_udp_process.html#details)

##  Public Member Functions  
  
---  
[Process](class_process.html) | [getHigherProcess](class_udp_process.html#a7550e80b4ab5192bbfd69b3b68986038) (int)  
| Returns the higher process at the specified local port. [More...](class_udp_process.html#a7550e80b4ab5192bbfd69b3b68986038)  
  
[CustomUdpProcess](class_custom_udp_process.html) | [createCustomUdpProcess](class_udp_process.html#a2708b65009be68631877d06b86065561) ()  
| Creates a custom UDP process. [More...](class_udp_process.html#a2708b65009be68631877d06b86065561)  
  
void | [deleteCustomUdpProcess](class_udp_process.html#ae51b3d791e2cab58785707b56593025e) ([CustomUdpProcess](class_custom_udp_process.html))  
| Deletes the specified custom UDP process. [More...](class_udp_process.html#ae51b3d791e2cab58785707b56593025e)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[UdpProcess](class_udp_process.html "UdpProcess handles and manipulates the UDP process.") handles and manipulates the UDP process. 

## Member Function Documentation

## ◆ createCustomUdpProcess()

[CustomUdpProcess](class_custom_udp_process.html) UdpProcess::createCustomUdpProcess  | ( | | ) |   
---|---|---|---|---  
  
Creates a custom UDP process. 

Returns
    [CustomUdpProcess](class_custom_udp_process.html "CustomUdpProcess is the process that manipulates the custom UDP process."), the [CustomUdpProcess](class_custom_udp_process.html "CustomUdpProcess is the process that manipulates the custom UDP process.") object. 

## ◆ deleteCustomUdpProcess()

void UdpProcess::deleteCustomUdpProcess  | ( | [CustomUdpProcess](class_custom_udp_process.html) | | ) |   
---|---|---|---|---|---  
  
Deletes the specified custom UDP process. 

Parameters
     process,the| [CustomUdpProcess](class_custom_udp_process.html "CustomUdpProcess is the process that manipulates the custom UDP process.") object to delete.   
---|---  
  
## ◆ getHigherProcess()

[Process](class_process.html) UdpProcess::getHigherProcess  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the higher process at the specified local port. 

Parameters
     localPort,the| local port of the process of interest.  
---|---  
  
Returns
    [Process](class_process.html "Process is the base class for all device processes."), the [Process](class_process.html "Process is the base class for all device processes.") object at the specified local port. 

* * *

The documentation for this class was generated from the following file:

  * [CUdpProcess.pki](_c_udp_process_8pki.html)


