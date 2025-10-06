# Cisco Packet Tracer Extensions API: DhcpServerMainProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_dhcp_server_main_process.html

---

[DhcpServerMainProcess](class_dhcp_server_main_process.html "DhcpServerMainProcess is the process manager that handles many DHCP server processes.") is the process manager that handles many DHCP server processes. [More...](class_dhcp_server_main_process.html#details)

##  Public Member Functions  
  
---  
[DhcpServerProcess](class_dhcp_server_process.html) | [getDhcpServerProcessByPortName](class_dhcp_server_main_process.html#a5cd21aa7d72dafb399059c5800d94736) (string)  
| Returns the [DhcpServerProcess](class_dhcp_server_process.html "DhcpServerProcess is the process that handles DHCP pools and leases.") object of the specified port. [More...](class_dhcp_server_main_process.html#a5cd21aa7d72dafb399059c5800d94736)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[DhcpServerMainProcess](class_dhcp_server_main_process.html "DhcpServerMainProcess is the process manager that handles many DHCP server processes.") is the process manager that handles many DHCP server processes. 

## Member Function Documentation

## ◆ getDhcpServerProcessByPortName()

[DhcpServerProcess](class_dhcp_server_process.html) DhcpServerMainProcess::getDhcpServerProcessByPortName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the [DhcpServerProcess](class_dhcp_server_process.html "DhcpServerProcess is the process that handles DHCP pools and leases.") object of the specified port. 

Parameters
     portName,the| name of the port of interest.  
---|---  
  
Returns
    [DhcpServerProcess](class_dhcp_server_process.html "DhcpServerProcess is the process that handles DHCP pools and leases."), the DHCP server process object of the specified port. 

* * *

The documentation for this class was generated from the following file:

  * [CDhcpServerMainProcess.pki](_c_dhcp_server_main_process_8pki.html)


