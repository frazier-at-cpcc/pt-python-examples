# Cisco Packet Tracer Extensions API: NdProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_nd_process.html

---

##  Public Member Functions  
  
---  
void | [autoConfigFailed](class_nd_process.html#a3ae453268ba06660af4566f9937f0b25) (QString, string)  
| Event triggered when autoconfig fails. [More...](class_nd_process.html#a3ae453268ba06660af4566f9937f0b25)  
  
void | [autoConfigSucceed](class_nd_process.html#a63b9bfaaa9d2724e9ab2b0b3e3c6a4d3) (QString, string, ipv6, int)  
| Event triggered when autoconfig succeeds. [More...](class_nd_process.html#a63b9bfaaa9d2724e9ab2b0b3e3c6a4d3)  
  
bool | [isNdProcessEnabledOnHost](class_nd_process.html#a75a46e9e5dc6f1ccc3e37c35c61d736e) ()  
| Gets if the process is enabled on the host. [More...](class_nd_process.html#a75a46e9e5dc6f1ccc3e37c35c61d736e)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Member Function Documentation

## ◆ autoConfigFailed()

void NdProcess::autoConfigFailed  | ( | QString  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Event triggered when autoconfig fails. 

  * deviceName, name of the device the event was triggered for. 
  * portName, name of the port the event was triggered for.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ autoConfigSucceed()

void NdProcess::autoConfigSucceed  | ( | QString  | ,   
---|---|---|---  
|  | string  | ,   
|  | ipv6  | ,   
|  | int  |   
| ) | |   
  
Event triggered when autoconfig succeeds. 

  * deviceName, name of the device the event was triggered for. 
  * portName, name of the port the event was triggered for. 
  * newip, the new ip address. 
  * prefix, the prefix.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ isNdProcessEnabledOnHost()

bool NdProcess::isNdProcessEnabledOnHost  | ( | | ) |   
---|---|---|---|---  
  
Gets if the process is enabled on the host. 

Returns
    bool, value is true if the process is enabled, false if not. 

* * *

The documentation for this class was generated from the following file:

  * [CNdProcess.pki](_c_nd_process_8pki.html)


