# Cisco Packet Tracer Extensions API: OspfArea Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ospf_area.html

---

[OspfArea](class_ospf_area.html "OspfArea handles and manipulates OSPF areas.") handles and manipulates OSPF areas. [More...](class_ospf_area.html#details)

##  Public Member Functions  
  
---  
ip | [getAreaId](class_ospf_area.html#a135e5b161fa74f9d5c91a110f56a13e3) ()  
| Returns the OSPF area ID. [More...](class_ospf_area.html#a135e5b161fa74f9d5c91a110f56a13e3)  
  
void | [setAuthentication](class_ospf_area.html#ac129b35dbe37beff0eb512647b81a61e) (OspfAuthType)  
| Sets the OSPF authentication type. [More...](class_ospf_area.html#ac129b35dbe37beff0eb512647b81a61e)  
  
OspfAuthType | [getAuthentication](class_ospf_area.html#a3f73e48116358371ba59ab43b1002242) ()  
| Returns the OSPF authentication type. [More...](class_ospf_area.html#a3f73e48116358371ba59ab43b1002242)  
  
int | [getConfiguredPortCount](class_ospf_area.html#a67eb3b18bef07cb15bba6c15191b5f42) ()  
| Returns the number of configured ports. [More...](class_ospf_area.html#a67eb3b18bef07cb15bba6c15191b5f42)  
  
int | [getConfiguredNetworkCount](class_ospf_area.html#ae4a8666c9d27514191b23cbc1b58ad85) ()  
| Returns the number of configured networks. [More...](class_ospf_area.html#ae4a8666c9d27514191b23cbc1b58ad85)  
  
pair< ip, ip > | [getConfiguredNetworkAt](class_ospf_area.html#a7dd2ad1c0d982b559704c5e6a071806e) (int)  
| Returns the network address and subnet mask at the specified index. [More...](class_ospf_area.html#a7dd2ad1c0d982b559704c5e6a071806e)  
  
[OspfNeighborTable](class_ospf_neighbor_table.html) | [getNeighborTable](class_ospf_area.html#a42c1b481ae315748622bb92dc6e87630) (string)  
| Returns the OSPF neighbor table of the specifed port. [More...](class_ospf_area.html#a42c1b481ae315748622bb92dc6e87630)  
  
[OspfDatabase](struct_ospf_database.html) | [getDatabase](class_ospf_area.html#a66127982db90ae2d7220245e8c9ab114) ()  
| Return the OSPF database. [More...](class_ospf_area.html#a66127982db90ae2d7220245e8c9ab114)  
  
int | [getFloodLength](class_ospf_area.html#a81099bbd2018bf909e6002c40097495b) (string)  
| Returns the flood length of the specified port. [More...](class_ospf_area.html#a81099bbd2018bf909e6002c40097495b)  
  
int | [getLastFloodLength](class_ospf_area.html#a5e79c2c931542a216e8b6d446a291ac8) (string)  
| Returns the last flood length of the specified port. [More...](class_ospf_area.html#a5e79c2c931542a216e8b6d446a291ac8)  
  
int | [getLastFloodTime](class_ospf_area.html#a89b4dc86cd7e322b7004b4be3d119ee8) (string)  
| Returns the last flood time of the specified port. [More...](class_ospf_area.html#a89b4dc86cd7e322b7004b4be3d119ee8)  
  
int | [getMaxFloodLength](class_ospf_area.html#ac87bf7fb8f5c7183e30449d2c70674fd) (string)  
| Returns the maximum flood length of the specified port. [More...](class_ospf_area.html#ac87bf7fb8f5c7183e30449d2c70674fd)  
  
int | [getMaxFloodTime](class_ospf_area.html#aa97aceffa023c9cfc923f1303fb64afe) (string)  
| Returns the maximum flood time of the specified port. [More...](class_ospf_area.html#aa97aceffa023c9cfc923f1303fb64afe)  
  
int | [getSpfCount](class_ospf_area.html#a53e426616a8c0f5e8efe44dd0d3146c0) ()  
| Returns the number of shortest paths. [More...](class_ospf_area.html#a53e426616a8c0f5e8efe44dd0d3146c0)  
  
  
## Detailed Description

[OspfArea](class_ospf_area.html "OspfArea handles and manipulates OSPF areas.") handles and manipulates OSPF areas. 

## Member Function Documentation

## ◆ getAreaId()

ip OspfArea::getAreaId  | ( | | ) |   
---|---|---|---|---  
  
Returns the OSPF area ID. 

Parameters
     ip,the| OSPF area ID.   
---|---  
  
## ◆ getAuthentication()

OspfAuthType OspfArea::getAuthentication  | ( | | ) |   
---|---|---|---|---  
  
Returns the OSPF authentication type. 

Returns
    enum<OspfAuthType>, the OSPF authentication type. Authentication types: eNoAuth = 0, eAuth = 1, eMD5Auth = 2 

## ◆ getConfiguredNetworkAt()

pair< ip, ip > OspfArea::getConfiguredNetworkAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the network address and subnet mask at the specified index. 

Parameters
     index,the| index of the network address and subnet mask of interest.  
---|---  
  
Returns
    pair<ip, ip>, the network address and subnet mask at the specified index. 

## ◆ getConfiguredNetworkCount()

int OspfArea::getConfiguredNetworkCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of configured networks. 

Returns
    int, the number of configured networks. 

## ◆ getConfiguredPortCount()

int OspfArea::getConfiguredPortCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of configured ports. 

Returns
    int, the number of configured ports. 

## ◆ getDatabase()

[OspfDatabase](struct_ospf_database.html) OspfArea::getDatabase  | ( | | ) |   
---|---|---|---|---  
  
Return the OSPF database. 

Returns
    [OspfDatabase](struct_ospf_database.html "Data element for OspfDatabase."), the [OspfDatabase](struct_ospf_database.html "Data element for OspfDatabase.") object. 

## ◆ getFloodLength()

int OspfArea::getFloodLength  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the flood length of the specified port. 

Parameters
     portName| portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    int, the flood length of the specified port. 

## ◆ getLastFloodLength()

int OspfArea::getLastFloodLength  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the last flood length of the specified port. 

Parameters
     portName| portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    int, the last flood length of the specified port. 

## ◆ getLastFloodTime()

int OspfArea::getLastFloodTime  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the last flood time of the specified port. 

Parameters
     portName| portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    int, the last flood time of the specified port. 

## ◆ getMaxFloodLength()

int OspfArea::getMaxFloodLength  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the maximum flood length of the specified port. 

Parameters
     portName| portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    int, the maximum flood length of the specified port. 

## ◆ getMaxFloodTime()

int OspfArea::getMaxFloodTime  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the maximum flood time of the specified port. 

Parameters
     portName| portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    int, the maximum flood time of the specified port. 

## ◆ getNeighborTable()

[OspfNeighborTable](class_ospf_neighbor_table.html) OspfArea::getNeighborTable  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the OSPF neighbor table of the specifed port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    [OspfNeighborTable](class_ospf_neighbor_table.html "OspfNeighborTable handles and manipulates OSPF neighbor tables."), the [OspfNeighborTable](class_ospf_neighbor_table.html "OspfNeighborTable handles and manipulates OSPF neighbor tables.") object of the specifed port. 

## ◆ getSpfCount()

int OspfArea::getSpfCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of shortest paths. 

Returns
    int, the number of shortest paths. 

## ◆ setAuthentication()

void OspfArea::setAuthentication  | ( | OspfAuthType  | | ) |   
---|---|---|---|---|---  
  
Sets the OSPF authentication type. 

Parameters
     type,the| OSPF authentication type. Authentication types: eNoAuth = 0, eAuth = 1, eMD5Auth = 2   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [COspfArea.pki](_c_ospf_area_8pki.html)


