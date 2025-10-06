# Cisco Packet Tracer Extensions API: Vlan Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_vlan.html

---

[Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN.") handles and manipulates the individual VLAN. [More...](class_vlan.html#details)

##  Public Member Functions  
  
---  
string | [getName](class_vlan.html#aaa71a468b90296cda0896cb4333fac70) ()  
| Returns the name of this VLAN. [More...](class_vlan.html#aaa71a468b90296cda0896cb4333fac70)  
  
[MacTable](struct_mac_table.html) | [getMacTable](class_vlan.html#a26f726dca047d437957d83b96ebda268) ()  
| Returns the MAC address table. [More...](class_vlan.html#a26f726dca047d437957d83b96ebda268)  
  
bool | [isDefault](class_vlan.html#a2f7036f311b7926df8fb11cb72bfe1d8) ()  
| Returns true if this is the default VLAN, otherwise false. [More...](class_vlan.html#a2f7036f311b7926df8fb11cb72bfe1d8)  
  
int | [getVlanNumber](class_vlan.html#a48645c33cae9294e821b58bee390b541) ()  
| Returns the VLAN number of this VLAN. [More...](class_vlan.html#a48645c33cae9294e821b58bee390b541)  
  
void | [macEntryAdded](class_vlan.html#a0407fe3ff96a744cc53b5e9e18b54742) (mac, string, bool)  
| This event is emitted when a MAC address entry is added. [More...](class_vlan.html#a0407fe3ff96a744cc53b5e9e18b54742)  
  
void | [macEntryRemoved](class_vlan.html#a4512110e99712313ce5c82a9b4141855) (mac, string, bool)  
| This event is emitted when a MAC address entry is removed. [More...](class_vlan.html#a4512110e99712313ce5c82a9b4141855)  
  
  
## Detailed Description

[Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN.") handles and manipulates the individual VLAN. 

## Member Function Documentation

## ◆ getMacTable()

[MacTable](struct_mac_table.html) Vlan::getMacTable  | ( | | ) |   
---|---|---|---|---  
  
Returns the MAC address table. 

Returns
    [MacTable](struct_mac_table.html "Data element for MAC tables."), the [MacTable](struct_mac_table.html "Data element for MAC tables.") object. 

## ◆ getName()

string Vlan::getName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of this VLAN. 

Returns
    string, the name of this VLAN. 

## ◆ getVlanNumber()

int Vlan::getVlanNumber  | ( | | ) |   
---|---|---|---|---  
  
Returns the VLAN number of this VLAN. 

Returns
    int, the VLAN number of this VLAN. 

## ◆ isDefault()

bool Vlan::isDefault  | ( | | ) |   
---|---|---|---|---  
  
Returns true if this is the default VLAN, otherwise false. 

Returns
    bool, true if this is the default VLAN, otherwise false. 

## ◆ macEntryAdded()

void Vlan::macEntryAdded  | ( | mac  | ,   
---|---|---|---  
|  | string  | ,   
|  | bool  |   
| ) | |   
  
This event is emitted when a MAC address entry is added. 

  * newMac, the new MAC address that was added. 
  * portName, the name of the associated port. 
  * isDynamic, true if dynamic, otherwise false.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ macEntryRemoved()

void Vlan::macEntryRemoved  | ( | mac  | ,   
---|---|---|---  
|  | string  | ,   
|  | bool  |   
| ) | |   
  
This event is emitted when a MAC address entry is removed. 

  * newMac, the new MAC address that was removed. 
  * portName, the name of the associated port. 
  * isDynamic, true if dynamic, otherwise false.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CVlan.pki](_c_vlan_8pki.html)


