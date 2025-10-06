# Cisco Packet Tracer Extensions API: Dhcpv6ClientProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_dhcpv6_client_process.html

---

[Dhcpv6ClientProcess](class_dhcpv6_client_process.html "Dhcpv6ClientProcess handles the DHCPv6 client process.") handles the DHCPv6 client process. [More...](class_dhcpv6_client_process.html#details)

##  Public Member Functions  
  
---  
void | [enableDhcpClient](class_dhcpv6_client_process.html#a37dbb9e2f6890cba0a40d9bd8d57723b) (Dhcpv6::EDhcpv6ClientEnabled, string, string)  
| Enable Dhcp Client process. [More...](class_dhcpv6_client_process.html#a37dbb9e2f6890cba0a40d9bd8d57723b)  
  
bool | [isDhcpClientEnabled](class_dhcpv6_client_process.html#a2beef2590f88eded62998a0a437c4cbf) ()  
| Check if DHCP Client is enabled. [More...](class_dhcpv6_client_process.html#a2beef2590f88eded62998a0a437c4cbf)  
  
void | [dhcpSucceed](class_dhcpv6_client_process.html#aceddeb7f2becd7b4f245e2bb44476455) (QString, string, ip, int)  
| This event is emitted when dhcp succeeds. [More...](class_dhcpv6_client_process.html#aceddeb7f2becd7b4f245e2bb44476455)  
  
void | [dhcpFailed](class_dhcpv6_client_process.html#adee5b805e8bc12cb52980681bcfdc4f3) (QString, string)  
| This event is emitted when dhcp fails. [More...](class_dhcpv6_client_process.html#adee5b805e8bc12cb52980681bcfdc4f3)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[Dhcpv6ClientProcess](class_dhcpv6_client_process.html "Dhcpv6ClientProcess handles the DHCPv6 client process.") handles the DHCPv6 client process. 

## Member Function Documentation

## ◆ dhcpFailed()

void Dhcpv6ClientProcess::dhcpFailed  | ( | QString  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
This event is emitted when dhcp fails. 

Parameters
     deviceName,the| device name in QString format  
---|---  
portName,the| port name in string format  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ dhcpSucceed()

void Dhcpv6ClientProcess::dhcpSucceed  | ( | QString  | ,   
---|---|---|---  
|  | string  | ,   
|  | ip  | ,   
|  | int  |   
| ) | |   
  
This event is emitted when dhcp succeeds. 

Parameters
     deviceName,the| device name in QString format  
---|---  
portName,the| port name in string format  
  
\newip, new ip address

\prefix, prefix info

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ enableDhcpClient()

void Dhcpv6ClientProcess::enableDhcpClient  | ( | Dhcpv6::EDhcpv6ClientEnabled  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  |   
| ) | |   
  
Enable Dhcp Client process. 

Parameters
     enable,enum<Dhcpv6::EDhcpv6ClientEnabled>| eClientEnabled_No = 0, eClientEnabled_ViaDhcp = 1, eClientEnabled_ViaNd = 2  
---|---  
portName,port| name  
prefixName,prefix| name   
  
## ◆ isDhcpClientEnabled()

bool Dhcpv6ClientProcess::isDhcpClientEnabled  | ( | | ) |   
---|---|---|---|---  
  
Check if DHCP Client is enabled. 

Parameters
     bool,return| true if enabled and false if not   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CDhcpv6ClientProcess.pki](_c_dhcpv6_client_process_8pki.html)


