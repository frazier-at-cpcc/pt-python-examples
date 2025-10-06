# Cisco Packet Tracer Extensions API: MacSwitch Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_mac_switch.html

---

[MacSwitch](class_mac_switch.html "MacSwitch handles and manipulates the MAC address table.") handles and manipulates the MAC address table. [More...](class_mac_switch.html#details)

##  Public Member Functions  
  
---  
bool | [addStaticMac](class_mac_switch.html#a074753b9ea7f4b097b5925ac273575ca) (mac, int, string)  
| Adds a static MAC address to the specified port. [More...](class_mac_switch.html#a074753b9ea7f4b097b5925ac273575ca)  
  
bool | [removeStaticMac](class_mac_switch.html#a0feaf3b4c693112f60279980166742f9) (mac, int, string)  
| Removes the static MAC address from the specified port. [More...](class_mac_switch.html#a0feaf3b4c693112f60279980166742f9)  
  
int | [getStaticMacCount](class_mac_switch.html#a05e5773ed43da8eddcf81fba8c614fdd) ()  
| Returns the number of static MAC addresses configured. [More...](class_mac_switch.html#a05e5773ed43da8eddcf81fba8c614fdd)  
  
[StaticMac](struct_static_mac.html) | [getGlobalMacAt](class_mac_switch.html#a1c8942693f09782399cf1d6c94691061) (int)  
| Returns the static MAC address at the specified index. [More...](class_mac_switch.html#a1c8942693f09782399cf1d6c94691061)  
  
bool | [portExistedInStatic](class_mac_switch.html#aa85a3b45108295735db8f8381fc4be54) (string)  
bool | [isEntryExisted](class_mac_switch.html#a8ab9ff0b81446180e4a3544ad5e60c20) (mac, int, string)  
| Returns true if the specified entry exists in the MAC address table, otherwise false. [More...](class_mac_switch.html#a8ab9ff0b81446180e4a3544ad5e60c20)  
  
void | [updateTableEvent](class_mac_switch.html#a11890ae5570a28cde4d2cf9749f6318c) ()  
| Event triggered when the table is updated. [More...](class_mac_switch.html#a11890ae5570a28cde4d2cf9749f6318c)  
  
void | [closeTableEvent](class_mac_switch.html#aa5ab34b7a132c95800c85b91b84e7705) ()  
| Event triggered when the table is closed/deleted. [More...](class_mac_switch.html#aa5ab34b7a132c95800c85b91b84e7705)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[MacSwitch](class_mac_switch.html "MacSwitch handles and manipulates the MAC address table.") handles and manipulates the MAC address table. 

## Member Function Documentation

## ◆ addStaticMac()

bool MacSwitch::addStaticMac  | ( | mac  | ,   
---|---|---|---  
|  | int  | ,   
|  | string  |   
| ) | |   
  
Adds a static MAC address to the specified port. 

Parameters
     macAddress,the| static MAC address.   
---|---  
vlanNumber,the| VLAN number.   
portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ closeTableEvent()

void MacSwitch::closeTableEvent  | ( | | ) |   
---|---|---|---|---  
  
Event triggered when the table is closed/deleted. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ getGlobalMacAt()

[StaticMac](struct_static_mac.html) MacSwitch::getGlobalMacAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the static MAC address at the specified index. 

Parameters
     index,the| index of the static MAC address of interest.  
---|---  
  
Returns
    [StaticMac](struct_static_mac.html "Data element for StaticMac."), the [StaticMac](struct_static_mac.html "Data element for StaticMac.") object at the specified index. 

## ◆ getStaticMacCount()

int MacSwitch::getStaticMacCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of static MAC addresses configured. 

Returns
    int, the number of static MAC addresses configured. 

## ◆ isEntryExisted()

bool MacSwitch::isEntryExisted  | ( | mac  | ,   
---|---|---|---  
|  | int  | ,   
|  | string  |   
| ) | |   
  
Returns true if the specified entry exists in the MAC address table, otherwise false. 

Parameters
     macAddress,the| static MAC address of interest.   
---|---  
vlanNumber,the| VLAN number of interest.   
portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    bool, true if the specified entry exists in the MAC address table, otherwise false. 

## ◆ portExistedInStatic()

bool MacSwitch::portExistedInStatic  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Parameters
     Returns| true if the specified port has a static MAC address, otherwise false.  
---|---  
portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    bool, true if the specified port has a static MAC address, otherwise false. 

## ◆ removeStaticMac()

bool MacSwitch::removeStaticMac  | ( | mac  | ,   
---|---|---|---  
|  | int  | ,   
|  | string  |   
| ) | |   
  
Removes the static MAC address from the specified port. 

Parameters
     macAddress,the| static MAC address of interest.   
---|---  
vlanNumber,the| VLAN number of interest.   
portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ updateTableEvent()

void MacSwitch::updateTableEvent  | ( | | ) |   
---|---|---|---|---  
  
Event triggered when the table is updated. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CMacSwitcher.pki](_c_mac_switcher_8pki.html)


