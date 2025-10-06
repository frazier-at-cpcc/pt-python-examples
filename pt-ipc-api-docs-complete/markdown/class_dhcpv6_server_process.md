# Cisco Packet Tracer Extensions API: Dhcpv6ServerProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_dhcpv6_server_process.html

---

[Dhcpv6ServerProcess](class_dhcpv6_server_process.html "Dhcpv6ServerProcess handles the DHCPv6 server process.") handles the DHCPv6 server process. [More...](class_dhcpv6_server_process.html#details)

##  Public Member Functions  
  
---  
void | [enableDhcpServer](class_dhcpv6_server_process.html#aad48f139fb5cb5d48f6dc0035ae6e311) (bool, [HostPort](class_host_port.html), std::string &)  
| Enables/Disables DHCPv6 server. [More...](class_dhcpv6_server_process.html#aad48f139fb5cb5d48f6dc0035ae6e311)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[Dhcpv6ServerProcess](class_dhcpv6_server_process.html "Dhcpv6ServerProcess handles the DHCPv6 server process.") handles the DHCPv6 server process. 

## Member Function Documentation

## ◆ enableDhcpServer()

void Dhcpv6ServerProcess::enableDhcpServer  | ( | bool  | ,   
---|---|---|---  
|  | [HostPort](class_host_port.html) | ,   
|  | std::string & |   
| ) | |   
  
Enables/Disables DHCPv6 server. 

  * enable, flag to enable or disable the DHCPv6 client 

Parameters
     pPort| the port that the DHCPv6 server resides on   
---|---  
poolName| the DHCPv6 pool name  
  
Returns
    void 



* * *

The documentation for this class was generated from the following file:

  * [CDhcpv6ServerProcess.pki](_c_dhcpv6_server_process_8pki.html)


