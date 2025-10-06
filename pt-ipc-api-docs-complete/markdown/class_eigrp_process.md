# Cisco Packet Tracer Extensions API: EigrpProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_eigrp_process.html

---

[EigrpProcess](class_eigrp_process.html "EigrpProcess is the process that handles the individual EIGRP AS process.") is the process that handles the individual EIGRP AS process. [More...](class_eigrp_process.html#details)

##  Public Member Functions  
  
---  
int | [getASNumber](class_eigrp_process.html#acd061d547a338e460c093f6b4484c3a0) ()  
| Returns the AS number of this EIGRP process. [More...](class_eigrp_process.html#acd061d547a338e460c093f6b4484c3a0)  
  
void | [setKs](class_eigrp_process.html#a369c8cc932fa248c09daa3763ffef960) (int, int, int, int, int)  
| Sets the K-values to the specified values. [More...](class_eigrp_process.html#a369c8cc932fa248c09daa3763ffef960)  
  
void | [setVariance](class_eigrp_process.html#a2bd7ca1b5a7a714af31ca0e0646c8aa3) (int)  
| Sets the variance to the specified value. [More...](class_eigrp_process.html#a2bd7ca1b5a7a714af31ca0e0646c8aa3)  
  
int | [getVariance](class_eigrp_process.html#a5313a6e72c4e7e2454c60727a878c6b9) ()  
| Returns the variance of this EIGRP process. [More...](class_eigrp_process.html#a5313a6e72c4e7e2454c60727a878c6b9)  
  
void | [setAutoSummary](class_eigrp_process.html#a8471983cb3e2cfe63c6213cc1f5c4dbc) (bool)  
| Enables or disables auto summary on this EIGRP process. [More...](class_eigrp_process.html#a8471983cb3e2cfe63c6213cc1f5c4dbc)  
  
bool | [getAutoSummary](class_eigrp_process.html#a063d2a2d05c90e5c067d93d199f29c4b) ()  
| Returns true if auto summary is enabled on this EIGRP process, otherwise false. [More...](class_eigrp_process.html#a063d2a2d05c90e5c067d93d199f29c4b)  
  
void | [setDefaultPassiveInt](class_eigrp_process.html#a6a09a812e53ed473955f1f7d56173467) (bool)  
| Enables or disables default passive interface on this EIGRP process. [More...](class_eigrp_process.html#a6a09a812e53ed473955f1f7d56173467)  
  
bool | [getDefaultPassiveInt](class_eigrp_process.html#a88c4027e3d248554a86c74bcde81e531) ()  
| Returns true if default passive interface is enabled on this EIGRP process, otherwise false. [More...](class_eigrp_process.html#a88c4027e3d248554a86c74bcde81e531)  
  
void | [setPassiveInt](class_eigrp_process.html#a920378ada8348d2442a3ed955a90a7a2) (string, bool)  
| Enables or disables passive interface on the specified port. [More...](class_eigrp_process.html#a920378ada8348d2442a3ed955a90a7a2)  
  
bool | [isPassiveInt](class_eigrp_process.html#a477ab1302afc6f14f7bf9bab14b23edd) (string)  
| Returns true if passive interface is enabled on the specified port, otherwise false. [More...](class_eigrp_process.html#a477ab1302afc6f14f7bf9bab14b23edd)  
  
void | [setIntAdminDistance](class_eigrp_process.html#a82e5dba9e1e98de1d9cc84a857f63147) (int)  
| Sets the internal administrative distance on this EIGRP process. [More...](class_eigrp_process.html#a82e5dba9e1e98de1d9cc84a857f63147)  
  
void | [setExtAdminDistance](class_eigrp_process.html#a92f0dd04748d4ba49f6fbcabdb73b503) (int)  
| Sets the external administrative distance on this EIGRP process. [More...](class_eigrp_process.html#a92f0dd04748d4ba49f6fbcabdb73b503)  
  
void | [addConfiguredNetwork](class_eigrp_process.html#a9a88bb5192b7105cb7c0cf2dd60738b1) (ip, ip)  
| Adds the network with the specified network address and mask to this EIGRP process. [More...](class_eigrp_process.html#a9a88bb5192b7105cb7c0cf2dd60738b1)  
  
void | [removeConfiguredNetwork](class_eigrp_process.html#af79542ec784536f9b0b1072f084151b9) (ip, ip)  
| Removes the network with the specified network address and mask from this EIGRP process. [More...](class_eigrp_process.html#af79542ec784536f9b0b1072f084151b9)  
  
int | [getConfiguredNetworkCount](class_eigrp_process.html#a00e78da80e20cd7f7481c14c843a0653) ()  
| Returns the number of networks in this EIGRP process. [More...](class_eigrp_process.html#a00e78da80e20cd7f7481c14c843a0653)  
  
bool | [addSummaryAddress](class_eigrp_process.html#a13f848f205ea9521e8a697f01e196fc1) (string, ip, ip, int)  
| Adds a summary aggregate address to the specified port. [More...](class_eigrp_process.html#a13f848f205ea9521e8a697f01e196fc1)  
  
bool | [removeSummaryAddress](class_eigrp_process.html#aa78d352dc565133b03f80bbf4a16c46b) (string, ip, ip, int)  
| Removes a summary aggregate address to the specified port. [More...](class_eigrp_process.html#aa78d352dc565133b03f80bbf4a16c46b)  
  
int | [getSummaryAddressCount](class_eigrp_process.html#af2c16928f1b65346f3c971b276619c41) (string)  
| Returns the number of summary aggregate addresses on the specified port. [More...](class_eigrp_process.html#af2c16928f1b65346f3c971b276619c41)  
  
[EigrpSummaryAddress](struct_eigrp_summary_address.html) | [getSummaryAddressAt](class_eigrp_process.html#a4f0e9b17e523186619de2c82c8a56a7d) (string, int, int)  
| Returns the summary aggregate address on the specified port, AS number, and index. [More...](class_eigrp_process.html#a4f0e9b17e523186619de2c82c8a56a7d)  
  
[EigrpTopologyTable](struct_eigrp_topology_table.html) | [getTopologyTable](class_eigrp_process.html#a214b1645bf3aa034233b31eeaa50a375) ()  
| Returns the topology table of this EIGRP process. [More...](class_eigrp_process.html#a214b1645bf3aa034233b31eeaa50a375)  
  
[EigrpNeighborTable](class_eigrp_neighbor_table.html) | [getNeighborTable](class_eigrp_process.html#ac670c874a77fce90c2d8887342d51e8f) ()  
| Returns the neighbor table of this EIGRP process. [More...](class_eigrp_process.html#ac670c874a77fce90c2d8887342d51e8f)  
  
Public Member Functions inherited from [RoutingProtocol](class_routing_protocol.html)  
void | [setAdminDistance](class_routing_protocol.html#a1f39516098814724cf82c520c510de71) (int)  
| Sets the administrative distance. [More...](class_routing_protocol.html#a1f39516098814724cf82c520c510de71)  
  
int | [getAdminDistance](class_routing_protocol.html#a297c8e3af679475657e71c9363970289) ()  
| Returns the administrative distance. [More...](class_routing_protocol.html#a297c8e3af679475657e71c9363970289)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[EigrpProcess](class_eigrp_process.html "EigrpProcess is the process that handles the individual EIGRP AS process.") is the process that handles the individual EIGRP AS process. 

## Member Function Documentation

## ◆ addConfiguredNetwork()

void EigrpProcess::addConfiguredNetwork  | ( | ip  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Adds the network with the specified network address and mask to this EIGRP process. 

Parameters
     ipAddress,the| network address.   
---|---  
mask,the| network mask.   
  
## ◆ addSummaryAddress()

bool EigrpProcess::addSummaryAddress  | ( | string  | ,   
---|---|---|---  
|  | ip  | ,   
|  | ip  | ,   
|  | int  |   
| ) | |   
  
Adds a summary aggregate address to the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
ipAddress,the| summary IP address.   
subnet,the| summary subnet mask.   
adminDistance,the| administrative distance.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getASNumber()

int EigrpProcess::getASNumber  | ( | | ) |   
---|---|---|---|---  
  
Returns the AS number of this EIGRP process. 

Returns
    int, the AS number of this EIGRP process. 

## ◆ getAutoSummary()

bool EigrpProcess::getAutoSummary  | ( | | ) |   
---|---|---|---|---  
  
Returns true if auto summary is enabled on this EIGRP process, otherwise false. 

Returns
    bool, true if auto summary is enabled on this EIGRP process, otherwise false. 

## ◆ getConfiguredNetworkCount()

int EigrpProcess::getConfiguredNetworkCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of networks in this EIGRP process. 

Returns
    int, the number of networks in this EIGRP process. 

## ◆ getDefaultPassiveInt()

bool EigrpProcess::getDefaultPassiveInt  | ( | | ) |   
---|---|---|---|---  
  
Returns true if default passive interface is enabled on this EIGRP process, otherwise false. 

Returns
    bool, true if default passive interface is enabled on this EIGRP process, otherwise false. 

## ◆ getNeighborTable()

[EigrpNeighborTable](class_eigrp_neighbor_table.html) EigrpProcess::getNeighborTable  | ( | | ) |   
---|---|---|---|---  
  
Returns the neighbor table of this EIGRP process. 

Returns
    [EigrpNeighborTable](class_eigrp_neighbor_table.html "EigrpNeighborTable holds the EIGRP neighbor table."), the [EigrpNeighborTable](class_eigrp_neighbor_table.html "EigrpNeighborTable holds the EIGRP neighbor table.") object of this EIGRP process. 

## ◆ getSummaryAddressAt()

[EigrpSummaryAddress](struct_eigrp_summary_address.html) EigrpProcess::getSummaryAddressAt  | ( | string  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  |   
| ) | |   
  
Returns the summary aggregate address on the specified port, AS number, and index. 

Parameters
     portName| portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
as,the| autonomous system of the summary aggregate address of interest.   
index,the| index of the summary aggregate address of interest.  
  
Returns
    [EigrpSummaryAddress](struct_eigrp_summary_address.html "Data element for EIGRP summary addresses."), the [EigrpSummaryAddress](struct_eigrp_summary_address.html "Data element for EIGRP summary addresses.") object on the specified port, AS number, and index. 

## ◆ getSummaryAddressCount()

int EigrpProcess::getSummaryAddressCount  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the number of summary aggregate addresses on the specified port. 

Parameters
     portName| portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    int, the number of summary aggregate addresses on the specified port. 

## ◆ getTopologyTable()

[EigrpTopologyTable](struct_eigrp_topology_table.html) EigrpProcess::getTopologyTable  | ( | | ) |   
---|---|---|---|---  
  
Returns the topology table of this EIGRP process. 

Returns
    [EigrpTopologyTable](struct_eigrp_topology_table.html "Data element for EIGRP topology tables."), the [EigrpTopologyTable](struct_eigrp_topology_table.html "Data element for EIGRP topology tables.") object of this EIGRP process. 

## ◆ getVariance()

int EigrpProcess::getVariance  | ( | | ) |   
---|---|---|---|---  
  
Returns the variance of this EIGRP process. 

Returns
    int, the variance of this EIGRP process. 

## ◆ isPassiveInt()

bool EigrpProcess::isPassiveInt  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if passive interface is enabled on the specified port, otherwise false. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    bool, true if passive interface is enabled on the specified port, otherwise false. 

## ◆ removeConfiguredNetwork()

void EigrpProcess::removeConfiguredNetwork  | ( | ip  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Removes the network with the specified network address and mask from this EIGRP process. 

Parameters
     ipAddress,the| network address of interest.   
---|---  
mask,the| network mask of interest.   
  
## ◆ removeSummaryAddress()

bool EigrpProcess::removeSummaryAddress  | ( | string  | ,   
---|---|---|---  
|  | ip  | ,   
|  | ip  | ,   
|  | int  |   
| ) | |   
  
Removes a summary aggregate address to the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
ipAddress,the| summary IP address.   
subnet,the| summary subnet mask.   
adminDistance,the| administrative distance.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ setAutoSummary()

void EigrpProcess::setAutoSummary  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables auto summary on this EIGRP process. 

Parameters
     bAutoSum,true| to enable auto summary, false to disable it.   
---|---  
  
## ◆ setDefaultPassiveInt()

void EigrpProcess::setDefaultPassiveInt  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables default passive interface on this EIGRP process. 

Parameters
     bEnable,true| to enable default passive interface on this EIGRP process, false to disable it.   
---|---  
  
## ◆ setExtAdminDistance()

void EigrpProcess::setExtAdminDistance  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the external administrative distance on this EIGRP process. 

Parameters
     adminDistance,the| external administrative distance.   
---|---  
  
## ◆ setIntAdminDistance()

void EigrpProcess::setIntAdminDistance  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the internal administrative distance on this EIGRP process. 

Parameters
     adminDistance,the| internal administrative distance.   
---|---  
  
## ◆ setKs()

void EigrpProcess::setKs  | ( | int  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
Sets the K-values to the specified values. 

Parameters
     k1,the| K1 value.   
---|---  
k2,the| K2 value.   
k3,the| K3 value.   
k4,the| K4 value.   
k5,the| K5 value.   
  
## ◆ setPassiveInt()

void EigrpProcess::setPassiveInt  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables passive interface on the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
bPassive,true| to enable passive interface, false to disable it.   
  
## ◆ setVariance()

void EigrpProcess::setVariance  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the variance to the specified value. 

Parameters
     variance,the| variance value.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CEIGRPProcess.pki](_c_e_i_g_r_p_process_8pki.html)


