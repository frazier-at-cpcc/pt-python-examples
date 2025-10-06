# Cisco Packet Tracer Extensions API: Dhcpv6ServerMainProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_dhcpv6_server_main_process.html

---

[Dhcpv6ServerMainProcess](class_dhcpv6_server_main_process.html "Dhcpv6ServerMainProcess handles the DHCPv6 server main process.") handles the DHCPv6 server main process. [More...](class_dhcpv6_server_main_process.html#details)

##  Public Member Functions  
  
---  
void | [enableDhcpServer](class_dhcpv6_server_main_process.html#a0fa5416d1eee54871c72732381cc97f5) (bool, [HostPort](class_host_port.html), std::string &, bool)  
| Enables/Disables DHCPv6 server. [More...](class_dhcpv6_server_main_process.html#a0fa5416d1eee54871c72732381cc97f5)  
  
Public Member Functions inherited from [Dhcpv6MainProcess](class_dhcpv6_main_process.html)  
[Dhcpv6ClientProcess](class_dhcpv6_client_process.html) | [getDhcpClientProcess](class_dhcpv6_main_process.html#a2b4861389071409f81b3859da6c5dd9d) (string)  
| get [Dhcpv6ClientProcess](class_dhcpv6_client_process.html "Dhcpv6ClientProcess handles the DHCPv6 client process.") object [More...](class_dhcpv6_main_process.html#a2b4861389071409f81b3859da6c5dd9d)  
  
void | [enableDhcpClient](class_dhcpv6_main_process.html#ac49e816b49a05bcfab331c7a2caafc95) (Dhcpv6ClientEnabled, string, string, bool, bool, bool)  
| enable [Dhcpv6ClientProcess](class_dhcpv6_client_process.html "Dhcpv6ClientProcess handles the DHCPv6 client process.") [More...](class_dhcpv6_main_process.html#ac49e816b49a05bcfab331c7a2caafc95)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[Dhcpv6ServerMainProcess](class_dhcpv6_server_main_process.html "Dhcpv6ServerMainProcess handles the DHCPv6 server main process.") handles the DHCPv6 server main process. 

## Member Function Documentation

## ◆ enableDhcpServer()

void Dhcpv6ServerMainProcess::enableDhcpServer  | ( | bool  | ,   
---|---|---|---  
|  | [HostPort](class_host_port.html) | ,   
|  | std::string & | ,   
|  | bool  |   
| ) | |   
  
Enables/Disables DHCPv6 server. 

  * enable, flag to enable or disable the DHCPv6 client 

Parameters
     pPort| the port that the DHCPv6 server resides on   
---|---  
poolName| the DHCPv6 pool name   
isToBeDeleted| this flag used in deserialize() for CServer  
  
Returns
    void 



* * *

The documentation for this class was generated from the following file:

  * [CDhcpv6ServerMainProcess.pki](_c_dhcpv6_server_main_process_8pki.html)


