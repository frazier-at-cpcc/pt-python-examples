# Cisco Packet Tracer Extensions API: HostIp Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_host_ip.html

---

[HostIp](class_host_ip.html "HostIp handles and manipulates the default gateway on end devices.") handles and manipulates the default gateway on end devices. [More...](class_host_ip.html#details)

##  Public Member Functions  
  
---  
void | [setDefaultGateway](class_host_ip.html#a4d56b98e03293c102842522c7f99894f) (ip)  
| Sets the default gateway with the specified IP address. [More...](class_host_ip.html#a4d56b98e03293c102842522c7f99894f)  
  
ip | [getDefaultGateway](class_host_ip.html#a3d13c9837560aafd79ff661f739a6488) ()  
| Returns the IP address of the default gateway. [More...](class_host_ip.html#a3d13c9837560aafd79ff661f739a6488)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[HostIp](class_host_ip.html "HostIp handles and manipulates the default gateway on end devices.") handles and manipulates the default gateway on end devices. 

## Member Function Documentation

## ◆ getDefaultGateway()

ip HostIp::getDefaultGateway  | ( | | ) |   
---|---|---|---|---  
  
Returns the IP address of the default gateway. 

Returns
    ip, the IP address of the default gateway. 

## ◆ setDefaultGateway()

void HostIp::setDefaultGateway  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the default gateway with the specified IP address. 

Parameters
     gatewayIp,the| IP address of the gateway.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CHostIp.pki](_c_host_ip_8pki.html)


