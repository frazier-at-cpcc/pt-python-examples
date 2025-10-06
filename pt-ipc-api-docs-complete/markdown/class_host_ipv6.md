# Cisco Packet Tracer Extensions API: HostIpv6 Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_host_ipv6.html

---

##  Public Member Functions  
  
---  
void | [setDefaultGateway](class_host_ipv6.html#ac658b85ff297dcea9aef6d1f689a2f91) (ipv6)  
| Sets the default gateway with the specified IP address. [More...](class_host_ipv6.html#ac658b85ff297dcea9aef6d1f689a2f91)  
  
ipv6 | [getDefaultGateway](class_host_ipv6.html#a6e5364e62b41371eba9d445db6b0df96) () const  
| Returns the IP address of the default gateway. [More...](class_host_ipv6.html#a6e5364e62b41371eba9d445db6b0df96)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Member Function Documentation

## ◆ getDefaultGateway()

ipv6 HostIpv6::getDefaultGateway  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the IP address of the default gateway. 
    
    
        \return ip, the IP address of the default gateway.
    

## ◆ setDefaultGateway()

void HostIpv6::setDefaultGateway  | ( | ipv6  | | ) |   
---|---|---|---|---|---  
  
Sets the default gateway with the specified IP address. 

Parameters
     gatewayIp,the| IP address of the gateway.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CHostIpv6.pki](_c_host_ipv6_8pki.html)


