# Cisco Packet Tracer Extensions API: Dhcpv6MainProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_dhcpv6_main_process.html

---

[Dhcpv6MainProcess](class_dhcpv6_main_process.html "Dhcpv6MainProcess handles the DHCPv6 main process.") handles the DHCPv6 main process. [More...](class_dhcpv6_main_process.html#details)

##  Public Member Functions  
  
---  
[Dhcpv6ClientProcess](class_dhcpv6_client_process.html) | [getDhcpClientProcess](class_dhcpv6_main_process.html#a2b4861389071409f81b3859da6c5dd9d) (string)  
| get [Dhcpv6ClientProcess](class_dhcpv6_client_process.html "Dhcpv6ClientProcess handles the DHCPv6 client process.") object [More...](class_dhcpv6_main_process.html#a2b4861389071409f81b3859da6c5dd9d)  
  
void | [enableDhcpClient](class_dhcpv6_main_process.html#ac49e816b49a05bcfab331c7a2caafc95) (Dhcpv6ClientEnabled, string, string, bool, bool, bool)  
| enable [Dhcpv6ClientProcess](class_dhcpv6_client_process.html "Dhcpv6ClientProcess handles the DHCPv6 client process.") [More...](class_dhcpv6_main_process.html#ac49e816b49a05bcfab331c7a2caafc95)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[Dhcpv6MainProcess](class_dhcpv6_main_process.html "Dhcpv6MainProcess handles the DHCPv6 main process.") handles the DHCPv6 main process. 

## Member Function Documentation

## ◆ enableDhcpClient()

void Dhcpv6MainProcess::enableDhcpClient  | ( | Dhcpv6ClientEnabled  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  | ,   
|  | bool  | ,   
|  | bool  | ,   
|  | bool  |   
| ) | |   
  
enable [Dhcpv6ClientProcess](class_dhcpv6_client_process.html "Dhcpv6ClientProcess handles the DHCPv6 client process.")

Parameters
     enable,enum<Dhcpv6::EDhcpv6ClientEnabled>| eClientEnabled_No = 0, eClientEnabled_ViaDhcp = 1, eClientEnabled_ViaNd = 2  
---|---  
portName,port| name  
prefixName,prefix| name   
  
bStatelessConfig,flag| for stateless config, true if enabled and false if not  
bStatelessConfigManagedFlag,flag| for stateless config managed, true if enabled and false if not  
bStatelessConfigOtherFlag,flag| for stateless config other, true if enabled and false if not   
  
## ◆ getDhcpClientProcess()

[Dhcpv6ClientProcess](class_dhcpv6_client_process.html) Dhcpv6MainProcess::getDhcpClientProcess  | ( | string  | | ) |   
---|---|---|---|---|---  
  
get [Dhcpv6ClientProcess](class_dhcpv6_client_process.html "Dhcpv6ClientProcess handles the DHCPv6 client process.") object 

Returns
    [Dhcpv6ClientProcess](class_dhcpv6_client_process.html "Dhcpv6ClientProcess handles the DHCPv6 client process."), [Dhcpv6ClientProcess](class_dhcpv6_client_process.html "Dhcpv6ClientProcess handles the DHCPv6 client process.") object 

* * *

The documentation for this class was generated from the following file:

  * [CDhcpv6MainProcess.pki](_c_dhcpv6_main_process_8pki.html)


