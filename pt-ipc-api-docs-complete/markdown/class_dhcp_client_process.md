# Cisco Packet Tracer Extensions API: DhcpClientProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_dhcp_client_process.html

---

[DhcpClientProcess](class_dhcp_client_process.html "DhcpClientProcess handles the DHCP client process.") handles the DHCP client process. [More...](class_dhcp_client_process.html#details)

##  Public Member Functions  
  
---  
void | [removePortDataEntry](class_dhcp_client_process.html#a842a754fd263024ce06ab23af7856618) (string)  
| Runs DHCP on the specified port. [More...](class_dhcp_client_process.html#a842a754fd263024ce06ab23af7856618)  
  
void | [addPortDataEntry](class_dhcp_client_process.html#a8c4f7e79e49026a7c29f7aa6527595c5) (string)  
bool | [isPortExisted](class_dhcp_client_process.html#a1067d950d4fbe2bf87073f0f8e0d530a) (string)  
| Runs DHCP on the specified port. [More...](class_dhcp_client_process.html#a1067d950d4fbe2bf87073f0f8e0d530a)  
  
void | [dhcpRun](class_dhcp_client_process.html#a874c6dbe5db5e00cf7bf1d9c0fc8de20) (string)  
| Start dhcp process on the specified port. [More...](class_dhcp_client_process.html#a874c6dbe5db5e00cf7bf1d9c0fc8de20)  
  
bool | [dhcpRelease](class_dhcp_client_process.html#a12f8496bfd1102a1011c37a4714eb7c9) (string)  
| Releases the DHCP lease from the specified port. [More...](class_dhcp_client_process.html#a12f8496bfd1102a1011c37a4714eb7c9)  
  
bool | [resetDhcpConfOn](class_dhcp_client_process.html#a30b2c1cf157de2b3ff58f908e3b2b812) (string)  
| Resets the DHCP configuration on the specified port. [More...](class_dhcp_client_process.html#a30b2c1cf157de2b3ff58f908e3b2b812)  
  
void | [dhcpSucceed](class_dhcp_client_process.html#a6b2c837a826c6758e75c36813590bd2f) (QString, string, ip, ip)  
| This event is emitted when the process receives a DHCP acknowledgement packet. [More...](class_dhcp_client_process.html#a6b2c837a826c6758e75c36813590bd2f)  
  
void | [dhcpConfigured](class_dhcp_client_process.html#a131bb749b7ba64afd897e6baee072555) (QString, string, bool)  
| This event is emitted when the process has determined that DHCP is configured. [More...](class_dhcp_client_process.html#a131bb749b7ba64afd897e6baee072555)  
  
void | [dhcpFailed](class_dhcp_client_process.html#a8970f48fad2d5657787f25a768ab48b2) (QString, string)  
| This event is emitted when a DHCP request fails. [More...](class_dhcp_client_process.html#a8970f48fad2d5657787f25a768ab48b2)  
  
[DhcpClientPortData](class_dhcp_client_port_data.html) | [getDataOfPort](class_dhcp_client_process.html#acbaa93bb573d80949a8b82c7adbad060) (string)  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[DhcpClientProcess](class_dhcp_client_process.html "DhcpClientProcess handles the DHCP client process.") handles the DHCP client process. 

## Member Function Documentation

## ◆ addPortDataEntry()

void DhcpClientProcess::addPortDataEntry  | ( | string  | | ) |   
---|---|---|---|---|---  
  
## ◆ dhcpConfigured()

void DhcpClientProcess::dhcpConfigured  | ( | QString  | ,   
---|---|---|---  
|  | string  | ,   
|  | bool  |   
| ) | |   
  
This event is emitted when the process has determined that DHCP is configured. 

  * deviceName, the name of the device. 
  * portName, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0 
  * isConfigured, true if DHCP is configured, otherwise false.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ dhcpFailed()

void DhcpClientProcess::dhcpFailed  | ( | QString  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
This event is emitted when a DHCP request fails. 

  * deviceName, the name of the device. 
  * portName, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ dhcpRelease()

bool DhcpClientProcess::dhcpRelease  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Releases the DHCP lease from the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ dhcpRun()

void DhcpClientProcess::dhcpRun  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Start dhcp process on the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
  
## ◆ dhcpSucceed()

void DhcpClientProcess::dhcpSucceed  | ( | QString  | ,   
---|---|---|---  
|  | string  | ,   
|  | ip  | ,   
|  | ip  |   
| ) | |   
  
This event is emitted when the process receives a DHCP acknowledgement packet. 

  * deviceName, the name of the device. 
  * portName, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0 
  * newip, the IP address that was leased. 
  * newmask, the subnet mask that was leased.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ getDataOfPort()

[DhcpClientPortData](class_dhcp_client_port_data.html) DhcpClientProcess::getDataOfPort  | ( | string  | | ) |   
---|---|---|---|---|---  
  
## ◆ isPortExisted()

bool DhcpClientProcess::isPortExisted  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Runs DHCP on the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ removePortDataEntry()

void DhcpClientProcess::removePortDataEntry  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Runs DHCP on the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
  
## ◆ resetDhcpConfOn()

bool DhcpClientProcess::resetDhcpConfOn  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Resets the DHCP configuration on the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CDhcpClientProcess.pki](_c_dhcp_client_process_8pki.html)


